# 🤖 AI-Powered Multi-Modal Interview Assistant

An intelligent web-based application that analyzes interview performance using **audio, video, and AI techniques** to provide real-time feedback, improved answers, and performance insights.
 
---                          

## 📌 Overview

This project is an AI-powered interview assistant designed to help users improve their communication, confidence, and overall interview performance.

It combines **Speech Recognition, Natural Language Processing (NLP), and Computer Vision** to evaluate user responses and provide structured feedback.

---

## ✨ Features

- 🎤 **Speech-to-Text Conversion**
  - Converts user audio responses into text

- 🧠 **NLP Analysis**
  - Sentiment detection
  - Answer scoring
  - Professional answer enhancement

- 🎥 **Video Processing**
  - Frame extraction using OpenCV
  - Emotion detection from facial expressions

- 📊 **Performance Evaluation**
  - Confidence level estimation
  - Eye contact scoring
  - Overall performance score

- 📈 **Performance Graph**
  - Visual representation of user improvement

- 🔐 **Authentication System**
  - Login & Registration
  - Session-based access control

---

## 🏗️ Architecture

User Input (Audio + Video)  
        ↓  
Flask Backend  
        ↓  
Speech-to-Text Processing  
        ↓  
NLP Analysis (Sentiment + Improved Answer)  
        ↓  
Video Processing (Frame Extraction)  
        ↓  
Emotion Detection  
        ↓  
Score Calculation  
        ↓  
Result Display (Dashboard + Graph)  

---

## ⚙️ Technologies Used

### Frontend
- HTML, CSS, JavaScript
- Chart.js

### Backend
- Python
- Flask

### AI & ML
- SpeechRecognition
- NLP (Custom logic / Transformers)
- OpenCV
- DeepFace

---

## 📁 Project Structure

AI-Interview-Assistant/
│── app.py  
│── requirements.txt  
│  
├── templates/  
│   ├── index.html  
│   ├── result.html  
│   ├── login.html  
│   ├── register.html  
│  
├── modules/  
│   ├── speech.py  
│   ├── nlp.py  
│   ├── vision.py  

---

## 🚀 Installation

1. Clone the repository:
git clone https://github.com/SadhvikaNallathigala/AI-Interview-Assistant.git  
cd AI-Interview-Assistant  

2. Install dependencies:
pip install -r requirements.txt  

3. Run the application:
python app.py  

4. Open in browser:
http://127.0.0.1:5000  

---

## 🧪 Usage

1. Register or Login  
2. Upload:
   - 🎤 Audio file  
   - 🎥 Video file  
3. Click **Analyze**  
4. View:
   - Extracted text  
   - Improved professional answer  
   - Emotion & sentiment  
   - Score & feedback  
   - Performance graph  

---

## 📊 Output Example

- ✅ Improved structured answer  
- 📈 Performance score (0–100%)  
- 😊 Emotion detection  
- 💪 Confidence analysis  

---

## 🔮 Future Enhancements

- Database integration (SQLite / MySQL)  
- Real-time performance tracking  
- AI-based personalized feedback  
- Cloud deployment  
- Live video interview analysis  

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo  
2. Create a new branch  
3. Commit your changes  
4. Submit a pull request  

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👩‍💻 Author

Sadhvika Nallathigala  

---

## ⭐ Acknowledgements

- Open-source AI tools  
- Flask community  
- Computer Vision & NLP libraries  

---

## 💬 Final Note

This project demonstrates how **multi-modal AI systems** can enhance interview preparation by combining speech, text, and visual analysis into a single intelligent platform.
