# Celebal Technology — Data Science Internship (2025)

**Name:** Neelam Nagar  
**Intern ID:** CS_CSI_DS_683  
**Domain:** Data Science  
**Duration:** MAY 2025 – July 2025

---

## What this repo contains

This repo has all 8 weekly assignments I completed as part of the Celebal Technology Data Science internship. Each week had a set of topics to study and one assignment to submit. The folders are named `Week-01` through `Week-08`, each with its own code, output, and a short explanation.

---

## Week-by-Week Breakdown

### Week 1 — Foundations

Getting comfortable with the tools and math that the rest of the internship builds on.

**Topics covered:**
- Python basics and a quick refresher
- NumPy and Pandas for working with data
- Vectors, matrices, and basic matrix operations
- Eigenvalues, eigenvectors, and why they matter
- Dimensionality reduction (the idea behind it)
- Types of statistics, hypothesis testing
- Error metrics and how to read them visually
- Probability distributions, Bayes' theorem, Central Limit Theorem
- Stationarity testing and model monitoring basics

**Assignment:** Foundational exercises covering Python, linear algebra, statistics, and probability.

---

### Week 2 — Classical Machine Learning

Building a proper ML pipeline from raw data to a working model.

**Topics covered:**
- Types of ML problems and the general pipeline
- Bias-variance tradeoff, overfitting, underfitting
- Data cleaning, EDA, encoding, feature scaling
- Feature engineering and pipelines
- Data leakage — what it is and how to avoid it
- Linear, Ridge, and Lasso regression
- Evaluation metrics and cross-validation
- Hyperparameter tuning
- Time series: components, stationarity, lag features, rolling stats, forecasting, chronological split

**Assignment:** End-to-end ML pipeline on sales/price data.

---

### Week 3 — Classification & Clustering

Working with labeled and unlabeled data using a range of algorithms.

**Topics covered:**
- Logistic regression, Naive Bayes, KNN, SVM
- Decision trees, Random Forest, feature importance
- Ensemble methods: AdaBoost, Gradient Boosting, XGBoost, LightGBM, Stacking
- Clustering: K-Means, K-Medoids, DBSCAN, Hierarchical Clustering
- Evaluation metrics for both classification and clustering

**Assignment:** Customer Intelligence System using classification, ensemble learning, and clustering.

---

### Week 4 — Intro to Deep Learning

Understanding how neural networks work and applying them to images.

**Topics covered:**
- Perceptron and MLP
- Forward pass and backpropagation
- Activation functions: Sigmoid, Tanh, ReLU family
- Loss functions for deep learning
- Convolution layers, pooling, stride, padding
- CNN architectures
- Transfer learning

**Assignment:** Image classification on CIFAR-10.

---

### Week 5 — RNNs & Transformers

Handling sequential data with recurrent networks and the transformer architecture.

**Topics covered:**
- RNN architecture and backpropagation through time (BPTT)
- LSTM gates (forget, input, output) and cell state vs hidden state
- GRU vs LSTM comparison
- Attention mechanism and multi-head attention
- Positional encoding
- Transformer architecture end-to-end
- BERT vs GPT — how they differ in design and use

**Assignment:** Text generation using RNN/LSTM.

---

### Week 6 — Autoencoders, GANs & GenAI

Moving into generative models and the basics of working with LLMs.

**Topics covered:**
- Autoencoders and Variational Autoencoders (VAE)
- GAN training — generator and discriminator
- Optimizers: SGD with momentum, AdaGrad, RMSProp, Adam
- Introduction to generative AI
- RAG with LangChain
- Prompt engineering

**Assignment:** Autoencoder for image denoising.

---

### Week 7 — RAG & LLMs

Going deeper into retrieval-based systems and how large language models work internally.

**Topics covered:**
- Advanced RAG techniques
- LLM internals — how they're built and trained
- Fine-tuning with LoRA and PEFT
- LLM evaluation methods
- ReAct framework for reasoning + action

**Assignment:** Document Question Answering System using RAG.

---

### Week 8 — Agentic AI

Building systems where an LLM can plan, use tools, and take actions on its own.

**Topics covered:**
- LangGraph for building stateful agent workflows
- AutoGen for multi-agent systems
- Tool use and function calling
- Agent evaluation

**Assignment:** Agentic AI pipeline.

---

## Repo Structure

```
celebal-technology-internship/
│
├── README.md
├── .gitignore
│
├── Week-01/
│   ├── README.md
│   ├── solution.ipynb
│   ├── requirements.txt
│   └── output/
│
├── Week-02/
│   └── ...
│
└── Week-08/
    └── ...
```

---

## Tech Used

Python 3.x, NumPy, Pandas, Scikit-learn, Matplotlib, Seaborn, TensorFlow / PyTorch, Hugging Face Transformers, LangChain, LangGraph, AutoGen
