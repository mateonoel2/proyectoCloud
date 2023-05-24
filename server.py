from flask import Flask, request, jsonify
import numpy as np
from keras.models import load_model
import pickle

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():

    data = request.get_json(force=True)
    
    try:
        # Cargar el modelo de red neuronal
        features = np.array([[data['day_of_week'], data['first_time'], data['total_distance'], data['first_stop'], data['target_stop']]])

        # Load scaler
        with open('models/rnn_scaler.pkl', 'rb') as file:
            scaler = pickle.load(file)
        scaled_features = scaler.transform(features)

        scaled_features = np.reshape(scaled_features, (scaled_features.shape[0], 1, scaled_features.shape[1]))
        scaled_features = [scaled_features]

        print(scaled_features)
        model = load_model('models/RNN_90.h5')
        prediction = model.predict(scaled_features)

        return jsonify(prediction=prediction.tolist())
    
    except Exception as e:
        return jsonify(error=str(e))
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
