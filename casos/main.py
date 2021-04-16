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


from casos.configuration.config import bloque_parametros, definir_configuracion
from casos.glucose_acceleration.glucose_acceleration import bloque_glucosa_aceleracion
#from casos.glucose_acceleration.glucose import
from casos.insulin.insulin import bloque_insulina, bloque_insulina_2
from casos.food.food import bloque_comida



from casos.execution.execution import bloque_ejecucion
from casos.execution.mean_score import media_resultados_pacientes



print("MAIN: BLOQUE CONFIGURACIÓN...")
path_project, path_glucose_acceleration_graphs, path_insulin_graphs, path_food_graphs, path_dataset, path_glucose_dataset, path_acceleration_dataset, path_insulin_dataset, path_food_dataset, path_dataset_processed, path_acceleration_dataset_processed, path_insulin_dataset_processed,  path_gai_dataset_processed, path_food_dataset_processed, path_full_dataset_processed, path_scores_dataset_processed, cn, en, tn, ph, pn, pi, st, a, fw, execution_number, posicion_glucosa, paciente_uno, pacientes_all, patient_digit, pacientes = bloque_parametros()
print("MAIN: BLOQUE GLUCOSA Y ACELERACIÓN...")
#bloque_glucosa_aceleracion(cn, patient_id, path_glucose_acceleration_graphs, path_glucose_dataset, pacientes)
print("MAIN: BLOQUE INSULINA...")
#signal_insulina_rapida, signal_insulina_lenta, ejemploInsulinaLispro, path_grafica_insulina_regular, lispro_insulin, regular_insulin, NPH_insulin = bloque_insulina(cn, pi, path_insulin_graphs, path_insulin_dataset)
#bloque_insulina_2(cn, patient_id, signal_insulina_rapida, signal_insulina_lenta, ejemploInsulinaLispro, path_grafica_insulina_regular, lispro_insulin, regular_insulin, NPH_insulin)
print("MAIN: BLOQUE COMIDA...")
#bloque_comida(cn, pi, patient_digit, path_food_graphs, path_food_dataset, path_gai_dataset_processed, path_food_dataset_processed, path_full_dataset_processed, posicion_glucosa, pacientes)
print("MAIN: BLOQUE EJECUCIÓN...")
#bloque_ejecucion(cn, pi, path_full_dataset_processed, path_scores_dataset_processed, execution_number, pacientes, posicion_glucosa)
print("MAIN: MEDIA DE RESULTADOS DE VARIOS PACIENTES...")
media_resultados_pacientes(path_scores_dataset_processed, pacientes)


