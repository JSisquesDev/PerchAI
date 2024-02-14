import os
import tensorflow as tf
import matplotlib as plt
from matplotlib import pyplot
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import tensorflow.keras as kr
import random

from dotenv import find_dotenv, load_dotenv
from tensorflow.keras.utils import load_img, img_to_array
from numpy.core.defchararray import array
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import load_model

def show_image(path, title = ""):
  photo = mpimg.imread(path)
  plt.imshow(photo)
  plt.title(title)
  plt.show()

if __name__ == '__main__':
    # Cargamos las variables de entorno
    load_dotenv(find_dotenv())
    
    # Establecemos el tamaño de las imágenes
    IMG_WIDTH = int(os.getenv("IMG_WIDTH"))
    IMG_HEIGHT = int(os.getenv("IMG_HEIGHT"))
    IMG_DEEP = int(os.getenv("IMG_DEEP"))
    
    PROJECT_PATH = os.getenv("PROJECT_PATH")
    MODEL_PATH = os.path.join(PROJECT_PATH, os.getenv("MODEL_PATH"))
    MODEL_NAME = os.path.join(MODEL_PATH, os.getenv("MODEL_NAME"))
        
    if os.path.exists(MODEL_NAME):
        model = load_model(MODEL_NAME)
        print("Modelo previo cargado")
        
        photo = "C:/Users/Javie/Documents/Proyectos/JSisquesDev/PerchAI/dataset/test/ZEBRA DOVE/3.jpg"
        
        show_image(photo)
        
        img = load_img(photo, target_size=(IMG_HEIGHT, IMG_WIDTH), color_mode="rgb")
        prediction = model.predict(np.expand_dims(img, 0))
        print(prediction)
        
    else:
        print("No se ha guardado ningún modelo previo")