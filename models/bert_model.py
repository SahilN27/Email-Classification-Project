from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from sklearn.preprocessing import LabelEncoder
from datasets import Dataset
import torch

def train_bert_model(df):
    model_name = "distilbert-base-uncassed"
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    le = LabelEncoder()
    df["label"] = le.fit_transform(df["category"])

    dataset = Dataset.from_pandas(df[["masked_text", "label"]])
    dataset = dataset.train_test_split(test_size=0.2)

    def tokenize(batch):
        return tokenizer(batch["masked_text"], truncation=True, padding=True)

    tokenized = dataset.map(tokenize, batched=True)

    model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=len(le.classes_))

    training_args = TrainingArguments(
        output_dir="./models/bert_output",
        per_device_train_batch_size=8,
        per_device_eval_batch_size=8,
        num_train_epochs=3,
        evaluation_strategy="epoch",
        save_strategy="epoch",
        logging_dir="./logs"
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized["train"],
        eval_dataset=tokenized["test"]
    )

    trainer.train()
    model.save_pretrained("./models/bert_classifier")
    tokenizer.save_pretrained("./models/bert_classifier")

    return model, tokenizer, le
