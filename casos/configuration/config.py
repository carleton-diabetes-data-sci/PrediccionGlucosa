

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

from casos.configuration.paths import define_paths
from casos.configuration.variables import parser_variables
from casos.configuration.model import define_model_hiperparameters


def definir_configuracion():
  print("-Definir los path...")
  path_project,  path_glucose_acceleration_graphs, path_insulin_graphs, path_food_graphs, path_dataset, path_glucose_dataset, path_acceleration_dataset, path_insulin_dataset, path_food_dataset, path_dataset_processed, path_acceleration_dataset_processed, path_insulin_dataset_processed,  path_gai_dataset_processed, path_food_dataset_processed, path_full_dataset_processed, path_scores_dataset_processed, path_models_saved = define_paths()
  print("path_project: ", path_project,  "path_glucose_acceleration_graphs: ", path_glucose_acceleration_graphs, "path_insulin_graphs: ", path_insulin_graphs, "path_food_graphs: ", path_food_graphs, "path_dataset: ", path_dataset, "path_glucose_dataset: ", path_glucose_dataset, "path_acceleration_dataset: ", path_acceleration_dataset, "path_insulin_dataset: ", path_insulin_dataset, "path_food_dataset: ",  path_food_dataset)

  print("-Definir los hiperparámetros del modelo LSTM")
  units, epochs, batch_size, adam_opt = define_model_hiperparameters()

  print("-Definir el caso de investigación con sus parámetros")
  cn, en, tn, ph, pn, pi, st, a, fw = parser_variables()
  print("cn:", cn, "en:", en, "tn:", tn, "ph:", ph, "pn:", pn, "pi:", pi, "st:", st, "a:", a, "fw:", fw)

  execution_number = en    #1 or 10
  #execution_number = 1

  posicion_glucosa = ph  #12 or 6
  #posicion_glucosa = 6
  #posicion_glucosa = 12

  paciente_uno = ['001']
  pacientes_all = ['001', '002', '003', '004', '005', '006', '007', '008', '009']


  if (pi==0):
    patient_digit = 1
    print(patient_digit)
    pacientes_relevantes = ['001', '002', '004', '006', '007', '008']    #El 5 no tiene horas de las comidas. El 3 y 9 tienen muy pocos datos de aceleración
    pacientes_id= pacientes_relevantes
    pacientes  = [1, 2, 4, 6, 7, 8]               #así en food_add

  if (pi==-1):
    patient_digit = 1
    pacientes = [1, 2, 4, 6, 7, 8]

  else:
    patient_digit = pi
    pacientes_id = "['00" + str(patient_digit) + "']"          #pacientes_id es ['00x']
    pacientes = [patient_digit]                #así en food_add
    print(pacientes)



  # El primer valor es la edad, el segundo el género, el tercero la altura y el último el peso
  caracteristica_pacientes = {'001': ['NA', 'Man', '180–189', '80–89'], '002': ['20–29', 'Man', '170–179', '60–69'],
                              '003': ['20–29', 'Man', '180–189', '70–79'], '004': ['20–29', 'Man', '180–189', '80–89'],
                              '005': ['30–39', 'Man', '180–189', '80–89'], '006': ['30–39', 'Man', '190–199', '70–79'],
                              '007': ['30–39', 'Woman', '160–169', '70–79'], '008': ['60–69', 'Woman', '150–159', '50–59'],
                              '009': ['70–79', 'Woman', '160–169', '50–59']}



  return path_project, path_glucose_acceleration_graphs, path_insulin_graphs, path_food_graphs, path_dataset, path_glucose_dataset, path_acceleration_dataset, path_insulin_dataset, path_food_dataset, path_dataset_processed, path_acceleration_dataset_processed, path_insulin_dataset_processed,  path_gai_dataset_processed, path_food_dataset_processed, path_full_dataset_processed, path_scores_dataset_processed, path_models_saved, units, epochs, batch_size, adam_opt, cn, en, tn, ph, pn, pi, st, a, fw, execution_number, posicion_glucosa, paciente_uno, pacientes_all, patient_digit, pacientes



def bloque_parametros():
  print("-CONFIG: DEFINIR PARÁMETROS DE CONFIGURACION")
  path_project, path_glucose_acceleration_graphs, path_insulin_graphs, path_food_graphs, path_dataset, path_glucose_dataset, path_acceleration_dataset, path_insulin_dataset, path_food_dataset, path_dataset_processed, path_acceleration_dataset_processed, path_insulin_dataset_processed,  path_gai_dataset_processed, path_food_dataset_processed, path_full_dataset_processed, path_scores_dataset_processed, path_models_saved, units, epochs, batch_size, adam_opt, cn, en, tn, ph, pn, pi, st, a, fw, execution_number, posicion_glucosa, paciente_uno, pacientes_all, patient_digit, pacientes = definir_configuracion()
  return path_project, path_glucose_acceleration_graphs, path_insulin_graphs, path_food_graphs, path_dataset, path_glucose_dataset, path_acceleration_dataset, path_insulin_dataset, path_food_dataset, path_dataset_processed, path_acceleration_dataset_processed, path_insulin_dataset_processed,  path_gai_dataset_processed, path_food_dataset_processed, path_full_dataset_processed, path_scores_dataset_processed, path_models_saved, units, epochs, batch_size, adam_opt, cn, en, tn, ph, pn, pi, st, a, fw, execution_number, posicion_glucosa, paciente_uno, pacientes_all, patient_digit, pacientes

