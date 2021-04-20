
import pandas as pd
import numpy as np


import keras as keras
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split


from keras.layers import LSTM
from keras import backend as K


units = 56
epochs = 1
batch_size = 16
adam_opt = 0.001
cn=0
pi=-1

en = 1  # 10 or 1
tn = 7
ph = 12
pn = 1
pi = -1  # 1 or -1    #1, 2, 4, 6, 7, 8 separado
st = 0
a = 1
fw = 1
execution_number = en

paciente_uno = ['001']
pacientes_all = ['001', '002', '003', '004', '005', '006', '007', '008', '009']

if (pi == 0):
    patient_digit = 1
    print(patient_digit)
    pacientes_relevantes = ['001', '002', '004', '006', '007',
                            '008']  # El 5 no tiene horas de las comidas. El 3 y 9 tienen muy pocos datos de aceleración
    pacientes_id = pacientes_relevantes
    pacientes = [1, 2, 4, 6, 7, 8]  # así en food_add

if (pi == -1):
    patient_digit = 1
    pacientes = [1, 2, 4, 6, 7, 8]

else:
    patient_digit = pi
    pacientes_id = "['00" + str(patient_digit) + "']"  # pacientes_id es ['00x']
    pacientes = [patient_digit]  # así en food_add
    print(pacientes)
posicion_glucosa = ph


path_project = r'C:\Users\apula\PycharmProjects\PrediccionGlucosa'  # PATH

path_dataset_processed = path_project + r'\D1NAMO\processed_subset'  # PATH

path_full_dataset_processed = [
                                path_dataset_processed + r'\001\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_datos_procesados.csv',  #_ or not
                                path_dataset_processed + r'\002\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_datos_procesados.csv',
                                path_dataset_processed + r'\003\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_datos_procesados.csv',
                                path_dataset_processed + r'\004\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_datos_procesados.csv',
                                path_dataset_processed + r'\005\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_datos_procesados.csv',
                                path_dataset_processed + r'\006\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_datos_procesados.csv',
                                path_dataset_processed + r'\007\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_datos_procesados.csv',
                                path_dataset_processed + r'\008\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_datos_procesados.csv',
                                path_dataset_processed + r'\009\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_datos_procesados.csv']  # PATH
path_models_saved = path_project + r'\models'  # PATH

path_scores_dataset_processed = [
                                path_dataset_processed + r'\001\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_scores.csv',
                                path_dataset_processed + r'\002\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_scores.csv',
                                path_dataset_processed + r'\003\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_scores.csv',
                                path_dataset_processed + r'\004\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_scores.csv',
                                path_dataset_processed + r'\005\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_scores.csv',
                                path_dataset_processed + r'\006\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_scores.csv',
                                path_dataset_processed + r'\007\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_scores.csv',
                                path_dataset_processed + r'\008\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_scores.csv',
                                path_dataset_processed + r'\009\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_scores.csv',
                                path_dataset_processed + r'\Caso_' + str(cn) + '_mean_scores_relevant_patients.csv',  # PATH
                                path_dataset_processed + r'\Caso_' + str(cn) + '_min_scores_relevant_patients.csv', # PATH
                                path_dataset_processed + r'\Caso_' + str(cn) + '_max_scores_relevant_patients.csv']  # PATH






