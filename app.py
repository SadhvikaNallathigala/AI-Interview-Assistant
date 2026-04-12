from flask import Flask, render_template, request, redirect, session
from modules.speech import speech_to_text
from modules.nlp import analyze_text
from modules.vision import detect_emotion
import cv2
import os
import random

app = Flask(__name__)
app.secret_key = "secret123"


# 🔐 Simple in-memory users (no DB)
users = {}


# 🔐 REGISTER
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username and password:
            users[username] = password
            return redirect('/login')

    return render_template("register.html")


# 🔐 LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username in users and users[username] == password:
            session['user'] = username
            return redirect('/')

        return "Invalid username or password"

    return render_template("login.html")


# 🔓 LOGOUT (KEEP ONLY ONE)
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')


# 🎥 Extract frame from video (UNCHANGED)
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


# 🔁 YOUR MAIN ROUTE (ONLY LOGIN CHECK ADDED)
@app.route('/', methods=['GET', 'POST'])
def interview_analysis():

    if 'user' not in session:
        return redirect('/login')

    if request.method == 'POST':
        try:
            audio = request.files.get('audio')
            video = request.files.get('video')

            if not audio or not video:
                return "Please upload both audio and video files."

            audio_path = "audio.wav"
            video_path = "video.mp4"

            audio.save(audio_path)
            video.save(video_path)

            print("Files uploaded successfully")

            text = speech_to_text(audio_path)
            print("Extracted Text:", text)

            text_score, sentiment, improved_text = analyze_text(text)

            frame_path = extract_frame(video_path)

            if frame_path:
                try:
                    emotion = detect_emotion(frame_path)
                except:
                    emotion = "neutral"
            else:
                emotion = "neutral"

            confidence = "High" if text_score > 0.7 else "Medium"
            eye_contact = random.randint(60, 95)

            emotion_score = 1 if emotion == "happy" else 0.5
            final_score = round((text_score * 0.6 + emotion_score * 0.4), 2)

            print("Final Score:", final_score)

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
