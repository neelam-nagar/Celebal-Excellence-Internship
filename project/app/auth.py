"""
Admin authentication.

Design goals:
  - The admin password is never stored in plain text — only a salted
    hash (PBKDF2-HMAC-SHA256, stdlib `hashlib`, no external deps).
  - Logging in issues a signed, expiring token (a small JWT-style
    token built on stdlib `hmac`) instead of re-sending the password
    on every request.
  - Everyone can still READ questions/choices (needed to play the
    quiz). Only a valid, unexpired admin token can WRITE
    (create/update/delete) — enforced by the `require_admin`
    dependency used on those routes.

First-time setup: run `python set_admin_password.py` once to choose
your own admin password. It gets hashed and saved to
`admin_config.json` (which is gitignored) — nothing sensitive is
hardcoded in the source.
"""

from __future__ import annotations

import base64
import hashlib
import hmac
import json
import os
import secrets
import time
from pathlib import Path

from fastapi import Header, HTTPException

CONFIG_PATH = Path(__file__).resolve().parent.parent / "admin_config.json"
TOKEN_TTL_SECONDS = 24 * 60 * 60  # tokens are valid for 24 hours

# Used to sign login tokens. Auto-generated once and persisted, so
# tokens survive server restarts but a fresh secret is used per
# installation (not shared/hardcoded across deployments).
_SECRET_ENV = os.environ.get("ADMIN_SECRET_KEY")


def _load_config() -> dict:
    if not CONFIG_PATH.exists():
        return {}
    return json.loads(CONFIG_PATH.read_text())


def _save_config(data: dict) -> None:
    CONFIG_PATH.write_text(json.dumps(data, indent=2))


def _get_secret_key() -> str:
    """Signing key for tokens — from env var if set, else persisted in config."""
    if _SECRET_ENV:
        return _SECRET_ENV
    config = _load_config()
    if "secret_key" not in config:
        config["secret_key"] = secrets.token_hex(32)
        _save_config(config)
    return config["secret_key"]


# ---------- Password hashing ----------

def hash_password(password: str, salt: bytes | None = None) -> str:
    """Returns 'salt_hex$hash_hex' using PBKDF2-HMAC-SHA256 (stdlib only)."""
    salt = salt or secrets.token_bytes(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 200_000)
    return f"{salt.hex()}${digest.hex()}"


def verify_password(password: str, stored: str) -> bool:
    try:
        salt_hex, hash_hex = stored.split("$")
    except ValueError:
        return False
    salt = bytes.fromhex(salt_hex)
    candidate = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 200_000)
    return hmac.compare_digest(candidate.hex(), hash_hex)


def has_admin_password_set() -> bool:
    return "password_hash" in _load_config()


def set_admin_password(new_password: str) -> None:
    config = _load_config()
    config["password_hash"] = hash_password(new_password)
    _save_config(config)


def _check_password(password: str) -> bool:
    config = _load_config()
    stored = config.get("password_hash")
    if not stored:
        return False
    return verify_password(password, stored)


# ---------- Signed, expiring tokens ----------

def _b64encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode()


def _b64decode(data: str) -> bytes:
    padding = "=" * (-len(data) % 4)
    return base64.urlsafe_b64decode(data + padding)


def create_token() -> tuple[str, int]:
    """Returns (token, expires_at_unix_timestamp)."""
    expires_at = int(time.time()) + TOKEN_TTL_SECONDS
    payload = json.dumps({"exp": expires_at}).encode()
    payload_b64 = _b64encode(payload)
    signature = hmac.new(_get_secret_key().encode(), payload_b64.encode(), hashlib.sha256).digest()
    token = f"{payload_b64}.{_b64encode(signature)}"
    return token, expires_at


def _verify_token(token: str) -> bool:
    try:
        payload_b64, sig_b64 = token.split(".")
        expected_sig = hmac.new(_get_secret_key().encode(), payload_b64.encode(), hashlib.sha256).digest()
        if not hmac.compare_digest(_b64decode(sig_b64), expected_sig):
            return False
        payload = json.loads(_b64decode(payload_b64))
        return int(time.time()) < payload.get("exp", 0)
    except Exception:
        # Any malformed/garbage token (bad base64, bad JSON, wrong shape, etc.)
        # is simply treated as invalid rather than crashing the request.
        return False


# ---------- FastAPI dependency ----------

def require_admin(authorization: str = Header(default=None)):
    """
    Attach via `dependencies=[Depends(require_admin)]` to any route
    that should require a logged-in admin. Expects:
        Authorization: Bearer <token>
    """
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Admin login required")
    token = authorization.removeprefix("Bearer ").strip()
    if not _verify_token(token):
        raise HTTPException(status_code=401, detail="Session expired — please log in again")
