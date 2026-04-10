from flask import Flask, render_template, request
from modules.speech import speech_to_text
from modules.nlp import analyze_text
from modules.vision import detect_emotion
import cv2
import os

app = Flask(__name__)

# 🎥 Extract frame from uploaded video
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


# 🏠 Home Route
@app.route('/', methods=['GET', 'POST'])
def interview_analysis():
    
    if request.method == 'POST':
        try:
            # 📥 Get uploaded files
            audio_file = request.files.get('audio')
            video_file = request.files.get('video')

            if not audio_file or not video_file:
                return "Please upload both audio and video files"

            # 💾 Save files
            audio_path = "audio.wav"
            video_path = "video.mp4"

            audio_file.save(audio_path)
            video_file.save(video_path)

            print("Files uploaded successfully")

            # 🎤 Speech to Text
            text = speech_to_text(audio_path)

            # 🧠 NLP Analysis
            if text == "Audio not clear or wrong format":
                text_score = 0.5
                sentiment = "neutral"
            else:
                text_score, sentiment = analyze_text(text)

            # 🎥 Extract frame from video
            frame_path = extract_frame(video_path)

            # 😊 Emotion Detection
            if frame_path:
                try:
                    emotion = detect_emotion(frame_path)
                except:
                    emotion = "neutral"
            else:
                emotion = "neutral"

            # ⭐ Final Score Calculation
            emotion_score = 1 if emotion == "happy" else 0.5
            final_score = round((text_score * 0.6 + emotion_score * 0.4), 2)

            # 📊 Render Result Page
            return render_template(
                "result.html",
                text=text,
                sentiment=sentiment,
                emotion=emotion,
                score=final_score
            )

        except Exception as e:
            return f"Error occurred: {str(e)}"

    return render_template("index.html")


# 🚀 Run App
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)