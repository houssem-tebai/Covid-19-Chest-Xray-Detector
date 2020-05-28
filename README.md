# Covid-19-Chest-Xray-Detector

## disclamer: this is just a litle school project, please do not claim diagnostic performance of a model without a clinical study!

# what is this
This project is a CNN (Convolutional Neural Network) that was trained to detect the presence of Covid-19 in an Xray chest image.
With a simple Flask application that serves as the frontend of the project.

The Dataset is a combination of [COVID-19 image data collection](https://github.com/ieee8023/covid-chestxray-dataset "dataset") and [Kaggle's pneumonia dataset](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia "kaggle dataset")

# How to use this

__For the impatient pros__, You just need to clone the repo, download the SavedModel from [here](https://drive.google.com/drive/folders/1Ehll-vh58qF-o6bXQERe9XOqt05K1mvJ?usp=sharing)
Copy the SavedModel to tensorflow/serving docker container using this command
```
sudo docker run -p 8502:8501 \
      --name=xray \
      -v "the/path/to/the/downloaded/model:/models/xray_model/1" \ 
      -e MODEL_NAME=xray_model \
      tensorflow/serving
```
install the dependencies.
```
pip install --no-cache-dir -r requirements.txt
```
Then just run __app.py__ , and voila !! you should be able to see the interface on http://localhost:5000

You can also use a pre-build docker image to run this project, 
### Note that the docker images are a bit large in size and may take some time to download depends on your internet speed

Download the model and run the tensorflow/serving container as mentioned above, and the run this command to launch the project in a pre-build docker image
```
sudo docker run --name xray \ 
        -p 8080:5000 \
        houssemtebai/cov-19-xray:local
```
Now you should see the app on http://localhost:8080

## Step by step quick start

### Pre-Requirement
Before we start lets download all the needed tools.

* [python 3.5 and above:](https://www.python.org/downloads/) 

* [pip:](https://pypi.org/project/pip/)

    you can skip downloading python and pip if you want to run the project inside of a docker container

* [git:](https://git-scm.com/)

* docker:

    if you're on windows or mac just download [docker desktop](https://www.docker.com/products/docker-desktop)

    on Ubuntu
```
apt update
apt install docker.io
```

Now that we got all the tools needed, lets get started 

1. first things first, clone the repo on your machine
```
git clone https://github.com/houssem-tebai/Covid-19-Chest-Xray-Detector.git
cd Covid-19-Chest-Xray-Detector
```

2. Then, download the [SavedModel](https://drive.google.com/drive/folders/1Ehll-vh58qF-o6bXQERe9XOqt05K1mvJ?usp=sharing) (or you can compile the model from model.ipynb and get your own SavedModel). 
  as the name suggest, the SavedModel is just our trained CNN saved in a format called "SavedModel" ready to be sent to tensorflow/serving to be used as a REST api, that recieves Xray-images, and return a result.
  we will be using the tensorflow/serving's docker image, and run our model inside it

3. Copy the SavedModel into tensorflow/serving container
```
sudo docker run -p 8502:8501 \
      --name=xray \
      -v "the/path/to/the/downloaded/model:/models/xray_model/1" \ 
      -e MODEL_NAME=xray_model \
      tensorflow/serving
```
  running this command for the first time may take some time.
  
  now you have a REST api serving at http://localhost:8502/v1/models/xray_model:predict and in its backend lives our model, next step is   to run our frontend app to be able to send images and recieves prediction from this Web-Service

4. Now we just need to run app.py, and we have two options here.
       
  * run it with your IDE of choice or from the command line
  but before we do that we need to install some python dependencies to run the code without any errors
  to do that, just run this command inside the application directory
  ```
  pip install --no-cache-dir -r requirements.txt
  ```
  after installing the requirements you should be able to run app.py
  to know if everything went well, you should get this message on your terminal.
  ```
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
  ```
  * run the app inside a docker container
  here, we need to build a docker image that contains all the necessery packages and file to run the code, to do so, just rub this command.
  ```
  sudo docker build -t "give the image a name" .
  ```
  after the build is complete just run a container instance from the image we just created
  ```
  sudo docker run --name xray-app -p 5000:5000 "the name of the image you created"
  ```

Finally check your browser at http://localhost:5000 and you should see the interface,
post an X-ray image you should get your result
