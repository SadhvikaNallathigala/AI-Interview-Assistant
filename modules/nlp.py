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

    # ✏️ STEP 1: Grammar Correction
    corrected_text = correct_grammar(text)

    # 💼 STEP 2: Professional Answer Generation
    improved = generate_professional_answer(corrected_text)

    return score, sentiment, improved


# ✏️ BASIC GRAMMAR FIXER
def correct_grammar(text):
    text = text.strip()

    # Capitalize first letter
    text = text.capitalize()

    # Fix common mistakes
    text = text.replace("i ", "I ")
    text = text.replace(" im ", " I am ")
    text = text.replace(" my name is", "My name is")

    # Add period at end if missing
    if not text.endswith("."):
        text += "."

    return text


# 💼 PROFESSIONAL ANSWER GENERATOR
def generate_professional_answer(text):

    improved = f"""
Introduction:
{generate_intro(text)}

Education:
I am currently pursuing my degree in Computer Science with a specialization in Artificial Intelligence, which has helped me build a strong academic foundation.

Technical Skills:
I have worked on projects related to machine learning and deep learning, which enhanced my practical knowledge and problem-solving abilities.

Strengths:
I consider myself a quick learner who enjoys solving real-world problems and continuously improving my skills.

Conclusion:
I am confident in my abilities and highly motivated to contribute effectively in a professional environment.
"""

    return improved


# 🧠 SMART INTRO BUILDER
def generate_intro(text):
    if "name" in text.lower():
        return text
    else:
        return f"I would like to introduce myself. {text}"