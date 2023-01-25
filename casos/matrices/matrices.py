import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

from matrices.separation import separar_train_val_test, bloque_dividir_datos


def bloque_matriz(cn, ac, path_full_dataset_processed, paciente, posicion_glucosa, datosProcesados, path_models_saved):
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
    print("--MATRICES: BLOQUE MATRIZ GENERATES MATRICES")

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
    #print('Tamaño de x: ', x.shape)

    y = np.array(y_glucose)
    #print('Tamaño de y: ', y.shape)

    xTrain, xVal, xTest, yTrain, yVal, yTest = separar_train_val_test(cn, x, y, paciente, path_models_saved)
    xTrain_glucose, xTrain_Accel, xTrain_DeltaInsulin, xTrain_Insulin, xTrain_Insulin_lispro, xTrain_Insulin_lispro_regular, xTrain_Insulin_profiles, xTrain_Insulin_exp, xTrain_Insulin_comidasDeltas, xTrain_Insulin_comidasDeltas_profiles, xTrain_Insulin_comidasExp, xTrain_Insulin_comidasExp_lispro, xTrain_Insulin_comidasExp_profiles, xVal_glucose, xVal_Accel, xVal_DeltaInsulin, xVal_Insulin, xVal_Insulin_lispro, xVal_Insulin_lispro_regular, xVal_Insulin_profiles, xVal_Insulin_exp, xVal_Insulin_comidasDeltas, xVal_Insulin_comidasDeltas_profiles, xVal_Insulin_comidasExp, xVal_Insulin_comidasExp_lispro, xVal_Insulin_comidasExp_profiles, xTest_glucose, xTest_Accel, xTest_DeltaInsulin, xTest_Insulin, xTest_Insulin_lispro, xTest_Insulin_lispro_regular, xTest_Insulin_profiles, xTest_Insulin_exp, xTest_Insulin_comidasDeltas, xTest_Insulin_comidasDeltas_profiles, xTest_Insulin_comidasExp, xTest_Insulin_comidasExp_lispro, xTest_Insulin_comidasExp_profiles = bloque_dividir_datos(xTrain, xVal, xTest, ac)

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
    #print(df)
    path = path_models_saved + '/Caso_' + str(cn) + '//00' + str(paciente)  + '/case_' + str(cn) + '_patient_' + str(paciente) + '_matrices.csv'
    df.to_csv(path, index=False)
    return yTrain, yVal, yTest, xTrain_glucose, xTrain_Accel, xTrain_DeltaInsulin, xTrain_Insulin, xTrain_Insulin_lispro, xTrain_Insulin_lispro_regular, xTrain_Insulin_profiles, xTrain_Insulin_exp, xTrain_Insulin_comidasDeltas, xTrain_Insulin_comidasDeltas_profiles, xTrain_Insulin_comidasExp, xTrain_Insulin_comidasExp_lispro, xTrain_Insulin_comidasExp_profiles, xVal_glucose, xVal_Accel, xVal_DeltaInsulin, xVal_Insulin, xVal_Insulin_lispro, xVal_Insulin_lispro_regular, xVal_Insulin_profiles, xVal_Insulin_exp, xVal_Insulin_comidasDeltas, xVal_Insulin_comidasDeltas_profiles, xVal_Insulin_comidasExp, xVal_Insulin_comidasExp_lispro, xVal_Insulin_comidasExp_profiles, xTest_glucose, xTest_Accel, xTest_DeltaInsulin, xTest_Insulin, xTest_Insulin_lispro, xTest_Insulin_lispro_regular, xTest_Insulin_profiles, xTest_Insulin_exp, xTest_Insulin_comidasDeltas, xTest_Insulin_comidasDeltas_profiles, xTest_Insulin_comidasExp, xTest_Insulin_comidasExp_lispro, xTest_Insulin_comidasExp_profiles




