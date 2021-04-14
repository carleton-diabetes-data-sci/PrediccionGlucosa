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


print("MAIN: BLOQUE CONFIGURACIÓN...")
path_project, path_glucose_acceleration_graphs, path_insulin_graphs, path_food_graphs, path_dataset, path_glucose_dataset, path_acceleration_dataset, path_insulin_dataset, path_food_dataset, path_dataset_processed, path_acceleration_dataset_processed, path_insulin_dataset_processed,  path_gai_dataset_processed, path_food_dataset_processed, path_full_dataset_processed, path_scores_dataset_processed, cn, en, tn, ph, pn, pi, st, a, fw, execution_number, posicion_glucosa, paciente_uno, pacientes_all, patient_digit, pacientes = bloque_parametros()
print("MAIN: BLOQUE GLUCOSA Y ACELERACIÓN...")
#bloque_glucosa_aceleracion(cn, patient_id, path_glucose_acceleration_graphs, path_glucose_dataset, pacientes)
print("MAIN: BLOQUE INSULINA...")
#signal_insulina_rapida, signal_insulina_lenta, ejemploInsulinaLispro, path_grafica_insulina_regular, lispro_insulin, regular_insulin, NPH_insulin = bloque_insulina(cn, pi, path_insulin_graphs, path_insulin_dataset)
#bloque_insulina_2(cn, patient_id, signal_insulina_rapida, signal_insulina_lenta, ejemploInsulinaLispro, path_grafica_insulina_regular, lispro_insulin, regular_insulin, NPH_insulin)
print("MAIN: BLOQUE COMIDA...")
bloque_comida(cn, pi, patient_digit, path_food_graphs, path_food_dataset, path_gai_dataset_processed, path_food_dataset_processed, path_full_dataset_processed, posicion_glucosa, pacientes)

