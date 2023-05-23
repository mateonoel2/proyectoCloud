from flask import Flask, request, jsonify
from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
import numpy as np
from keras.models import load_model

app = Flask(__name__)

def is_short(input_data):
    return 'TODO'

@app.route('/predict', methods=['POST'])
def predict():

    data = request.get_json(force=True)
    
    try:
    
        input_data = np.array([[data['day_of_week'], data['first_time'], data['total_distance'], data['first_stop'], data['target_stop']]])

        if(is_short(input_data)):
            # Cargar el modelo de regresión lineal

            spark = SparkSession.builder.appName('predict_short').getOrCreate()

            input_data = spark.createDataFrame(input_data)
            
            assembler = VectorAssembler(inputCols=input_data.columns, outputCol="features_a")
            features = assembler.transform(input_data)

            scaler = spark.read('trained_models/linearScaler').load('scaler')
            scaled_features = scaler.transform(features)
            
            model = spark.read('trained_models/linearRegression').load('model')
            prediction = model.transform(scaled_features)

            return jsonify(prediction=prediction[0])
        
        else:
            # Cargar el modelo de red neuronal
            features = np.array([[data['day_of_week'], data['first_time'], data['total_distance'], data['first_stop'], data['target_stop']]])

            scaler = load_model('/trained_models/RNNScaler')
            scaled_features = scaler.transform(features)
            
            model = load_model('/trained_models/RNN_40.h5')
            prediction = model.predict(scaled_features)

            return jsonify(prediction=prediction[0])
    
    except Exception as e:
        return jsonify(error=str(e))
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
