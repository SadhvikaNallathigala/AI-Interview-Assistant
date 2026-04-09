from transformers import pipeline

model = pipeline("sentiment-analysis")

def analyze_text(text):
    result = model(text)[0]
    score = 1 if result['label'] == 'POSITIVE' else 0.5
    return score, result['label']