from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)


with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction_text = ""
    
    if request.method == 'POST':
        try:
            danceability = float(request.form['danceability'])
            energy = float(request.form['energy'])
            valence = float(request.form['valence'])
            tempo = float(request.form['tempo'])
            acousticness = float(request.form['acousticness'])

           
            features = np.array([[danceability, energy, valence, tempo, acousticness]])
            scaled_features = scaler.transform(features)

           
            cluster = model.predict(scaled_features)[0]

            
            cluster_labels = {
                0: "Chill Vibes Listener 🎧 - You enjoy calm, relaxing tracks perfect for unwinding.",
                1: "Energetic Partygoer 🔊 - You love high-energy, danceable music that gets the party started.",
                2: "Balanced Explorer 🎵 - You explore a variety of music with a mix of moods and tempos."
            }

           
            listener_type = cluster_labels.get(cluster, f"Cluster {cluster}")
            prediction_text = f"🎯 You are a {listener_type}"

        except ValueError:
            prediction_text = "⚠️ Please enter valid numeric values."

    return render_template('index.html', prediction_text=prediction_text)

if __name__ == '__main__':
    app.run(debug=True)

