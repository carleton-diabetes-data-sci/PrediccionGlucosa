import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


def separar_x_y(x ,y):
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

    # print(x.shape)   #(2738, 24, 14)
    # print(y.shape)   #(2738,)

    xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size = 0.2, random_state = 0)
    print (xTrain.shape)    # (2190, 24, 14)  [[[7.40000000e+00 4.21584213e+01 0.00000000e+00 ... 0.00000000e+00   5.76909235e-02 2.60332989e+00]
    print (xTest.shape)     # (548, 24, 14)      [[[12.9        45.11801353  0.         ...  0.          0.       0.        ]
    print(yTrain.shape)    # (2190,)            [ 3.7 11.5  4.6 ...  7.2  4.6  4.6]
    print(yTest.shape)      # (548,)    [ 6.3  6.9  8.   4.3  ... 6.3 22.2  2.5 13.5   5.5 16.3]

    xTrain, xVal, yTrain, yVal = train_test_split(xTrain, yTrain, test_size = 0.25, random_state = 0)
    print(xTrain.shape)  # (1642, 24, 14)
    print(xVal.shape)  # (548, 24, 14)
    print (yVal.shape)  # (548,)

    return xTrain, xVal, xTest, yTrain, yVal, yTest
    # (4688, 24, 14)
    # (1172, 24, 14)
    # (4688,)
    # (1172,)
    # (3516, 24, 14)
    # (1172, 24, 14)
    # (1172,)


