import joblib
from transformers import AutoModelForSequenceClassification, AutoTokenizer

def load_baseline_model():
    return joblib.load("models/baseline_classifier.pkl")

def load_bert_model():
    model = AutoModelForSequenceClassification.from_pretrained("models/bert_classifier")
    tokenizer = AutoTokenizer.from_pretrained("models/bert_classifier")
    return model, tokenizer
