import json
import pandas as pd
import numpy as np
import cv2
from PIL import Image
import keras
from keras import backend as k
from keras.models import Sequential
from keras.models import load_model
from keras.preprocessing.image import img_to_array
from flask import request
from flask import Flask
from keras.models import model_from_json
import os
from tensorflow import keras
import subprocess



#def get_model():

with open ('Model_0.97_150x150.json','r+') as f:
    model_json = json.load(f)
model = keras.models.model_from_json(model_json)
model.load_weights('Model_0.97_150x150.h5')


def preprocess_image(path):
    im = cv2.imread(path)
    im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    img = cv2.resize(im,(150,150))
    print(img.shape)
    img = np.array(img)
    print(img.shape)
    img = np.expand_dims(img,axis=0)
    print(img.shape)
    return img


def get_prediction(path):
    prediction = model.predict(preprocess_image(path))[0]
    subprocess.call(['speech-dispatcher'])  
    clases = ['Fire', 'Neutral']
    for i, p in enumerate(prediction):
        if p > 0.5:
            dicc =  {
                "classes":clases,
                "prediction": {
                    "label":clases[i],
                    "prob": str(p)}}
            if 'Fire' in clases:
                subprocess.call(['spd-say', '"BE CAREFUL, FIRE!"'])
    return dicc if clases == 'Neutral' else dicc

    
