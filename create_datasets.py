import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import os
import cv2
from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen
import requests
from zipfile import ZipFile

def create_dirs():
    '''
    create directories
    '''

    # check if datasets dir exist
    dir_path = 'datasets'
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

    # create a directory for raw data
    dirs_type = ['raw']
    labels = [0,1]

    for dir_type in dirs_type:

        dir_path = 'datasets/{}_data'.format(dir_type)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)

        for label in labels:
            dir_path = 'datasets/{}_data/{}'.format(dir_type,label)
            if not os.path.exists(dir_path):
                os.mkdir(dir_path)

def get_chai_raw_data():
    '''
    get chai images from github
    '''

    # download zipfile fro, url
    url = 'https://github.com/yehonatanshavit/chai_classification/blob/main/datasets/chai_dataset.zip?raw=true'

def read_jpg():
    '''
    Read jpg image, resize and save it
    '''
    # set dataset type - [0] = not chai [1] = chai
    labels = [0, 1]
    for label in labels:
        path = 'datasets/raw_data/{}'.format(label)
        images = os.listdir(path)
        for image in images:
            image_arr = cv2.cvtColor(cv2.imread('{}/{}'.format(path,image)),cv2.COLOR_BGR2RGB)
            image_arr = cv2.resize(image_arr,(100,100),interpolation = cv2.INTER_AREA)

create_dirs()
get_chai_raw_data()