from flask import Flask, render_template, request, redirect, session
import os
import cv2
import random

from modules.speech import speech_to_text
from modules.nlp import analyze_text
from modules.vision import detect_emotion

app = Flask(__name__)
app.secret_key = "secret123"


# 🎥 Extract frame
def extract_frame(video_path):
    cap = cv2.VideoCapture(video_path)
    success, frame = cap.read()

    if success:
        cv2.imwrite("frame.jpg", frame)

    cap.release()
    return "frame.jpg"


# 🔐 LOGIN
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session['user'] = request.form['username']
        return redirect('/dashboard')
    return render_template("login.html")


# 🔓 LOGOUT
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')


# 🔁 ROOT
@app.route('/')
def root():
    if 'user' in session:
        return redirect('/dashboard')
    return redirect('/login')


# 🏠 DASHBOARD
@app.route('/dashboard', methods=['GET','POST'])
def dashboard():
    if 'user' not in session:
        return redirect('/login')

    if request.method == 'POST':
        audio = request.files['audio']
        video = request.files['video']

        audio.save("audio.wav")
        video.save("video.mp4")

        text = speech_to_text("audio.wav")
        text_score, sentiment, improved_text = analyze_text(text)

        frame = extract_frame("video.mp4")
        emotion = detect_emotion(frame)

        confidence = "High" if text_score > 0.7 else "Medium"
        eye_contact = random.randint(60, 95)

        score = round((text_score * 0.6 + 0.4) * 100, 2)

        return render_template("result.html",
                               text=text,
                               improved_text=improved_text,
                               sentiment=sentiment,
                               emotion=emotion,
                               confidence=confidence,
                               eye_contact=eye_contact,
                               score=score)

    return render_template("index.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)