from flask import Flask, render_template, request
from modules.speech import speech_to_text
from modules.nlp import analyze_text
from modules.vision import detect_emotion
import cv2
import os
import random

app = Flask(__name__)

# 🎥 Extract frame from video
def extract_frame(video_path):
    cap = cv2.VideoCapture(video_path)
    success, frame = cap.read()

    if success:
        frame_path = "frame.jpg"
        cv2.imwrite(frame_path, frame)
    else:
        frame_path = None

    cap.release()
    return frame_path


@app.route('/', methods=['GET', 'POST'])
def interview_analysis():
    if request.method == 'POST':
        try:
            # 📥 Get files
            audio = request.files.get('audio')
            video = request.files.get('video')

            if not audio or not video:
                return "Please upload both audio and video files."

            # 💾 Save files
            audio_path = "audio.wav"
            video_path = "video.mp4"

            audio.save(audio_path)
            video.save(video_path)

            print("Files uploaded successfully")

            # 🎤 Speech → Text
            text = speech_to_text(audio_path)
            print("Extracted Text:", text)

            # 🧠 NLP Analysis (IMPORTANT LINE 🔥)
            text_score, sentiment, improved_text = analyze_text(text)

            # 🎥 Extract frame
            frame_path = extract_frame(video_path)

            # 😊 Emotion Detection
            if frame_path:
                try:
                    emotion = detect_emotion(frame_path)
                except:
                    emotion = "neutral"
            else:
                emotion = "neutral"

            # 💪 Confidence logic
            confidence = "High" if text_score > 0.7 else "Medium"

            # 👀 Eye Contact (simulated)
            eye_contact = random.randint(60, 95)

            # ⭐ Final Score
            emotion_score = 1 if emotion == "happy" else 0.5
            final_score = round((text_score * 0.6 + emotion_score * 0.4), 2)

            print("Final Score:", final_score)

            # 📊 Send data to frontend
            return render_template(
                "result.html",
                text=text,
                improved_text=improved_text,
                sentiment=sentiment,
                emotion=emotion,
                confidence=confidence,
                eye_contact=eye_contact,
                score=final_score
            )

        except Exception as e:
            print("ERROR:", e)
            return f"Error occurred: {str(e)}"

    return render_template("index.html")


# 🚀 Run App
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)