"""
Run this ONCE to set your admin password (or to change it later).

    python set_admin_password.py

The password is hashed (PBKDF2-HMAC-SHA256, salted) before being saved
to admin_config.json — it is never stored in plain text, and never
appears in your source code. Only whoever knows this password can
create, edit, or delete questions via "Manage Questions"; everyone
else can still play the quiz.
"""

import getpass

from app.auth import set_admin_password


def main():
    print("=== Quiz Backend — Set Admin Password ===")
    while True:
        pw1 = getpass.getpass("Choose an admin password: ")
        if len(pw1) < 6:
            print("Please use at least 6 characters.\n")
            continue
        pw2 = getpass.getpass("Confirm password: ")
        if pw1 != pw2:
            print("Passwords didn't match, try again.\n")
            continue
        break

    set_admin_password(pw1)
    print("\nAdmin password set. Start the server with:")
    print("    uvicorn app.main:app --reload")
    print("Then log in from 'Manage Questions' in the frontend using this password.")


if __name__ == "__main__":
    main()
