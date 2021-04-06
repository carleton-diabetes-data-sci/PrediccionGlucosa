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
# !pip install seaborn
import seaborn as sns
# %matplotlib inline

from configuration.paths import define_paths
from configuration.variables import parser_variables


def definir_configuracion():
  print("Definir los path...")
  r, root = define_paths()
  print("r:", r, "root:", root)

  print("Definir el caso de investigación con sus parámetros")
  cn, en, tn, ph, pn, pi, st, a, fw = parser_variables()
  print("cn:", cn, "en:", en, "tn:", tn, "ph:", ph, "pn:", pn, "pi:", pi, "st:", st, "a:", a, "fw:", fw)

  execution_number = en    #1 or 10
  #execution_number = 1

  posicion_glucosa = ph  #12 or 6
  #posicion_glucosa = 6
  #posicion_glucosa = 12

  #patient_id = pi
  patient_id = 1
  pacientes_all = ['001', '002', '003', '004', '005', '006', '007', '008', '009']
  if (patient_id==0):
    print(patient_id)
    pacientes_relevantes = ['001', '002', '004', '006', '007', '008']    #El 5 no tiene horas de las comidas. El 3 y 9 tienen muy pocos datos de aceleración
    pacientes = pacientes_relevantes

  else:
    patientid = "['00" + patient_id + "']"
    print(patientid)
    paciente_unico = patientid


  pacientes_relevantes = ['001', '002', '004','006','007','008']
  pacientes = pacientes_relevantes
  paciente_uno = ['001']


  # El primer valor es la edad, el segundo el género, el tercero la altura y el último el peso
  caracteristica_pacientes = {'001': ['NA', 'Man', '180–189', '80–89'], '002': ['20–29', 'Man', '170–179', '60–69'],
                              '003': ['20–29', 'Man', '180–189', '70–79'], '004': ['20–29', 'Man', '180–189', '80–89'],
                              '005': ['30–39', 'Man', '180–189', '80–89'], '006': ['30–39', 'Man', '190–199', '70–79'],
                              '007': ['30–39', 'Woman', '160–169', '70–79'], '008': ['60–69', 'Woman', '150–159', '50–59'],
                              '009': ['70–79', 'Woman', '160–169', '50–59']}





  return r, root, pacientes, pacientes_all, posicion_glucosa



def bloque_parametros():
  print("PARÁMETROS DE CONFIGURACION")
  r, root, pacientes, pacientes_all, posicion_glucosa = definir_configuracion()
  return r, root, pacientes, pacientes_all, posicion_glucosa
