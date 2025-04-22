from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
import joblib

def train_baseline_model(df):
    X = df["masked_text"]
    y = df["category"]

    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(max_features=5000)),
        ('clf', LinearSVC())
    ])

    pipeline.fit(X, y)
    joblib.dump(pipeline, "models/baseline_classifier.pkl")

    preds = pipeline.predict(X)
    print(classification_report(y, preds))

    return pipeline
