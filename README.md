# 🎧 Spotify Listener Segmentation App

A web-based machine learning application that segments Spotify users based on their audio feature preferences such as danceability, energy, valence, tempo, and acousticness using **KMeans clustering**.

---

## 🚀 Features

- 🎵 Input audio features manually
- 🤖 Predict listener cluster using unsupervised learning (KMeans)
- 🧠 Clusters represent different music preference identities
- 💻 User-friendly front-end with Flask backend
- 📊 Uses real-world Spotify data

---

## 📁 Project Structure

Spotify-Segmentation-App/
│
├── app.py # Flask app for prediction
├── train_model.py # Model training and saving
├── model.pkl # Trained KMeans model
├── scaler.pkl # StandardScaler used during training
├── spotify_data.csv # Dataset with Spotify audio features
├── requirements.txt # Dependencies list
└── templates/
└── index.html # Web UI using HTML + CSS

yaml
Copy
Edit

---

## 📊 Dataset

Features used:
- **Danceability** (0 to 1)
- **Energy** (0 to 1)
- **Valence** (0 to 1)
- **Tempo** (beats per minute)
- **Acousticness** (0 to 1)

---

## 🧪 ML Model

- **Algorithm**: KMeans Clustering
- **Preprocessing**: StandardScaler
- **Output**: Cluster prediction (User segment)

---

## ⚙️ Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/praveena-vidhyaprakash/Spotify-Segmentation-App.git
   cd Spotify-Segmentation-App
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Train the model (optional):

bash
Copy
Edit
python train_model.py
Run the Flask app:

bash
Copy
Edit
python app.py
Open in browser:

arduino
Copy
Edit
http://localhost:5000
🖼️ App UI
The UI allows users to input audio feature values and get an intuitive listener group prediction:



🧠 Cluster Interpretations
Cluster	Description
0	🎤 High-energy & upbeat music lovers
1	🎧 Mellow or acoustic preferences
2	💃 Dance-oriented or rhythmic tastes

🙋‍♀️ Made By
This project was created by Praveena Vidhyaprakash as a learning project in Machine Learning and Web Development.


