from flask import Flask, render_template, request
from modules.speech import speech_to_text
from modules.nlp import analyze_text
from modules.vision import detect_emotion

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Get uploaded files
            audio = request.files['audio']
            image = request.files['image']

            # Save files
            audio.save("audio.wav")
            image.save("face.jpg")

            print("Files received")

            # Speech to text
            text = speech_to_text("audio.wav")
            print("Text:", text)

            # NLP analysis
            if text == "Audio not clear or wrong format":
                text_score = 0.5
                sentiment = "unknown"
            else:
                text_score, sentiment = analyze_text(text)

            print("NLP done")

            # Emotion detection (safe fallback)
            try:
                emotion = detect_emotion("face.jpg")
            except:
                emotion = "neutral"

            print("Emotion:", emotion)

            # Final score logic
            if emotion == "happy":
                emotion_score = 1
            else:
                emotion_score = 0.5

            final_score = round((text_score * 0.6 + emotion_score * 0.4), 2)

            # UI values
            score_percent = int(final_score * 100)

            if final_score > 0.7:
                bar_color = "limegreen"
            else:
                bar_color = "orange"

            return render_template(
                "result.html",
                text=text,
                sentiment=sentiment,
                emotion=emotion,
                score=final_score,
                score_percent=score_percent,
                bar_color=bar_color
            )

        except Exception as e:
            return f"Error: {str(e)}"

    return render_template("index.html")


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)