def separar_train_val_test(x ,y, paciente):
    """
    :param x:
    :param y:
    :return:

    Separamos en test y train
    Dividimos los datos en test, entrenamiento y validación para entrenar, validar y testear el modelo.

    *   Datos de entrenamiento: se utilizan para entrenar el modelo. El modelo aprenderá de estos datos.
    *   Datos de validación: se utilizan para proporcionar una evaluación imparcial del modelo de datos mientras se ajustan los hiperparámetros del modelo.
    *   Datos de test: conjunto de datos utilizados para proporcionar una evaluación imparcial del modelo final.
    """
    dimension_x_y_list=[]
    # print(x.shape)   #(2738, 24, 14)
    # print(y.shape)   #(2738,)

    xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size = 0.2, random_state = 0)
    #print('Tamaño de xTrain: ', xTrain.shape)  # (2190, 24, 14)  [[[7.40000000e+00 4.21584213e+01 0.00000000e+00 ... 0.00000000e+00   5.76909235e-02 2.60332989e+00]
    #print('Tamaño de yTrain: ', yTrain.shape)    # (2190,)            [ 3.7 11.5  4.6 ...  7.2  4.6  4.6]
    print('Tamaño de xTest: ', xTest.shape)  # (548, 24, 14)      [[[12.9        45.11801353  0.         ...  0.          0.       0.        ]
    print('Tamaño de yTest: ', yTest.shape)   # (548,)    [ 6.3  6.9  8.   4.3  ... 6.3 22.2  2.5 13.5   5.5 16.3]


    xTrain, xVal, yTrain, yVal = train_test_split(xTrain, yTrain, test_size = 0.25, random_state = 0)
    print('Tamaño de xTrain: ', xTrain.shape)     # (1642, 24, 14)
    print('Tamaño de yTrain: ', yTrain.shape)
    print('Tamaño de xVal: ', xVal.shape) # (548, 24, 14)
    print('Tamaño de yVal: ', yVal.shape)  # (548,)

    print('Tamaño de x, xTrain, xVal y xTest: ', x.shape, xTrain.shape, xVal.shape, xTest.shape)   # patient 1 Caso 0 (665, 24, 14) (399, 24, 14) (133, 24, 14) (133, 24, 14)
    #all patients Caso 1 (3516, 24, 14), (1172, 24, 14), (1172, 24, 14)

    dimension_x_y_list.append([x.shape, y.shape, xTrain.shape, yTrain.shape, xVal.shape, yVal.shape, xTest.shape, yTest.shape])
    df = pd.DataFrame(np.array(dimension_x_y_list), columns=['x', 'y', 'xTrain', 'yTrain', 'xVal', 'yVal', 'xTest', 'yTest'])

    path = path_models_saved + '\Caso_' + str(cn) + '\\00' + str(paciente)  + '\case_' + str(cn) + '_patient_' + str(paciente) + '_matrices.csv'
    df.to_csv(path, index=False)

    return xTrain, xVal, xTest, yTrain, yVal, yTest



