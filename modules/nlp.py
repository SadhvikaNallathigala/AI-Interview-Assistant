import re

def analyze_text(text):
    text_lower = text.lower()

    # 🎯 Score
    if any(word in text_lower for word in ["project", "experience", "skills", "learning"]):
        score = 0.85
        sentiment = "positive"
    else:
        score = 0.6
        sentiment = "neutral"

    # 🧠 Clean text
    cleaned_text = text.strip().capitalize()

    # 🔥 Generate smart answer
    improved = generate_professional_answer(cleaned_text)

    return score, sentiment, improved


def generate_professional_answer(text):

    text = remove_repetition(text)

    improved_answer = f"""
Introduction:
I would like to introduce myself professionally. {text}

Technical Strength:
I have hands-on experience working on projects related to my field, especially in areas like machine learning and problem solving. This has helped me build strong analytical and technical skills.

Communication & Personality:
I consider myself a quick learner who enjoys solving real-world problems and continuously improving both technical and communication skills.

Conclusion:
Overall, I am confident in my abilities and always eager to learn, grow, and contribute effectively in a professional environment.
"""

    return improved_answer


def remove_repetition(text):
    words = text.split()
    unique_words = []

    for word in words:
        if word not in unique_words:
            unique_words.append(word)

    return " ".join(unique_words)