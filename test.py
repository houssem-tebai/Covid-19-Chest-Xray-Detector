import tensorflow as tf
import numpy as np
import json
import requests

SIZE=320
MODEL_URI='http://52.170.7.78:8502/v1/models/xray:predict'
CLASSES = ['might have COVID-19', 'doesn''t have COVID-19']

# bla bla bla
def get_prediction(image_path):
    image = tf.keras.preprocessing.image.load_img(
        image_path, target_size=(SIZE, SIZE, 3)
    )
    image = tf.keras.preprocessing.image.img_to_array(image)
    #    image = tf.keras.applications.mobilenet_v2.preprocess_input(image)
    image = np.expand_dims(image, axis=0)

    data = json.dumps({
        'instances':image.tolist()
    })
    response = requests.post(MODEL_URI, data=data.encode())
    result = json.loads(response.text)
    prediction = np.squeeze(result['predictions'][0])
    #class_name = CLASSES[int(prediction > 0.5)]
    if (prediction != 1.0):
        class_name=CLASSES[0]
    else:
        class_name=CLASSES[1]
    print(prediction)
    return class_name