def divideDatos(xDiv):
    #ac = 1 or 0
    ac=1
    xDiv_glucose = np.zeros(xDiv.shape[0] * xDiv.shape[1]).reshape((xDiv.shape[0], xDiv.shape[1], 1))  # change dimensions
    xDiv_Accel = np.zeros(xDiv.shape[0] * xDiv.shape[1]*(ac+1)).reshape((xDiv.shape[0], xDiv.shape[1], 1+ac))
    xDiv_DeltaInsulin = np.zeros(xDiv.shape[0] * xDiv.shape[1] * (ac+3)).reshape((xDiv.shape[0], xDiv.shape[1], 3+ac))
    xDiv_Insulin = np.zeros(xDiv.shape[0] * xDiv.shape[1] * (ac+3)).reshape((xDiv.shape[0], xDiv.shape[1], 3+ac))
    xDiv_Insulin_lispro = np.zeros(xDiv.shape[0] * xDiv.shape[1] * (ac+3)).reshape((xDiv.shape[0], xDiv.shape[1], 3+ac))
    xDiv_Insulin_lispro_regular = np.zeros(xDiv.shape[0] * xDiv.shape[1] * (ac+3)).reshape((xDiv.shape[0], xDiv.shape[1], 3+ac))
    xDiv_Insulin_profiles = np.zeros(xDiv.shape[0] * xDiv.shape[1] * (ac+3)).reshape((xDiv.shape[0], xDiv.shape[1], 3+ac))
    xDiv_Insulin_exp = np.zeros(xDiv.shape[0] * xDiv.shape[1] * (ac+3)).reshape((xDiv.shape[0], xDiv.shape[1], 3+ac))
    xDiv_Insulin_comidasDeltas = np.zeros(xDiv.shape[0] * xDiv.shape[1] * (ac+4)).reshape((xDiv.shape[0], xDiv.shape[1], 4+ac))
    xDiv_Insulin_comidasDeltas_profiles = np.zeros(xDiv.shape[0] * xDiv.shape[1] * (ac+4)).reshape((xDiv.shape[0], xDiv.shape[1], 4+ac))
    xDiv_Insulin_comidasExp = np.zeros(xDiv.shape[0] * xDiv.shape[1] * (ac+4)).reshape((xDiv.shape[0], xDiv.shape[1], 4+ac))
    xDiv_Insulin_comidasExp_lispro = np.zeros(xDiv.shape[0] * xDiv.shape[1] * (ac+4)).reshape((xDiv.shape[0], xDiv.shape[1], 4+ac))
    xDiv_Insulin_comidasExp_profiles = np.zeros(xDiv.shape[0] * xDiv.shape[1] * (ac+4)).reshape((xDiv.shape[0], xDiv.shape[1], 4+ac))

    for x in range(xDiv.shape[0]):
        for y in range(xDiv.shape[1]):

            #Glucose model
            xDiv_glucose[x][y] = xDiv[x][y][0]

            #Glucose+acceleration model
            xDiv_Accel[x][y][0] = xDiv[x][y][0]
            if(ac==1):
                xDiv_Accel[x][y][1] = xDiv[x][y][1]

            #Try 1: glucose+acceleration+2+3
            xDiv_DeltaInsulin[x][y][0] = xDiv[x][y][0]
            if(ac==1):
                xDiv_DeltaInsulin[x][y][1] = xDiv[x][y][1]
            xDiv_DeltaInsulin[x][y][ac+1] = xDiv[x][y][2]
            xDiv_DeltaInsulin[x][y][ac+2] = xDiv[x][y][3]

            #Try 2: glucose+acceleration+4+5
            xDiv_Insulin[x][y][0] = xDiv[x][y][0]
            if(ac==1):
                xDiv_Insulin[x][y][1] = xDiv[x][y][1]
            xDiv_Insulin[x][y][ac+1] = xDiv[x][y][4]
            xDiv_Insulin[x][y][ac+2] = xDiv[x][y][5]

            #Try 3: glucose+acceleration+Michaelis+exponentials
            xDiv_Insulin_lispro[x][y][0] = xDiv[x][y][0]
            if(ac==1):
                xDiv_Insulin_lispro[x][y][1] = xDiv[x][y][1]
            xDiv_Insulin_lispro[x][y][ac+1] = xDiv[x][y][5]
            xDiv_Insulin_lispro[x][y][ac+2] = xDiv[x][y][10]

            #Bad model: glucose+acceleration+11+10
            xDiv_Insulin_lispro_regular[x][y][0] = xDiv[x][y][0]
            if (ac == 1):
                xDiv_Insulin_lispro_regular[x][y][1] = xDiv[x][y][1]
            xDiv_Insulin_lispro_regular[x][y][ac+1] = xDiv[x][y][11]
            xDiv_Insulin_lispro_regular[x][y][ac+2] = xDiv[x][y][10]

            #Bad model: glucose+acceleration+12+13
            xDiv_Insulin_profiles[x][y][0] = xDiv[x][y][0]
            if(ac==1):
                xDiv_Insulin_profiles[x][y][1] = xDiv[x][y][1]
            xDiv_Insulin_profiles[x][y][ac+1] = xDiv[x][y][12]
            xDiv_Insulin_profiles[x][y][ac+2] = xDiv[x][y][13]

            #Bad model: glucose+acceleration+6+7
            xDiv_Insulin_exp[x][y][0] = xDiv[x][y][0]
            if (ac == 1):
                xDiv_Insulin_exp[x][y][1] = xDiv[x][y][1]
            xDiv_Insulin_exp[x][y][ac+1] = xDiv[x][y][6]
            xDiv_Insulin_exp[x][y][ac+2] = xDiv[x][y][7]

            #Try 4: glucose+acceleration+4+5+8
            xDiv_Insulin_comidasDeltas[x][y][0] = xDiv[x][y][0]
            if (ac == 1):
                xDiv_Insulin_comidasDeltas[x][y][1] = xDiv[x][y][1]
            xDiv_Insulin_comidasDeltas[x][y][ac+1] = xDiv[x][y][4]
            xDiv_Insulin_comidasDeltas[x][y][ac+2] = xDiv[x][y][5]
            xDiv_Insulin_comidasDeltas[x][y][ac+3] = xDiv[x][y][8]  # all in 0

            #Bad model: glucose+acceleration+12+13+8
            xDiv_Insulin_comidasDeltas_profiles[x][y][0] = xDiv[x][y][0]
            if (ac == 1):
                xDiv_Insulin_comidasDeltas_profiles[x][y][1] = xDiv[x][y][1]
            xDiv_Insulin_comidasDeltas_profiles[x][y][ac+1] = xDiv[x][y][12]
            xDiv_Insulin_comidasDeltas_profiles[x][y][ac+2] = xDiv[x][y][13]
            xDiv_Insulin_comidasDeltas_profiles[x][y][ac+3] = xDiv[x][y][8]

            #Try 5: glucose+acceleration+4+5+9
            xDiv_Insulin_comidasExp[x][y][0] = xDiv[x][y][0]
            if (ac == 1):
                xDiv_Insulin_comidasExp[x][y][1] = xDiv[x][y][1]
            xDiv_Insulin_comidasExp[x][y][ac+1] = xDiv[x][y][4]
            xDiv_Insulin_comidasExp[x][y][ac+2] = xDiv[x][y][5]
            xDiv_Insulin_comidasExp[x][y][ac+3] = xDiv[x][y][9]

            #Try 6: glucose+acceleration+5+10+9 (Menten)
            xDiv_Insulin_comidasExp_lispro[x][y][0] = xDiv[x][y][0]
            if (ac == 1):
                xDiv_Insulin_comidasExp_lispro[x][y][1] = xDiv[x][y][1]
            xDiv_Insulin_comidasExp_lispro[x][y][ac+1] = xDiv[x][y][5]
            xDiv_Insulin_comidasExp_lispro[x][y][ac+2] = xDiv[x][y][10]
            xDiv_Insulin_comidasExp_lispro[x][y][ac+3] = xDiv[x][y][9]

            # Try 7: glucose+acceleration+12+13+9 (Profiles of insulin and food)
            xDiv_Insulin_comidasExp_profiles[x][y][0] = xDiv[x][y][0]
            if (ac == 1):
                xDiv_Insulin_comidasExp_profiles[x][y][1] = xDiv[x][y][1]
            xDiv_Insulin_comidasExp_profiles[x][y][ac+1] = xDiv[x][y][12]
            xDiv_Insulin_comidasExp_profiles[x][y][ac+2] = xDiv[x][y][13]
            xDiv_Insulin_comidasExp_profiles[x][y][ac+3] = xDiv[x][y][9]

    return xDiv_glucose, xDiv_Accel, xDiv_DeltaInsulin, xDiv_Insulin, xDiv_Insulin_lispro, xDiv_Insulin_lispro_regular, xDiv_Insulin_profiles, xDiv_Insulin_exp, xDiv_Insulin_comidasDeltas, xDiv_Insulin_comidasDeltas_profiles, xDiv_Insulin_comidasExp, xDiv_Insulin_comidasExp_lispro, xDiv_Insulin_comidasExp_profiles

