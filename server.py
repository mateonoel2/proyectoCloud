from flask import Flask, request, jsonify
from keras.models import load_model
from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler, StandardScaler
import numpy as np

app = Flask(__name__)

@app.route('/predict_short', methods=['POST'])
def predict():
    data = request.get_json(force=True)

    spark = SparkSession.builder.appName('predict').getOrCreate()

    input_data = spark.createDataFrame(data)

    print(input_data)
    #input_data = np.array(data['day_of_week'], data['first_time'], data['total_distance'], data['first_stop'], data['target_stop'])

    #input_data.reshape(1, -1)
    
    prediction = [0]

    # Regresar la predicción como respuesta JSON
    return jsonify(prediction=prediction[0])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
