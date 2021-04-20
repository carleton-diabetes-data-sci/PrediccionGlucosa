import time
from casos.execution.model import guardar_modelo, cargar_modelo
import pandas as pd
import numpy as np


def bloque_guardar_modelos_experimentos(cargar, units, epochs, batch_size, adam_opt, path_models_saved, cn, paciente, exe, yTrain, yVal, yTest, xTrain_glucose, xTrain_Accel, xTrain_DeltaInsulin, xTrain_Insulin, xTrain_Insulin_lispro, xTrain_Insulin_lispro_regular, xTrain_Insulin_profiles, xTrain_Insulin_exp, xTrain_Insulin_comidasDeltas, xTrain_Insulin_comidasDeltas_profiles, xTrain_Insulin_comidasExp, xTrain_Insulin_comidasExp_lispro, xTrain_Insulin_comidasExp_profiles, xVal_glucose, xVal_Accel, xVal_DeltaInsulin, xVal_Insulin, xVal_Insulin_lispro, xVal_Insulin_lispro_regular, xVal_Insulin_profiles, xVal_Insulin_exp, xVal_Insulin_comidasDeltas, xVal_Insulin_comidasDeltas_profiles, xVal_Insulin_comidasExp, xVal_Insulin_comidasExp_lispro, xVal_Insulin_comidasExp_profiles, xTest_glucose, xTest_Accel, xTest_DeltaInsulin, xTest_Insulin, xTest_Insulin_lispro, xTest_Insulin_lispro_regular, xTest_Insulin_profiles, xTest_Insulin_exp, xTest_Insulin_comidasDeltas, xTest_Insulin_comidasDeltas_profiles, xTest_Insulin_comidasExp, xTest_Insulin_comidasExp_lispro, xTest_Insulin_comidasExp_profiles):
    print("-- MODELS_TRIES: bloque_guardar_modelos_experimentos")
    start_time = time.time()
    if (cargar==0):
        try_number = 1
        guardar_modelo(units, epochs, batch_size, adam_opt, path_models_saved, cn, paciente, exe, try_number, xTrain_DeltaInsulin, yTrain, xVal_DeltaInsulin, yVal, xTest_DeltaInsulin, yTest)
        try_number = 2
        guardar_modelo(units, epochs, batch_size, adam_opt, path_models_saved, cn, paciente, exe, try_number, xTrain_Insulin, yTrain, xVal_Insulin, yVal, xTest_Insulin, yTest)
        try_number = 3
        guardar_modelo(units, epochs, batch_size, adam_opt, path_models_saved, cn, paciente, exe, try_number, xTrain_Insulin_lispro, yTrain, xVal_Insulin_lispro, yVal, xTest_Insulin_lispro, yTest)
        try_number = 4
        guardar_modelo(units, epochs, batch_size, adam_opt, path_models_saved, cn, paciente, exe, try_number, xTrain_Insulin_comidasDeltas, yTrain, xVal_Insulin_comidasDeltas, yVal, xTest_Insulin_comidasDeltas, yTest)
        try_number = 5
        guardar_modelo(units, epochs, batch_size, adam_opt, path_models_saved, cn, paciente, exe, try_number, xTrain_Insulin_comidasExp, yTrain, xVal_Insulin_comidasExp, yVal, xTest_Insulin_comidasExp, yTest)
        try_number = 6
        guardar_modelo(units, epochs, batch_size, adam_opt, path_models_saved, cn, paciente, exe, try_number, xTrain_Insulin_comidasExp_lispro, yTrain, xVal_Insulin_comidasExp_lispro, yVal, xTest_Insulin_comidasExp_lispro, yTest)
        try_number = 7
        guardar_modelo(units, epochs, batch_size, adam_opt, path_models_saved, cn, paciente, exe, try_number, xTrain_Insulin_comidasExp_profiles, yTrain, xVal_Insulin_comidasExp_profiles, yVal, xTest_Insulin_comidasExp_profiles, yTest)


    #Save time in a file
    t=[]
    t.append([time.time() - start_time])
    df = pd.DataFrame(t, columns=['train_model_time (s)'])
    #print(df)
    path = path_models_saved + '\Caso_' + str(cn) + '\\00' + str(paciente) + '\case_' + str(cn) + '_patient_' + str(paciente) + '_save_time.csv'
    df.to_csv(path, index=False)
    print("--- bloque_guardar_modelos_experimentos takes %s seconds: ---" % (time.time() - start_time))