def bloque_dividir_datos(xTrain, xVal, xTest):
    xTrain_glucose, xTrain_Accel, xTrain_DeltaInsulin, xTrain_Insulin, xTrain_Insulin_lispro, xTrain_Insulin_lispro_regular, xTrain_Insulin_profiles, xTrain_Insulin_exp, xTrain_Insulin_comidasDeltas, xTrain_Insulin_comidasDeltas_profiles, xTrain_Insulin_comidasExp, xTrain_Insulin_comidasExp_lispro, xTrain_Insulin_comidasExp_profiles = divideDatos(xTrain)

    # print('xTrain_try_1 tiene un tamaño: ',xTrain_DeltaInsulin.shape)
    # print('xTrain_try_2 tiene un tamaño: ',xTrain_Insulin.shape)
    # print('xTrain_try_3 tiene un tamaño: ',xTrain_Insulin_lispro.shape)
    # print('xTrain_try_4 tiene un tamaño: ',xTrain_Insulin_comidasDeltas.shape)
    # print('xTrain_try_5 tiene un tamaño: ',xTrain_Insulin_comidasExp.shape)
    # print('xTrain_try_6 tiene un tamaño: ',xTrain_Insulin_comidasExp_lispro.shape)
    # print('xTrain_try_7 tiene un tamaño: ',xTrain_Insulin_comidasExp_profiles.shape)

    xVal_glucose, xVal_Accel, xVal_DeltaInsulin, xVal_Insulin, xVal_Insulin_lispro, xVal_Insulin_lispro_regular, xVal_Insulin_profiles, xVal_Insulin_exp, xVal_Insulin_comidasDeltas, xVal_Insulin_comidasDeltas_profiles, xVal_Insulin_comidasExp, xVal_Insulin_comidasExp_lispro, xVal_Insulin_comidasExp_profiles = divideDatos(xVal)

    # print('xVal_try_1 tiene un tamaño: ',xVal_DeltaInsulin.shape)
    # print('xVal_try_2 tiene un tamaño: ',xVal_Insulin.shape)
    # print('xVal_try_3 tiene un tamaño: ',xVal_Insulin_lispro.shape)
    # print('xVal_try_4 tiene un tamaño: ',xVal_Insulin_comidasDeltas.shape)
    # print('xVal_try_5 tiene un tamaño: ',xVal_Insulin_comidasExp.shape)
    # print('xVal_try_6 tiene un tamaño: ',xVal_Insulin_comidasExp_lispro.shape)
    # print('xVal_try_7 tiene un tamaño: ',xVal_Insulin_comidasExp_profiles.shape)

    xTest_glucose, xTest_Accel, xTest_DeltaInsulin, xTest_Insulin, xTest_Insulin_lispro, xTest_Insulin_lispro_regular, xTest_Insulin_profiles, xTest_Insulin_exp, xTest_Insulin_comidasDeltas, xTest_Insulin_comidasDeltas_profiles, xTest_Insulin_comidasExp, xTest_Insulin_comidasExp_lispro, xTest_Insulin_comidasExp_profiles = divideDatos(xTest)

    # print('xTest_try_1 tiene un tamaño: ',xTest_DeltaInsulin.shape)
    # print('xTest_try_2 tiene un tamaño: ',xTest_Insulin.shape)
    # print('xTest_try_3 tiene un tamaño: ',xTest_Insulin_lispro.shape)
    # print('xTest_try_4 tiene un tamaño: ',xTest_Insulin_comidasDeltas.shape)
    # print('xTest_try_5 tiene un tamaño: ',xTest_Insulin_comidasExp.shape)
    # print('xTest_try_6 tiene un tamaño: ',xTest_Insulin_comidasExp_lispro.shape)
    # print('xTest_try_7 tiene un tamaño: ',xTest_Insulin_comidasExp_profiles.shape)

    return xTrain_glucose, xTrain_Accel, xTrain_DeltaInsulin, xTrain_Insulin, xTrain_Insulin_lispro, xTrain_Insulin_lispro_regular, xTrain_Insulin_profiles, xTrain_Insulin_exp, xTrain_Insulin_comidasDeltas, xTrain_Insulin_comidasDeltas_profiles, xTrain_Insulin_comidasExp, xTrain_Insulin_comidasExp_lispro, xTrain_Insulin_comidasExp_profiles, xVal_glucose, xVal_Accel, xVal_DeltaInsulin, xVal_Insulin, xVal_Insulin_lispro, xVal_Insulin_lispro_regular, xVal_Insulin_profiles, xVal_Insulin_exp, xVal_Insulin_comidasDeltas, xVal_Insulin_comidasDeltas_profiles, xVal_Insulin_comidasExp, xVal_Insulin_comidasExp_lispro, xVal_Insulin_comidasExp_profiles, xTest_glucose, xTest_Accel, xTest_DeltaInsulin, xTest_Insulin, xTest_Insulin_lispro, xTest_Insulin_lispro_regular, xTest_Insulin_profiles, xTest_Insulin_exp, xTest_Insulin_comidasDeltas, xTest_Insulin_comidasDeltas_profiles, xTest_Insulin_comidasExp, xTest_Insulin_comidasExp_lispro, xTest_Insulin_comidasExp_profiles