"""
print("MAIN: BLOQUE EJECUCIÓN...")
#execution_number = 1
scores_exp_1 = []
scores_exp_2 = []
scores_exp_3 = []
scores_exp_4 = []
scores_exp_5 = []
scores_exp_6 = []
scores_exp_7 = []
listaScores = []

for x in range(execution_number):
    print('EJECUCION: ', x)
    r, root, pacientes, pacientes_all, posicion_glucosa = definir_configuracion()
    x, y = bloque_matriz(root, pacientes)
    xTrain, xVal, xTest, yTrain, yVal, yTest = separar_x_y(x, y)
    xTrain_glucose, xTrain_Accel, xTrain_DeltaInsulin, xTrain_Insulin, xTrain_Insulin_lispro, xTrain_Insulin_lispro_regular, xTrain_Insulin_profiles, xTrain_Insulin_exp, xTrain_Insulin_comidasDeltas, xTrain_Insulin_comidasDeltas_profiles, xTrain_Insulin_comidasExp, xTrain_Insulin_comidasExp_lispro, xTrain_Insulin_comidasExp_profiles, xVal_glucose, xVal_Accel, xVal_DeltaInsulin, xVal_Insulin, xVal_Insulin_lispro, xVal_Insulin_lispro_regular, xVal_Insulin_profiles, xVal_Insulin_exp, xVal_Insulin_comidasDeltas, xVal_Insulin_comidasDeltas_profiles, xVal_Insulin_comidasExp, xVal_Insulin_comidasExp_lispro, xVal_Insulin_comidasExp_profiles, xTest_glucose, xTest_Accel, xTest_DeltaInsulin, xTest_Insulin, xTest_Insulin_lispro, xTest_Insulin_lispro_regular, xTest_Insulin_profiles, xTest_Insulin_exp, xTest_Insulin_comidasDeltas, xTest_Insulin_comidasDeltas_profiles, xTest_Insulin_comidasExp, xTest_Insulin_comidasExp_lispro, xTest_Insulin_comidasExp_profiles = bloque_dividir_datos(
        xTrain, xVal, xTest)

    y_pred_exp_1, score_exp_1 = ejecutaModeloSinPrint(xTrain_DeltaInsulin, yTrain, xVal_DeltaInsulin, yVal,
                                                      xTest_DeltaInsulin, yTest)
    y_pred_exp_2, score_exp_2 = ejecutaModeloSinPrint(xTrain_Insulin, yTrain, xVal_Insulin, yVal, xTest_Insulin, yTest)
    y_pred_exp_3, score_exp_3 = ejecutaModeloSinPrint(xTrain_Insulin_lispro, yTrain, xVal_Insulin_lispro, yVal,
                                                      xTest_Insulin_lispro, yTest)
    y_pred_exp_4, score_exp_4 = ejecutaModeloSinPrint(xTrain_Insulin_comidasDeltas, yTrain, xVal_Insulin_comidasDeltas,
                                                      yVal, xTest_Insulin_comidasDeltas, yTest)
    y_pred_exp_5, score_exp_5 = ejecutaModeloSinPrint(xTrain_Insulin_comidasExp, yTrain, xVal_Insulin_comidasExp, yVal,
                                                      xTest_Insulin_comidasExp, yTest)
    y_pred_exp_6, score_exp_6 = ejecutaModeloSinPrint(xTrain_Insulin_comidasExp_lispro, yTrain,
                                                      xVal_Insulin_comidasExp_lispro, yVal,
                                                      xTest_Insulin_comidasExp_lispro, yTest)
    y_pred_exp_7, score_exp_7 = ejecutaModeloSinPrint(xTrain_Insulin_comidasExp_profiles, yTrain,
                                                      xVal_Insulin_comidasExp_profiles, yVal,
                                                      xTest_Insulin_comidasExp_profiles, yTest)

    print('score_exp_1: ', score_exp_1)
    print('score_exp_2: ', score_exp_2)
    print('score_exp_3: ', score_exp_3)
    print('score_exp_4: ', score_exp_4)
    print('score_exp_5: ', score_exp_5)
    print('score_exp_6: ', score_exp_6)
    print('score_exp_7: ', score_exp_7)

    scores_exp_1.append(score_exp_1)
    scores_exp_2.append(score_exp_2)
    scores_exp_3.append(score_exp_3)
    scores_exp_4.append(score_exp_4)
    scores_exp_5.append(score_exp_5)
    scores_exp_6.append(score_exp_6)
    scores_exp_7.append(score_exp_7)

    listaScores.append([score_exp_1, score_exp_2, score_exp_3, score_exp_4, score_exp_5, score_exp_6, score_exp_7])

print('FINAL: ')

print('scores_exp_1: ', np.mean(scores_exp_1))
print(' -  Valor mínimo: ', np.amin(scores_exp_1))
print(' - Valor máximo: ', np.amax(scores_exp_1))

print('scores_exp_2: ', np.mean(scores_exp_2))
print(' -  Valor mínimo: ', np.amin(scores_exp_2))
print(' - Valor máximo: ', np.amax(scores_exp_2))

print('scores_exp_3: ', np.mean(scores_exp_3))
print(' -  Valor mínimo: ', np.amin(scores_exp_3))
print(' - Valor máximo: ', np.amax(scores_exp_3))

print('scores_exp_4: ', np.mean(scores_exp_4))
print(' -  Valor mínimo: ', np.amin(scores_exp_4))
print(' - Valor máximo: ', np.amax(scores_exp_4))

print('scores_exp_5: ', np.mean(scores_exp_5))
print(' -  Valor mínimo: ', np.amin(scores_exp_5))
print(' - Valor máximo: ', np.amax(scores_exp_5))

print('scores_exp_6: ', np.mean(scores_exp_6))
print(' -  Valor mínimo: ', np.amin(scores_exp_6))
print(' - Valor máximo: ', np.amax(scores_exp_6))

print('scores_exp_7: ', np.mean(scores_exp_7))
print(' -  Valor mínimo: ', np.amin(scores_exp_7))
print(' - Valor máximo: ', np.amax(scores_exp_7))

listaScores.append(
    [np.mean(score_exp_1), np.mean(score_exp_2), np.mean(score_exp_3), np.mean(score_exp_4), np.mean(score_exp_5),
     np.mean(score_exp_6), np.mean(score_exp_7)])
listaScores.append(
    [np.amin(score_exp_1), np.amin(score_exp_2), np.amin(score_exp_3), np.amin(score_exp_4), np.amin(score_exp_5),
     np.amin(score_exp_6), np.amin(score_exp_7)])
listaScores.append(
    [np.amax(score_exp_1), np.amax(score_exp_2), np.amax(score_exp_3), np.amax(score_exp_4), np.amax(score_exp_5),
     np.amax(score_exp_6), np.amax(score_exp_7)])

df = pd.DataFrame(np.array(listaScores),
                  columns=['score_exp_1', 'score_exp_2', 'score_exp_3', 'score_exp_4', 'score_exp_5', 'score_exp_6',
                           'score_exp_7'])

df.to_csv(root + '/scores.csv', index=False)

"""