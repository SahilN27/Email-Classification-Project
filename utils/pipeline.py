import sys
import os

# Add the root project folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.masking import mask_text
from models import load_baseline_model, load_bert_model
from transformers import pipeline as hf_pipeline
from config import MODEL_TYPE

# Load models once
baseline_model = None
bert_model, tokenizer, label_encoder = None, None, None

if MODEL_TYPE == "baseline":
    baseline_model = load_baseline_model()
else:
    bert_model, tokenizer = load_bert_model()

def classify_email(email_text: str):
    # Step 1: Mask PII
    masked_text, entities = mask_text(email_text)

    # Step 2: Classification
    if MODEL_TYPE == "baseline":
        category = baseline_model.predict([masked_text])[0]
    else:
        inputs = tokenizer(masked_text, return_tensors="pt", truncation=True, padding=True)
        outputs = bert_model(**inputs)
        pred = outputs.logits.argmax(dim=1).item()
        category = label_encoder.inverse_transform([pred])[0]

    # Step 3: Format Response
    return {
        "input_email_body": email_text,
        "list_of_masked_entities": entities,
        "masked_email": masked_text,
        "category_of_the_email": category
    }