def bloque_cargar_modelos_experimentos(cargar, listaScores, units, epochs, batch_size, adam_opt, path_models_saved, cn, paciente, exe, yTrain, yVal, yTest, xTrain_glucose, xTrain_Accel, xTrain_DeltaInsulin, xTrain_Insulin, xTrain_Insulin_lispro, xTrain_Insulin_lispro_regular, xTrain_Insulin_profiles, xTrain_Insulin_exp, xTrain_Insulin_comidasDeltas, xTrain_Insulin_comidasDeltas_profiles, xTrain_Insulin_comidasExp, xTrain_Insulin_comidasExp_lispro, xTrain_Insulin_comidasExp_profiles, xVal_glucose, xVal_Accel, xVal_DeltaInsulin, xVal_Insulin, xVal_Insulin_lispro, xVal_Insulin_lispro_regular, xVal_Insulin_profiles, xVal_Insulin_exp, xVal_Insulin_comidasDeltas, xVal_Insulin_comidasDeltas_profiles, xVal_Insulin_comidasExp, xVal_Insulin_comidasExp_lispro, xVal_Insulin_comidasExp_profiles, xTest_glucose, xTest_Accel, xTest_DeltaInsulin, xTest_Insulin, xTest_Insulin_lispro, xTest_Insulin_lispro_regular, xTest_Insulin_profiles, xTest_Insulin_exp, xTest_Insulin_comidasDeltas, xTest_Insulin_comidasDeltas_profiles, xTest_Insulin_comidasExp, xTest_Insulin_comidasExp_lispro, xTest_Insulin_comidasExp_profiles):
    print("-- MODELS_TRIES: bloque_cargar_modelos_experimentos")
    start_time = time.time()

    scores_exp_1 = []
    scores_exp_2 = []
    scores_exp_3 = []
    scores_exp_4 = []
    scores_exp_5 = []
    scores_exp_6 = []
    scores_exp_7 = []

    if(cargar==1):
        try_number = 1
        y_pred_exp_1, score_exp_1 = cargar_modelo(units, epochs, batch_size, adam_opt, path_models_saved, cn, paciente, exe, try_number, xTrain_DeltaInsulin, yTrain, xVal_DeltaInsulin, yVal, xTest_DeltaInsulin, yTest)
        try_number = 2
        y_pred_exp_2, score_exp_2 = cargar_modelo(units, epochs, batch_size, adam_opt, path_models_saved, cn, paciente, exe, try_number, xTrain_Insulin, yTrain, xVal_Insulin, yVal, xTest_Insulin, yTest)
        try_number = 3
        y_pred_exp_3, score_exp_3 = cargar_modelo(units, epochs, batch_size, adam_opt, path_models_saved, cn, paciente, exe, try_number, xTrain_Insulin_lispro, yTrain, xVal_Insulin_lispro, yVal, xTest_Insulin_lispro, yTest)
        try_number = 4
        y_pred_exp_4, score_exp_4 = cargar_modelo(units, epochs, batch_size, adam_opt, path_models_saved, cn, paciente, exe, try_number, xTrain_Insulin_comidasDeltas, yTrain, xVal_Insulin_comidasDeltas, yVal, xTest_Insulin_comidasDeltas, yTest)
        try_number = 5
        y_pred_exp_5, score_exp_5 = cargar_modelo(units, epochs, batch_size, adam_opt, path_models_saved, cn, paciente, exe, try_number, xTrain_Insulin_comidasExp, yTrain, xVal_Insulin_comidasExp, yVal, xTest_Insulin_comidasExp, yTest)
        try_number = 6
        y_pred_exp_6, score_exp_6 = cargar_modelo(units, epochs, batch_size, adam_opt, path_models_saved, cn, paciente, exe, try_number, xTrain_Insulin_comidasExp_lispro, yTrain, xVal_Insulin_comidasExp_lispro, yVal, xTest_Insulin_comidasExp_lispro, yTest)
        try_number = 7
        y_pred_exp_7, score_exp_7 = cargar_modelo(units, epochs, batch_size, adam_opt, path_models_saved, cn, paciente, exe, try_number, xTrain_Insulin_comidasExp_profiles, yTrain, xVal_Insulin_comidasExp_profiles, yVal, xTest_Insulin_comidasExp_profiles, yTest)

    elif(cargar==0):
        y_pred_exp_1, score_exp_1 = 1, 3
        y_pred_exp_2, score_exp_2 = 1, 4
        y_pred_exp_3, score_exp_3 = 1, 5
        y_pred_exp_4, score_exp_4 = 1, 6
        y_pred_exp_5, score_exp_5 = 1, 7
        y_pred_exp_6, score_exp_6 = 1, 8
        y_pred_exp_7, score_exp_7 = 1, 9

    #print('score_exp_1: ', score_exp_1)
    #print('score_exp_2: ', score_exp_2)
    #print('score_exp_3: ', score_exp_3)
    #print('score_exp_4: ', score_exp_4)
    #print('score_exp_5: ', score_exp_5)
    #print('score_exp_6: ', score_exp_6)
    #print('score_exp_7: ', score_exp_7)

    scores_exp_1.append(score_exp_1)
    scores_exp_2.append(score_exp_2)
    scores_exp_3.append(score_exp_3)
    scores_exp_4.append(score_exp_4)
    scores_exp_5.append(score_exp_5)
    scores_exp_6.append(score_exp_6)
    scores_exp_7.append(score_exp_7)

    listaScores.append([score_exp_1, score_exp_2, score_exp_3, score_exp_4, score_exp_5, score_exp_6, score_exp_7])

    # Save time in a file
    t = []
    t.append([time.time() - start_time])
    df = pd.DataFrame(t, columns=['load_model_time (s)'])
    # print(df)
    path = path_models_saved + '\Caso_' + str(cn) + '\\00' + str(paciente) + '\case_' + str(cn) + '_patient_' + str(paciente) + '_execution_' + str(exe) + '_load_time.csv'
    df.to_csv(path, index=False)
    print("--- bloque_cargar_modelos_experimentos takes %s seconds: ---" % (time.time() - start_time))

    return listaScores, scores_exp_1, scores_exp_2, scores_exp_3, scores_exp_4, scores_exp_5, scores_exp_6, scores_exp_7