#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 17:06:25 2024

@author: dcocu
"""

import pandas as pd
import numpy as np
from matplotlib import ticker   # Para agregar separador de miles
from matplotlib import rcParams # Para modificar el tipo de letra
import matplotlib.pyplot as plt # Para graficar series multiples

carpeta = 'dataset/'

df = pd.read_csv(carpeta + 'sign_mnist_train.csv')





dicc_alfabeto = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 10:'K', 11:'L', 12:'M', 13:'N', 14:'O', 15:'P', 16:'Q', 17:'R', 18:'S', 19:'T', 20:'U', 21:'V', 22:'W', 23:'X', 24:'Y'}

for label in dicc_alfabeto:
    label_to_plot = dicc_alfabeto[label]
    label_value = label
    # Filter the DataFrame for the specified label
    subset_df = df[df['label'] == label_value]

    # Exclude the 'label' column
    pixels = subset_df.drop('label', axis=1).values.flatten()

    # Number of pixels in a single image (assuming 28x28)
    num_pixels_per_image = 28 * 28

    # Number of images in the subset
    num_images = subset_df.shape[0]

    # Create x-axis values for all pixels in the subset
    x_values = np.tile(np.arange(num_pixels_per_image), num_images)
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.scatter(x_values, pixels, s=0.5, c='blue', alpha=0.5)
    plt.title(f'Scatter Plot for Grayscale Values of Label "{label_to_plot}" (Label {label_value})')
    plt.xlabel('Pixel Index within a 28x28 Image')
    plt.ylabel('Grayscale Value (0-255)')
    
    filas = list(range(0,785,28))
    
    plt.xticks(filas)
    
    plt.show()