def bloque_matriz(path_full_dataset_processed, paciente, posicion_glucosa, datosProcesados):
    """
    :param path_full_dataset_processed:
    :param pacientes:
    :param posicion_glucosa:
    :return:

    Damos forma a los datos
    Contruimos la matriz de entrenamiento y de test con los datos de glucosa obtenidos de un paciente.
    En base a 24 datos, el objetivo es predecir la glucosa dentro de media hora.
    A estos datos añadimos los valores de ejercicio físico

    """
    x_glucose = []
    y_glucose = []
    dimension_x_y_list = []  #to store the dimension of each try matrices
    try_1_list= []
    try_2_list = []
    try_3_list= []
    try_4_list = []
    try_5_list= []
    try_6_list = []
    try_7_list= []


    for x in range(datosProcesados.shape[0] - 24 - posicion_glucosa):

        if datosProcesados['Date'][x] == datosProcesados['Date'][x + 24 + posicion_glucosa]:

            x_muestras = []

            for y in range(24):
                # meto en un array todos mis datos
                x_muestras.append([datosProcesados['Glucose'][x + y],
                                   datosProcesados['Accel'][x + y],
                                   datosProcesados['Fast_insulin'][x + y],
                                   datosProcesados['Slow_insulin'][x + y],
                                   datosProcesados['Fast_insulin_process'][x + y],
                                   datosProcesados['Slow_insulin_process'][x + y],
                                   datosProcesados['Fast_insulin_process_exp'][x + y],
                                   datosProcesados['Slow_insulin_process_exp'][x + y],
                                   datosProcesados['Delta_calories'][x + y],
                                   datosProcesados['Calories_exp'][x + y],
                                   datosProcesados['Fast_insulin_lispro'][x + y],
                                   datosProcesados['Slow_insulin_regular'][x + y],
                                   datosProcesados['Fast_insulin_profile'][x + y],
                                   datosProcesados['Slow_insulin_profile'][x + y]])

            x_glucose.append(x_muestras)
            y_glucose.append(datosProcesados['Glucose'][x + 24 + posicion_glucosa])

    x = np.array(x_glucose)
    print('Tamaño de x: ', x.shape)

    y = np.array(y_glucose)
    print('Tamaño de y: ', y.shape)

    xTrain, xVal, xTest, yTrain, yVal, yTest = separar_train_val_test(x, y, paciente)
    xTrain_glucose, xTrain_Accel, xTrain_DeltaInsulin, xTrain_Insulin, xTrain_Insulin_lispro, xTrain_Insulin_lispro_regular, xTrain_Insulin_profiles, xTrain_Insulin_exp, xTrain_Insulin_comidasDeltas, xTrain_Insulin_comidasDeltas_profiles, xTrain_Insulin_comidasExp, xTrain_Insulin_comidasExp_lispro, xTrain_Insulin_comidasExp_profiles, xVal_glucose, xVal_Accel, xVal_DeltaInsulin, xVal_Insulin, xVal_Insulin_lispro, xVal_Insulin_lispro_regular, xVal_Insulin_profiles, xVal_Insulin_exp, xVal_Insulin_comidasDeltas, xVal_Insulin_comidasDeltas_profiles, xVal_Insulin_comidasExp, xVal_Insulin_comidasExp_lispro, xVal_Insulin_comidasExp_profiles, xTest_glucose, xTest_Accel, xTest_DeltaInsulin, xTest_Insulin, xTest_Insulin_lispro, xTest_Insulin_lispro_regular, xTest_Insulin_profiles, xTest_Insulin_exp, xTest_Insulin_comidasDeltas, xTest_Insulin_comidasDeltas_profiles, xTest_Insulin_comidasExp, xTest_Insulin_comidasExp_lispro, xTest_Insulin_comidasExp_profiles = bloque_dividir_datos(xTrain, xVal, xTest)

    #Save dimensions in a file
    dimension_x_y_list.append(['total_patient', xTrain.shape, xVal.shape, xTest.shape, yTrain.shape, yVal.shape, yTest.shape, x.shape, y.shape])
    try_1_list.append(['try_1', xTrain_DeltaInsulin.shape, xVal_DeltaInsulin.shape, xTest_DeltaInsulin.shape, '-', '-', '-', '-', '-'])
    try_2_list.append(['try_2', xTrain_Insulin.shape, xVal_Insulin.shape, xTest_Insulin.shape, '', '', '', '', ''])
    try_3_list.append(['try_3', xTrain_Insulin_lispro.shape, xVal_Insulin_lispro.shape,xTest_Insulin_lispro.shape, '', '', '', '', ''])
    try_4_list.append(['try_4', xTrain_Insulin_comidasDeltas.shape,xVal_Insulin_comidasDeltas.shape, xTest_Insulin_comidasDeltas.shape, '', '', '', '', ''])
    try_5_list.append(['try_5', xTrain_Insulin_comidasExp.shape,xVal_Insulin_comidasExp.shape,xTest_Insulin_comidasExp.shape, '', '', '', '', ''])
    try_6_list.append(['try_6', xTrain_Insulin_comidasExp_lispro.shape, xVal_Insulin_comidasExp_lispro.shape, xTest_Insulin_comidasExp_lispro.shape, '', '', '', '', ''])
    try_7_list.append(['try_7', xTrain_Insulin_comidasExp_profiles.shape, xVal_Insulin_comidasExp_profiles.shape, xTest_Insulin_comidasExp_profiles.shape, '', '', '', '', ''])
    df = pd.DataFrame(dimension_x_y_list, columns=['', 'xTrain', 'xVal', 'xTest', 'yTrain', 'yVal', 'yTest', 'x', 'y'])
    df.loc[1] = try_1_list[0]
    df.loc[2] = try_2_list[0]
    df.loc[3] = try_3_list[0]
    df.loc[4] = try_4_list[0]
    df.loc[5] = try_5_list[0]
    df.loc[6] = try_6_list[0]
    df.loc[7] = try_7_list[0]
    print(df)
    path = path_models_saved + '\Caso_' + str(cn) + '\\00' + str(paciente)  + '\case_' + str(cn) + '_patient_' + str(paciente) + '_matrices.csv'
    df.to_csv(path, index=False)



    return xTrain_glucose, xTrain_Accel, xTrain_DeltaInsulin, xTrain_Insulin, xTrain_Insulin_lispro, xTrain_Insulin_lispro_regular, xTrain_Insulin_profiles, xTrain_Insulin_exp, xTrain_Insulin_comidasDeltas, xTrain_Insulin_comidasDeltas_profiles, xTrain_Insulin_comidasExp, xTrain_Insulin_comidasExp_lispro, xTrain_Insulin_comidasExp_profiles, xVal_glucose, xVal_Accel, xVal_DeltaInsulin, xVal_Insulin, xVal_Insulin_lispro, xVal_Insulin_lispro_regular, xVal_Insulin_profiles, xVal_Insulin_exp, xVal_Insulin_comidasDeltas, xVal_Insulin_comidasDeltas_profiles, xVal_Insulin_comidasExp, xVal_Insulin_comidasExp_lispro, xVal_Insulin_comidasExp_profiles, xTest_glucose, xTest_Accel, xTest_DeltaInsulin, xTest_Insulin, xTest_Insulin_lispro, xTest_Insulin_lispro_regular, xTest_Insulin_profiles, xTest_Insulin_exp, xTest_Insulin_comidasDeltas, xTest_Insulin_comidasDeltas_profiles, xTest_Insulin_comidasExp, xTest_Insulin_comidasExp_lispro, xTest_Insulin_comidasExp_profiles







