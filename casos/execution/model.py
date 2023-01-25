import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import LSTM
import datetime as tm
from matplotlib import pyplot
import math
from scipy import signal
from sklearn.metrics import mean_squared_error
from scipy.fftpack import fft, fftshift

from tabulate import tabulate
#!pip install seaborn
import seaborn as sns

from tensorflow.keras import backend as K

import tensorflow.keras.utils
from importlib import reload
reload(tensorflow.keras.utils)



import pydot as pyd
from IPython.display import SVG
from tensorflow.keras.utils import model_to_dot

tensorflow.keras.utils.pydot = pyd

import tensorflow.keras
import pydot
import pydotplus
from pydotplus import graphviz
# from tensorflow.keras.utils.vis_utils import pydot
from tensorflow.keras.utils import plot_model






def root_mean_squared_error(y_true, y_pred):
    return K.sqrt(K.mean(K.square(y_pred - y_true)))

def loss_max(y_true, y_pred):
    from tensorflow.keras import backend as K
    return K.max(K.abs(y_pred - y_true), axis=-1)



def guardar_modelo(units, epochs, batch_size, adam_opt, path_models_saved, cn, paciente, exe, try_number,  xTrain, yTrain, xVal, yVal, xTest, yTest):
    print("-MODEL: SAVE MODEL OF A TRY AND PATIENT")
    model = Sequential()
    model.add(LSTM(units=units, input_shape=(xTrain.shape[1], xTrain.shape[2])))
    model.add(Dense(units=1))
    plot_model(model, to_file='model_plot.png', show_shapes=True, show_layer_names=False)
    model.compile(loss=root_mean_squared_error, optimizer=tensorflow.keras.optimizers.Adam(adam_opt))      #solo 1 vez

    history = model.fit(xTrain, yTrain, epochs=epochs, batch_size=batch_size, validation_data=(xVal, yVal), verbose=0, shuffle=False)         #de nuevo al importar el modelo de otro paciente
    model.summary()
    ###y_pred = model.predict(xTest)
    ###score = model.evaluate(xTest, yTest)

    # Guardar el Modelo
    """if caso 1, si no pacientes cambia"""
    path = path_models_saved + '/Caso_' + str(cn) + '//00' + str(paciente)  + '/case_' + str(cn) + '_patient_' + str(paciente) + '_trynumber_' + str(try_number) + '_execution_' + str(exe) + '_model'
    model.save(path, save_format='tf')
    #return y_pred, score

def cargar_modelo(units, epochs, batch_size, adam_opt, path_models_saved, cn, paciente, exe, try_number,  xTrain, yTrain, xVal, yVal, xTest, yTest):
    print("-MODEL: LOAD MODEL OF A TRY AND PATIENT")
    # Recrea exactamente el mismo modelo solo desde el archivo
    #exe=0  #use the first created model instead of a new one each execution
    path = path_models_saved + '/Caso_' + str(cn) + '//00' + str(paciente)  + '/case_' + str(cn) + '_patient_' + str(paciente) + '_trynumber_' + str(try_number) + '_execution_' + str(exe) + '_model'
    new_model = tensorflow.models.load_model(path, custom_objects={'root_mean_squared_error': root_mean_squared_error})
    history = new_model.fit(xTrain, yTrain, epochs=epochs, batch_size=batch_size, validation_data=(xVal, yVal), verbose=0, shuffle=False)
    y_pred = new_model.predict(xTest)
    score = new_model.evaluate(xTest, yTest)
    return y_pred, score


