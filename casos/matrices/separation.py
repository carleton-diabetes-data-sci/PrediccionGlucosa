import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

from tensorflow.keras import backend as K

def root_mean_squared_error(y_true, y_pred):
    return K.eval(K.sqrt(K.mean(K.square(y_pred - y_true))))


def separar_train_val_test(cn, x ,y, paciente, path_models_saved):
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

    print("---SEPARATION: SEPARATE TRAIN, VAL AND TEST")
    dimension_x_y_list=[]
    # print(x.shape)   #(2738, 24, 14)
    # print(y.shape)   #(2738,)

    xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size = 0.2, random_state = 0)
    #print('Tamaño de xTest: ', xTest.shape)  # (548, 24, 14)      [[[12.9        45.11801353  0.         ...  0.          0.       0.        ]
    #print('Tamaño de yTest: ', yTest.shape)   # (548,)    [ 6.3  6.9  8.   4.3  ... 6.3 22.2  2.5 13.5   5.5 16.3]

    # Calculate and print performance (RMSE) of naive model on unshuffled test data (last 20%)
        # yTest is an array containing actual blood glucose levels (one hour into the future)
        # xTest[:,-1,0] is an array containing the last glucose reading for each two-hour training window
            # the colon selects all data points
            # -1 refers to the last time step
            # 0 refers to the first feature, which is blood glucose
    # By calculating the RMSE between values from these two arrays,
    # we obtain the RMSE of a naive model that simply predicts that a patient's
    # blood glucose level one hour in the future will equal their current blood glucose level
    xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size = 0.2, random_state = 0, shuffle=False)
    rmse = root_mean_squared_error(yTest, xTest[:,-1,0])
    print("Naive RMSE (last 20%):", rmse, "mmol/L\t", rmse * 18, "mg/dL (x18)")

    xTrain, xVal, yTrain, yVal = train_test_split(xTrain, yTrain, test_size = 0.25, random_state = 0)
    #print('Tamaño de xTrain: ', xTrain.shape)     # (1642, 24, 14)
    #print('Tamaño de yTrain: ', yTrain.shape)
    #print('Tamaño de xVal: ', xVal.shape) # (548, 24, 14)
    #print('Tamaño de yVal: ', yVal.shape)  # (548,)

    #print('Tamaño de x, xTrain, xVal y xTest: ', x.shape, xTrain.shape, xVal.shape, xTest.shape)   # patient 1 Caso 0 (665, 24, 14) (399, 24, 14) (133, 24, 14) (133, 24, 14)
    #all patients Caso 1 (3516, 24, 14), (1172, 24, 14), (1172, 24, 14)

    dimension_x_y_list.append([x.shape, y.shape, xTrain.shape, yTrain.shape, xVal.shape, yVal.shape, xTest.shape, yTest.shape])
    df = pd.DataFrame(np.array(dimension_x_y_list), columns=['x', 'y', 'xTrain', 'yTrain', 'xVal', 'yVal', 'xTest', 'yTest'])

    path = path_models_saved + '/Caso_' + str(cn) + '//00' + str(paciente)  + '/case_' + str(cn) + '_patient_' + str(paciente) + '_matrices.csv'
    df.to_csv(path, index=False)

    return xTrain, xVal, xTest, yTrain, yVal, yTest



def divideDatos(xDiv, ac):
    print("----SEPARATION: DIVIDE DATE INTO TRY CONFIGURATIONS")
    #ac = 1 #or 0 in case of no acceleration
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

