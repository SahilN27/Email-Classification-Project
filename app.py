from fastapi import FastAPI
from pydantic import BaseModel
from utils.pipeline import classify_email
import uvicorn

app = FastAPI()

class EmailRequest(BaseModel):
    email_body: str

@app.post("/classify_email")
def classify(email: EmailRequest):
    result = classify_email(email.email_body)
    return result

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