def root_mean_squared_error(y_true, y_pred):
    return K.sqrt(K.mean(K.square(y_pred - y_true)))

def loss_max(y_true, y_pred):
    from keras import backend as K
    return K.max(K.abs(y_pred - y_true), axis=-1)

def ejecutaModeloSinPrint(units, epochs, batch_size, adam_opt, path_models_saved, cn, paciente, exe, try_number,  xTrain, yTrain, xVal, yVal, xTest, yTest):
    model = Sequential()
    model.add(LSTM(units=units, input_shape=(xTrain.shape[1], xTrain.shape[2])))
    model.add(Dense(units=1))

    model.compile(loss=root_mean_squared_error, optimizer=keras.optimizers.Adam(adam_opt))      #solo 1 vez

    history = model.fit(xTrain, yTrain, epochs=epochs, batch_size=batch_size, validation_data=(xVal, yVal), verbose=0, shuffle=False)         #de nuevo al importar el modelo de otro paciente
    model.summary()
    y_pred = model.predict(xTest)
    score = model.evaluate(xTest, yTest)

    # Guardar el Modelo
    """if caso 1, si no pacientes cambia"""
    path = path_models_saved + '\Caso_' + str(cn) + '\\00' + str(paciente)  + '\case_' + str(cn) + '_patient_' + str(paciente) + '_trynumber_' + str(try_number) + '_execution_' + str(exe) + '_model'
    model.save(path, save_format='tf')
    return y_pred, score