def bloque_dividir_datos(xTrain, xVal, xTest, ac):
    print("---SEPARATION: DIVIDE DATA INTO TRAIN, VAL AND TEST")

    xTrain_glucose, xTrain_Accel, xTrain_DeltaInsulin, xTrain_Insulin, xTrain_Insulin_lispro, xTrain_Insulin_lispro_regular, xTrain_Insulin_profiles, xTrain_Insulin_exp, xTrain_Insulin_comidasDeltas, xTrain_Insulin_comidasDeltas_profiles, xTrain_Insulin_comidasExp, xTrain_Insulin_comidasExp_lispro, xTrain_Insulin_comidasExp_profiles = divideDatos(xTrain, ac)

    # print('xTrain_try_1 tiene un tamaño: ',xTrain_DeltaInsulin.shape)
    # print('xTrain_try_2 tiene un tamaño: ',xTrain_Insulin.shape)
    # print('xTrain_try_3 tiene un tamaño: ',xTrain_Insulin_lispro.shape)
    # print('xTrain_try_4 tiene un tamaño: ',xTrain_Insulin_comidasDeltas.shape)
    # print('xTrain_try_5 tiene un tamaño: ',xTrain_Insulin_comidasExp.shape)
    # print('xTrain_try_6 tiene un tamaño: ',xTrain_Insulin_comidasExp_lispro.shape)
    # print('xTrain_try_7 tiene un tamaño: ',xTrain_Insulin_comidasExp_profiles.shape)

    xVal_glucose, xVal_Accel, xVal_DeltaInsulin, xVal_Insulin, xVal_Insulin_lispro, xVal_Insulin_lispro_regular, xVal_Insulin_profiles, xVal_Insulin_exp, xVal_Insulin_comidasDeltas, xVal_Insulin_comidasDeltas_profiles, xVal_Insulin_comidasExp, xVal_Insulin_comidasExp_lispro, xVal_Insulin_comidasExp_profiles = divideDatos(xVal, ac)

    # print('xVal_try_1 tiene un tamaño: ',xVal_DeltaInsulin.shape)
    # print('xVal_try_2 tiene un tamaño: ',xVal_Insulin.shape)
    # print('xVal_try_3 tiene un tamaño: ',xVal_Insulin_lispro.shape)
    # print('xVal_try_4 tiene un tamaño: ',xVal_Insulin_comidasDeltas.shape)
    # print('xVal_try_5 tiene un tamaño: ',xVal_Insulin_comidasExp.shape)
    # print('xVal_try_6 tiene un tamaño: ',xVal_Insulin_comidasExp_lispro.shape)
    # print('xVal_try_7 tiene un tamaño: ',xVal_Insulin_comidasExp_profiles.shape)

    xTest_glucose, xTest_Accel, xTest_DeltaInsulin, xTest_Insulin, xTest_Insulin_lispro, xTest_Insulin_lispro_regular, xTest_Insulin_profiles, xTest_Insulin_exp, xTest_Insulin_comidasDeltas, xTest_Insulin_comidasDeltas_profiles, xTest_Insulin_comidasExp, xTest_Insulin_comidasExp_lispro, xTest_Insulin_comidasExp_profiles = divideDatos(xTest, ac)

    # print('xTest_try_1 tiene un tamaño: ',xTest_DeltaInsulin.shape)
    # print('xTest_try_2 tiene un tamaño: ',xTest_Insulin.shape)
    # print('xTest_try_3 tiene un tamaño: ',xTest_Insulin_lispro.shape)
    # print('xTest_try_4 tiene un tamaño: ',xTest_Insulin_comidasDeltas.shape)
    # print('xTest_try_5 tiene un tamaño: ',xTest_Insulin_comidasExp.shape)
    # print('xTest_try_6 tiene un tamaño: ',xTest_Insulin_comidasExp_lispro.shape)
    # print('xTest_try_7 tiene un tamaño: ',xTest_Insulin_comidasExp_profiles.shape)

    return xTrain_glucose, xTrain_Accel, xTrain_DeltaInsulin, xTrain_Insulin, xTrain_Insulin_lispro, xTrain_Insulin_lispro_regular, xTrain_Insulin_profiles, xTrain_Insulin_exp, xTrain_Insulin_comidasDeltas, xTrain_Insulin_comidasDeltas_profiles, xTrain_Insulin_comidasExp, xTrain_Insulin_comidasExp_lispro, xTrain_Insulin_comidasExp_profiles, xVal_glucose, xVal_Accel, xVal_DeltaInsulin, xVal_Insulin, xVal_Insulin_lispro, xVal_Insulin_lispro_regular, xVal_Insulin_profiles, xVal_Insulin_exp, xVal_Insulin_comidasDeltas, xVal_Insulin_comidasDeltas_profiles, xVal_Insulin_comidasExp, xVal_Insulin_comidasExp_lispro, xVal_Insulin_comidasExp_profiles, xTest_glucose, xTest_Accel, xTest_DeltaInsulin, xTest_Insulin, xTest_Insulin_lispro, xTest_Insulin_lispro_regular, xTest_Insulin_profiles, xTest_Insulin_exp, xTest_Insulin_comidasDeltas, xTest_Insulin_comidasDeltas_profiles, xTest_Insulin_comidasExp, xTest_Insulin_comidasExp_lispro, xTest_Insulin_comidasExp_profiles


