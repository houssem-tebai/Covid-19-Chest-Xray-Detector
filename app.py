from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap

import os
import test
app = Flask(__name__)
Bootstrap(app)

"""
Routes
"""
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            image_path = os.path.join('static', uploaded_file.filename)
            uploaded_file.save(image_path)
            class_name = test.get_prediction(image_path)
            print('CLASS NAME = ', class_name)
            result = {
                'class_name': class_name,
                'image_path': image_path,
            }
            return render_template('show.html', result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')


# tensorflow/serving docker command
#sudo docker run -p 8502:8501 --name=pets -v "/home/rhyme/Desktop/app/pets/:/models/pets/1" -e MODEL_NAME=pets tensorflow/serving

#sudo docker run -p 8502:8501 --name=pets -v "/home/merihen/Covid-19-Chest-Xray-Detector/pets/:/models/pets/1" -e MODEL_NAME=pets tensorflow/serving


# docker run -p 8502:8501 --name=pets -v "/home/merihen/xray_model/1:/models/xray_model/1" -e MODEL_NAME=xray_model tensorflow/serving
