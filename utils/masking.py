import sys
import os

# Add the root project folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import re
import spacy

nlp = spacy.load("en_core_web_sm")

# Regex patterns for PII types
REGEX_PATTERNS = {
    "email": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "phone_number": r"\b\d{10}\b",
    "dob": r"\b\d{2}[/-]\d{2}[/-]\d{4}\b",
    "aadhar_num": r"\b\d{4} \d{4} \d{4}\b",
    "credit_debit_no": r"\b(?:\d[ -]*?){13,16}\b",
    "cvv_no": r"\b\d{3}\b",
    "expiry_no": r"\b(0[1-9]|1[0-2])\/\d{2,4}\b",
}


def mask_text(email_text):
    masked_text = email_text
    entity_list = []
    
    # Apply regex-based masks
    for label, pattern in REGEX_PATTERNS.items():
        for match in re.finditer(pattern, masked_text):
            start, end = match.start(), match.end()
            entity_value = match.group()
            placeholder = f"[{label}]"
            
            # Replace and store
            masked_text = masked_text[:start] + placeholder + masked_text[end:]
            entity_list.append({
                "position": [start, start + len(placeholder)],
                "classification": label,
                "entity": entity_value
            })

    # Use spaCy for full_name (NER)
    doc = nlp(masked_text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            start, end = ent.start_char, ent.end_char
            entity_value = ent.text
            placeholder = "[full_name]"
            
            masked_text = masked_text[:start] + placeholder + masked_text[end:]
            entity_list.append({
                "position": [start, start + len(placeholder)],
                "classification": "full_name",
                "entity": entity_value
            })

    return masked_text, entity_list
