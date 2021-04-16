import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import keras as keras
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from keras.layers import LSTM
import datetime as tm
from matplotlib import pyplot
import math
from scipy import signal
from sklearn.metrics import mean_squared_error
from scipy.fftpack import fft, fftshift

from tabulate import tabulate
#!pip install seaborn
import seaborn as sns

from keras import backend as K


def root_mean_squared_error(y_true, y_pred):
    return K.sqrt(K.mean(K.square(y_pred - y_true)))




def ejecutaModeloSinPrint(xTrain, yTrain, xVal, yVal, xTest, yTest):
    model = Sequential()
    model.add(LSTM(units=56, input_shape=(xTrain.shape[1], xTrain.shape[2])))
    model.add(Dense(units=1))

    model.compile(loss=root_mean_squared_error, optimizer=keras.optimizers.Adam(0.001))      #solo 1 vez

    history = model.fit(xTrain, yTrain, epochs=150, batch_size=16, validation_data=(xVal, yVal), verbose=0, shuffle=False)         #de nuevo al importar el modelo de otro paciente

    y_pred = model.predict(xTest)
    score = model.evaluate(xTest, yTest)

    # Guardar el Modelo
    model.save('path_to_my_model.h5')

    # Recrea exactamente el mismo modelo solo desde el archivo
    new_model = keras.models.load_model('path_to_my_model.h5')
    history = new_model.fit(xTrain, yTrain, epochs=150, batch_size=16, validation_data=(xVal, yVal), verbose=0,
                        shuffle=False)
    y_pred = new_model.predict(xTest)
    score = new_model.evaluate(xTest, yTest)

    return y_pred, score