def divideDatos(xDiv):
    #ac = 1 or 0
    ac=1
    xDiv_glucose = np.zeros(xDiv.shape[0] * xDiv.shape[1]).reshape((xDiv.shape[0], xDiv.shape[1], 1))  # change dimensions
    xDiv_Accel = np.zeros(xDiv.shape[0] * xDiv.shape[1]).reshape((xDiv.shape[0], xDiv.shape[1], 1+ac))
    xDiv_DeltaInsulin = np.zeros(xDiv.shape[0] * xDiv.shape[1] * 3).reshape((xDiv.shape[0], xDiv.shape[1], 2+ac))
    xDiv_Insulin = np.zeros(xDiv.shape[0] * xDiv.shape[1] * 3).reshape((xDiv.shape[0], xDiv.shape[1], 2+ac))
    xDiv_Insulin_lispro = np.zeros(xDiv.shape[0] * xDiv.shape[1] * 3).reshape((xDiv.shape[0], xDiv.shape[1], 2+ac))
    xDiv_Insulin_lispro_regular = np.zeros(xDiv.shape[0] * xDiv.shape[1] * 3).reshape((xDiv.shape[0], xDiv.shape[1], 2+ac))
    xDiv_Insulin_profiles = np.zeros(xDiv.shape[0] * xDiv.shape[1] * 3).reshape((xDiv.shape[0], xDiv.shape[1], 2+ac))
    xDiv_Insulin_exp = np.zeros(xDiv.shape[0] * xDiv.shape[1] * 3).reshape((xDiv.shape[0], xDiv.shape[1], 2+ac))
    xDiv_Insulin_comidasDeltas = np.zeros(xDiv.shape[0] * xDiv.shape[1] * 4).reshape((xDiv.shape[0], xDiv.shape[1], 3+ac))
    xDiv_Insulin_comidasDeltas_profiles = np.zeros(xDiv.shape[0] * xDiv.shape[1] * 4).reshape((xDiv.shape[0], xDiv.shape[1], 3+ac))
    xDiv_Insulin_comidasExp = np.zeros(xDiv.shape[0] * xDiv.shape[1] * 4).reshape((xDiv.shape[0], xDiv.shape[1], 3+ac))
    xDiv_Insulin_comidasExp_lispro = np.zeros(xDiv.shape[0] * xDiv.shape[1] * 4).reshape((xDiv.shape[0], xDiv.shape[1], 3+ac))
    xDiv_Insulin_comidasExp_profiles = np.zeros(xDiv.shape[0] * xDiv.shape[1] * 4).reshape((xDiv.shape[0], xDiv.shape[1], 3+ac))

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
    xTrain_glucose, xTrain_Accel, xTrain_DeltaInsulin, xTrain_Insulin, xTrain_Insulin_lispro, xTrain_Insulin_lispro_regular, xTrain_Insulin_profiles, xTrain_Insulin_exp, xTrain_Insulin_comidasDeltas, xTrain_Insulin_comidasDeltas_profiles, xTrain_Insulin_comidasExp, xTrain_Insulin_comidasExp_lispro, xTrain_Insulin_comidasExp_profiles = divideDatos(
        xTrain)
    #print('xTrain_glucose tiene un tamaño: ', xTrain_glucose.shape)
    #print('xTrain_Accel tiene un tamaño: ', xTrain_Accel.shape)
    # print('xTrain_DeltaInsulin tiene un tamaño: ',xTrain_DeltaInsulin.shape)
    # print('xTrain_Insulin tiene un tamaño: ',xTrain_Insulin.shape)
    # xTrain_Insulin_lispro
    # xTrain_Insulin_lispro_regular
    # xTrain_Insulin_profiles
    # print('xTrain_Insulin_exp tiene un tamaño: ',xTrain_Insulin_exp.shape)
    # print('xTrain_Insulin_comidasDeltas tiene un tamaño: ',xTrain_Insulin_comidasDeltas.shape)
    # xTrain_Insulin_comidasDeltas_profiles
    # print('xTrain_Insulin_comidasExp tiene un tamaño: ',xTrain_Insulin_comidasExp.shape)
    # xTrainv_Insulin_comidasExp_lispro
    # xTrain_Insulin_comidasExp_profiles

    xVal_glucose, xVal_Accel, xVal_DeltaInsulin, xVal_Insulin, xVal_Insulin_lispro, xVal_Insulin_lispro_regular, xVal_Insulin_profiles, xVal_Insulin_exp, xVal_Insulin_comidasDeltas, xVal_Insulin_comidasDeltas_profiles, xVal_Insulin_comidasExp, xVal_Insulin_comidasExp_lispro, xVal_Insulin_comidasExp_profiles = divideDatos(
        xVal)
    # print('xVal_glucose tiene un tamaño: ',xVal_glucose.shape)
    # print('xVal_Accel tiene un tamaño: ',xVal_Accel.shape)
    # print('xVal_DeltaInsulin tiene un tamaño: ',xVal_DeltaInsulin.shape)
    # print('xVal_Insulin tiene un tamaño: ',xVal_Insulin.shape)
    # print('xVal_Insulin_exp tiene un tamaño: ',xVal_Insulin_exp.shape)
    # print('xVal_Insulin_comidasDeltas tiene un tamaño: ',xVal_Insulin_comidasDeltas.shape)
    # print('xVal_Insulin_comidasExp tiene un tamaño: ',xVal_Insulin_comidasExp.shape)

    xTest_glucose, xTest_Accel, xTest_DeltaInsulin, xTest_Insulin, xTest_Insulin_lispro, xTest_Insulin_lispro_regular, xTest_Insulin_profiles, xTest_Insulin_exp, xTest_Insulin_comidasDeltas, xTest_Insulin_comidasDeltas_profiles, xTest_Insulin_comidasExp, xTest_Insulin_comidasExp_lispro, xTest_Insulin_comidasExp_profiles = divideDatos(
        xTest)
    # print('xTest_glucose tiene un tamaño: ',xTest_glucose.shape)
    # print('xTest_Accel tiene un tamaño: ',xTest_Accel.shape)
    # print('xTest_DeltaInsulin tiene un tamaño: ',xTest_DeltaInsulin.shape)
    # print('xTest_Insulin tiene un tamaño: ',xTest_Insulin.shape)
    # print('xTest_Insulin_exp tiene un tamaño: ',xTest_Insulin_exp.shape)
    # print('xTest_Insulin_comidasDeltas tiene un tamaño: ',xTest_Insulin_comidasDeltas.shape)
    # print('xTest_Insulin_comidasExp tiene un tamaño: ',xTest_Insulin_comidasExp.shape)

    return xTrain_glucose, xTrain_Accel, xTrain_DeltaInsulin, xTrain_Insulin, xTrain_Insulin_lispro, xTrain_Insulin_lispro_regular, xTrain_Insulin_profiles, xTrain_Insulin_exp, xTrain_Insulin_comidasDeltas, xTrain_Insulin_comidasDeltas_profiles, xTrain_Insulin_comidasExp, xTrain_Insulin_comidasExp_lispro, xTrain_Insulin_comidasExp_profiles, xVal_glucose, xVal_Accel, xVal_DeltaInsulin, xVal_Insulin, xVal_Insulin_lispro, xVal_Insulin_lispro_regular, xVal_Insulin_profiles, xVal_Insulin_exp, xVal_Insulin_comidasDeltas, xVal_Insulin_comidasDeltas_profiles, xVal_Insulin_comidasExp, xVal_Insulin_comidasExp_lispro, xVal_Insulin_comidasExp_profiles, xTest_glucose, xTest_Accel, xTest_DeltaInsulin, xTest_Insulin, xTest_Insulin_lispro, xTest_Insulin_lispro_regular, xTest_Insulin_profiles, xTest_Insulin_exp, xTest_Insulin_comidasDeltas, xTest_Insulin_comidasDeltas_profiles, xTest_Insulin_comidasExp, xTest_Insulin_comidasExp_lispro, xTest_Insulin_comidasExp_profiles
