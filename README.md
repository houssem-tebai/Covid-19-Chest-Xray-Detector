# Covid-19-Chest-Xray-Detector

## disclamer: this is just a litle school project, please do not claim diagnostic performance of a model without a clinical study!

# what is this
This project is a CNN (Convolutional Neural Network) that was trained to detect the presence of Covid-19 in an Xray chest image.
With a simple Flask application that serves as the frontend of the project.

The Dataset is a combination of [COVID-19 image data collection](https://github.com/ieee8023/covid-chestxray-dataset "dataset") and [Kaggle's pneumonia dataset](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia "kaggle dataset")

# How to use this
For the impatient pros, You just need to clone the repo, download the SavedModel from [here](https://drive.google.com/drive/folders/1Ehll-vh58qF-o6bXQERe9XOqt05K1mvJ?usp=sharing)
Copy the SavedModel to tensorflow/serving docker container using this command
```
docker run -p 8502:8501 --name=xray -v "the/path/to/the/downloaded/model:/models/xray_model/1" -e MODEL_NAME=xray_model tensorflow/serving
```
install the dependencies.
```
pip install --no-cache-dir -r requirements.txt
```
Then just run __app.py__ , and voila !! you should be able to see the interface on localhost:5000
