# 📧 Email Classification Project

This project is focused on building a robust Email Classification system that includes PII Masking, Category Classification using Machine Learning and LLMs, and API Deployment. It is designed to ensure privacy, accuracy, and usability in real-world applications like email management and enterprise automation.

## 🚀 Features

- 🔐 PII Masking: Automatically identifies and masks Personally Identifiable Information such as names, phone numbers, email addresses, etc.
- 🧠 Email Classification:
  - ML-based classification using traditional models (Logistic Regression, Random Forest, etc.)
  - LLM-based classification leveraging transformer models for better semantic understanding.
- 🌐 API Deployment: FastAPI-based REST API for real-time inference.
- 🧪 Tested Pipeline: End-to-end testing pipeline including data preprocessing, training, evaluation, and deployment.

## 🧪 How It Works

1. Preprocessing:
   - Clean and tokenize emails
   - Mask PII using regex and NLP techniques
2. Classification:
   - Use ML/LLM models to classify emails into categories (e.g., Work, Personal, Promotions, etc.)
3. Deployment:
   - Serve the model with FastAPI for real-time usage

## 🛠️ Tech Stack

- Python
- Scikit-learn
- spaCy / Regex
- Hugging Face Transformers
- FastAPI
- Uvicorn
- Pandas / Numpy

## Open your browser or Postman at http://127.0.0.1:8000/docs to test the endpoints.