def cargaModeloSinPrint(units, epochs, batch_size, adam_opt, path_models_saved, cn, paciente, exe, try_number,  xTrain, yTrain, xVal, yVal, xTest, yTest):
    # Recrea exactamente el mismo modelo solo desde el archivo
    path = path_models_saved + '\Caso_' + str(cn) + '\\00' + str(paciente)  + '\case_' + str(cn) + '_patient_' + str(paciente) + '_trynumber_' + str(try_number) + '_execution_' + str(exe) + '_model'
    new_model = keras.models.load_model(path, custom_objects={'root_mean_squared_error': root_mean_squared_error})
    history = new_model.fit(xTrain, yTrain, epochs=epochs, batch_size=batch_size, validation_data=(xVal, yVal), verbose=0, shuffle=False)
    y_pred = new_model.predict(xTest)
    score = new_model.evaluate(xTest, yTest)
    return y_pred, score




def bloque_ejecucion(units, epochs, batch_size, adam_opt, cn, pi, path_full_dataset_processed, path_scores_dataset_processed, path_models_saved, execution_number, pacientes, posicion_glucosa):
    print("-EXECUTION: BLOQUE EJECUCIÓN...")
    #pacientes=[1, 2, 4, 6, 7, 8]
    pacientes=[1]

    for paciente in pacientes:
        path_fichero_full_procesados = path_full_dataset_processed[paciente - 1]  # cambiar por path_gai_dataset_processed
        datosProcesados = pd.read_csv(path_fichero_full_procesados)
        print('paciente: ', paciente)
        #print('Tamaño del csv de datos procesados gai previo a comida: ', datosProcesados.shape)




        #execution_number = 10
        execution_list = []

        scores_exp_1 = []
        scores_exp_2 = []
        scores_exp_3 = []
        scores_exp_4 = []
        scores_exp_5 = []
        scores_exp_6 = []
        scores_exp_7 = []
        listaScores = []
        execution_number=2

        xTrain_glucose, xTrain_Accel, xTrain_DeltaInsulin, xTrain_Insulin, xTrain_Insulin_lispro, xTrain_Insulin_lispro_regular, xTrain_Insulin_profiles, xTrain_Insulin_exp, xTrain_Insulin_comidasDeltas, xTrain_Insulin_comidasDeltas_profiles, xTrain_Insulin_comidasExp, xTrain_Insulin_comidasExp_lispro, xTrain_Insulin_comidasExp_profiles, xVal_glucose, xVal_Accel, xVal_DeltaInsulin, xVal_Insulin, xVal_Insulin_lispro, xVal_Insulin_lispro_regular, xVal_Insulin_profiles, xVal_Insulin_exp, xVal_Insulin_comidasDeltas, xVal_Insulin_comidasDeltas_profiles, xVal_Insulin_comidasExp, xVal_Insulin_comidasExp_lispro, xVal_Insulin_comidasExp_profiles, xTest_glucose, xTest_Accel, xTest_DeltaInsulin, xTest_Insulin, xTest_Insulin_lispro, xTest_Insulin_lispro_regular, xTest_Insulin_profiles, xTest_Insulin_exp, xTest_Insulin_comidasDeltas, xTest_Insulin_comidasDeltas_profiles, xTest_Insulin_comidasExp, xTest_Insulin_comidasExp_lispro, xTest_Insulin_comidasExp_profiles = bloque_matriz(path_full_dataset_processed, paciente, posicion_glucosa, datosProcesados)

        for exe in range(execution_number):    #duda, execution antes de bloque matriz, separar x y y dividir datos o depues.
            print('EJECUCION: ', exe)
            execution_list.append("execution_" + str(exe+1) + "_case_" + str(cn) + "_patient_" + str(paciente))

            try_number=1
            #y_pred_exp_1, score_exp_1 = ejecutaModeloSinPrint(units, epochs, batch_size, adam_opt, path_models_saved, cn, paciente, exe, try_number, xTrain_DeltaInsulin, yTrain, xVal_DeltaInsulin, yVal, xTest_DeltaInsulin, yTest)
            #y_pred_exp_1, score_exp_1 = cargaModeloSinPrint(units, epochs, batch_size, adam_opt, path_models_saved, cn, paciente, exe, try_number, xTrain_DeltaInsulin, yTrain, xVal_DeltaInsulin, yVal, xTest_DeltaInsulin, yTest)
            try_number=2
            # y_pred_exp_2, score_exp_2 = ejecutaModeloSinPrint(units, epochs, batch_size, adam_opt, path_models_saved, cn, paciente, exe, try_number, xTrain_Insulin, yTrain, xVal_Insulin, yVal, xTest_Insulin, yTest)
            try_number=3
            # y_pred_exp_3, score_exp_3 = ejecutaModeloSinPrint(units, epochs, batch_size, adam_opt, path_models_saved, cn, paciente, exe, try_number, xTrain_Insulin_lispro, yTrain, xVal_Insulin_lispro, yVal, xTest_Insulin_lispro, yTest)
            try_number = 4
            # _pred_exp_4, score_exp_4 = ejecutaModeloSinPrint(units, epochs, batch_size, adam_opt, path_models_saved, cn, paciente, exe, try_number, xTrain_Insulin_comidasDeltas, yTrain, xVal_Insulin_comidasDeltas, yVal, xTest_Insulin_comidasDeltas, yTest)
            try_number = 5
            # y_pred_exp_5, score_exp_5 = ejecutaModeloSinPrint(units, epochs, batch_size, adam_opt, path_models_saved, cn, paciente, exe, try_number, xTrain_Insulin_comidasExp, yTrain, xVal_Insulin_comidasExp, yVal, xTest_Insulin_comidasExp, yTest)
            try_number = 6
            # y_pred_exp_6, score_exp_6 = ejecutaModeloSinPrint(units, epochs, batch_size, adam_opt, path_models_saved, cn, , paciente, exe, try_number, xTrain_Insulin_comidasExp_lispro, yTrain, xVal_Insulin_comidasExp_lispro, yVal, xTest_Insulin_comidasExp_lispro, yTest)
            try_number = 7
            # y_pred_exp_7, score_exp_7 = ejecutaModeloSinPrint(units, epochs, batch_size, adam_opt, path_models_saved, cn, , paciente, exe, try_number, xTrain_Insulin_comidasExp_profiles, yTrain, xVal_Insulin_comidasExp_profiles, yVal, xTest_Insulin_comidasExp_profiles, yTest)

            y_pred_exp_1, score_exp_1 = 1, 3
            y_pred_exp_2, score_exp_2 = 1, 4
            y_pred_exp_3, score_exp_3 = 1, 5
            y_pred_exp_4, score_exp_4 = 1, 6
            y_pred_exp_5, score_exp_5 = 1, 7
            y_pred_exp_6, score_exp_6 = 1, 8
            y_pred_exp_7, score_exp_7 = 1, 9

            print('score_exp_1: ', score_exp_1)
            print('score_exp_2: ', score_exp_2)
            print('score_exp_3: ', score_exp_3)
            print('score_exp_4: ', score_exp_4)
            print('score_exp_5: ', score_exp_5)
            print('score_exp_6: ', score_exp_6)
            print('score_exp_7: ', score_exp_7)


print("MAIN: BLOQUE EJECUCIÓN...")
bloque_ejecucion(units, epochs, batch_size, adam_opt, cn, pi, path_full_dataset_processed, path_scores_dataset_processed, path_models_saved, execution_number, pacientes, posicion_glucosa)
