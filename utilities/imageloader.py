
from tensorflow.keras.preprocessing import image

from utilities import IMG_WIDTH, IMG_HEIGHT

from pathlib import Path 
from PIL import Image 

import numpy as np 

def loadImages(folder):
  '''
  Iterate over all the images in the folder and convert them to numpy arrays 
  with format channels_last incase a number of images in a single folder need to be 
  evaluated or predicted.
  '''
  current_directory = Path.cwd()
  image_directory = current_directory.joinpath(folder)
  images = []
    
  for filename in image_directory.iterdir():
    
    #Load the images into PIL format
    img = image.load_img(filename, target_size=(IMG_HEIGHT, IMG_WIDTH))
    #Convert the PIL image to a numpy array
    img = image.img_to_array(img) / 255
    images.append(img)
    
  return np.array(images)

def loadSingleImage(filename):
    '''
    Change the image file to a numpy array for prediction or evaluation
    returns rescaled version of the image in the range [0, 1]

    '''
    # ...
    # ... incomplete
    # ...
    img = image.load_img(filename, target_size=(IMG_HEIGHT, IMG_WIDTH))
    img = image.img_to_array(img) / 255

    return img

