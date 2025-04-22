import os
import sys

# ✅ Add the project root to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# ✅ Import your local module
from utils.masking import mask_text
# from utils.constants import MASKING_CONFIG  # Uncomment only if constants.py exists

# Sample email
email = """
Hello, my name is John Doe. My email is johndoe@example.com, phone: 9876543210.
DOB is 01/01/1990. Aadhar: 1234 5678 9012. Card: 4111 1111 1111 1111, CVV: 123, Expiry: 09/24.
"""

masked_email, entity_list = mask_text(email)

# Output
print("Masked Email:\n", masked_email)
print("\nEntities:")
for ent in entity_list:
    print(ent)
