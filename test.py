import tensorflow as tf
import numpy as np
import json
import requests

SIZE=128
MODEL_URI='http://52.170.84.148:8502/v1/models/xray:predict'
CLASSES = ['might have COVID-19', 'doesn''t have COVID-19']

def get_prediction(image_path):
    image = tf.keras.preprocessing.image.load_img(
        image_path, target_size=(SIZE, SIZE)
    )
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = tf.keras.applications.mobilenet_v2.preprocess_input(image)
    image = np.expand_dims(image, axis=0)

    data = json.dumps({
        'instances':image.tolist()
    })
    response = requests.post(MODEL_URI, data=data.encode())
    result = json.loads(response.text)
    prediction = np.squeeze(result['predictions'][0])
    class_name = CLASSES[int(prediction > 0.5)]
    print(prediction)
    return class_name
