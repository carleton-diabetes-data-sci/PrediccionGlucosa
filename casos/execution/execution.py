import pandas as pd
import numpy as np

from casos.matrices.matrices import bloque_matriz
from casos.execution.models_tries import bloque_guardar_modelos_experimentos, bloque_cargar_modelos_experimentos

def bloque_ejecucion(cargar, units, epochs, batch_size, adam_opt, cn, ac, pi, path_full_dataset_processed, path_scores_dataset_processed, path_models_saved, execution_number, pacientes, posicion_glucosa):
    print("-EXECUTION: BLOQUE EJECUCIÓN...")
    #pacientes=[1, 2, 4, 6, 7, 8]
    #pacientes=[8]
    execution_number = 1
    #cargar = 0

    for paciente in pacientes:
        path_fichero_full_procesados = path_full_dataset_processed[paciente - 1]  # cambiar por path_gai_dataset_processed
        datosProcesados = pd.read_csv(path_fichero_full_procesados)
        print('PACIENTE: ', paciente)
        #print('Tamaño del csv de datos procesados gai previo a comida: ', datosProcesados.shape)

        execution_list = []
        listaScores = []
        scores_exp_1 = []
        scores_exp_2 = []
        scores_exp_3 = []
        scores_exp_4 = []
        scores_exp_5 = []
        scores_exp_6 = []
        scores_exp_7 = []

        #bloque matriz antes o después de las ejecuciones independiente, depende entonces si se vuelven a dividir xtrain, xval y xtest en las ejecuciones.  Antes, se repiten resultados.
        yTrain, yVal, yTest, xTrain_glucose, xTrain_Accel, xTrain_DeltaInsulin, xTrain_Insulin, xTrain_Insulin_lispro, xTrain_Insulin_lispro_regular, xTrain_Insulin_profiles, xTrain_Insulin_exp, xTrain_Insulin_comidasDeltas, xTrain_Insulin_comidasDeltas_profiles, xTrain_Insulin_comidasExp, xTrain_Insulin_comidasExp_lispro, xTrain_Insulin_comidasExp_profiles, xVal_glucose, xVal_Accel, xVal_DeltaInsulin, xVal_Insulin, xVal_Insulin_lispro, xVal_Insulin_lispro_regular, xVal_Insulin_profiles, xVal_Insulin_exp, xVal_Insulin_comidasDeltas, xVal_Insulin_comidasDeltas_profiles, xVal_Insulin_comidasExp, xVal_Insulin_comidasExp_lispro, xVal_Insulin_comidasExp_profiles, xTest_glucose, xTest_Accel, xTest_DeltaInsulin, xTest_Insulin, xTest_Insulin_lispro, xTest_Insulin_lispro_regular, xTest_Insulin_profiles, xTest_Insulin_exp, xTest_Insulin_comidasDeltas, xTest_Insulin_comidasDeltas_profiles, xTest_Insulin_comidasExp, xTest_Insulin_comidasExp_lispro, xTest_Insulin_comidasExp_profiles = bloque_matriz(cn, ac, path_full_dataset_processed, paciente, posicion_glucosa, datosProcesados, path_models_saved)

        for exe in range(execution_number):    #duda, execution antes de bloque matriz, separar x y y dividir datos o depues.
            print('\t EJECUCION: ', exe)
            execution_list.append("execution_" + str(exe+1) + "_case_" + str(cn) + "_patient_" + str(paciente))

            # bloque matriz después de las ejecuciones independiente, depende entonces si se vuelven a dividir xtrain, xval y xtest en las ejecuciones.  Antes, se repiten resultados.
            yTrain, yVal, yTest, xTrain_glucose, xTrain_Accel, xTrain_DeltaInsulin, xTrain_Insulin, xTrain_Insulin_lispro, xTrain_Insulin_lispro_regular, xTrain_Insulin_profiles, xTrain_Insulin_exp, xTrain_Insulin_comidasDeltas, xTrain_Insulin_comidasDeltas_profiles, xTrain_Insulin_comidasExp, xTrain_Insulin_comidasExp_lispro, xTrain_Insulin_comidasExp_profiles, xVal_glucose, xVal_Accel, xVal_DeltaInsulin, xVal_Insulin, xVal_Insulin_lispro, xVal_Insulin_lispro_regular, xVal_Insulin_profiles, xVal_Insulin_exp, xVal_Insulin_comidasDeltas, xVal_Insulin_comidasDeltas_profiles, xVal_Insulin_comidasExp, xVal_Insulin_comidasExp_lispro, xVal_Insulin_comidasExp_profiles, xTest_glucose, xTest_Accel, xTest_DeltaInsulin, xTest_Insulin, xTest_Insulin_lispro, xTest_Insulin_lispro_regular, xTest_Insulin_profiles, xTest_Insulin_exp, xTest_Insulin_comidasDeltas, xTest_Insulin_comidasDeltas_profiles, xTest_Insulin_comidasExp, xTest_Insulin_comidasExp_lispro, xTest_Insulin_comidasExp_profiles = bloque_matriz(
                cn, ac, path_full_dataset_processed, paciente, posicion_glucosa, datosProcesados, path_models_saved)

            #cargar=0          #to save the model first
            bloque_guardar_modelos_experimentos(cargar, units, epochs, batch_size, adam_opt, path_models_saved, cn,
                                                paciente,
                                                exe, yTrain, yVal, yTest, xTrain_glucose, xTrain_Accel,
                                                xTrain_DeltaInsulin, xTrain_Insulin, xTrain_Insulin_lispro,
                                                xTrain_Insulin_lispro_regular, xTrain_Insulin_profiles,
                                                xTrain_Insulin_exp, xTrain_Insulin_comidasDeltas,
                                                xTrain_Insulin_comidasDeltas_profiles, xTrain_Insulin_comidasExp,
                                                xTrain_Insulin_comidasExp_lispro, xTrain_Insulin_comidasExp_profiles,
                                                xVal_glucose, xVal_Accel, xVal_DeltaInsulin, xVal_Insulin,
                                                xVal_Insulin_lispro, xVal_Insulin_lispro_regular, xVal_Insulin_profiles,
                                                xVal_Insulin_exp, xVal_Insulin_comidasDeltas,
                                                xVal_Insulin_comidasDeltas_profiles, xVal_Insulin_comidasExp,
                                                xVal_Insulin_comidasExp_lispro, xVal_Insulin_comidasExp_profiles,
                                                xTest_glucose, xTest_Accel, xTest_DeltaInsulin, xTest_Insulin,
                                                xTest_Insulin_lispro, xTest_Insulin_lispro_regular,
                                                xTest_Insulin_profiles, xTest_Insulin_exp, xTest_Insulin_comidasDeltas,
                                                xTest_Insulin_comidasDeltas_profiles, xTest_Insulin_comidasExp,
                                                xTest_Insulin_comidasExp_lispro, xTest_Insulin_comidasExp_profiles)
            #cargar=1       #to load the model after
            listaScores, scores_exp_1, scores_exp_2, scores_exp_3, scores_exp_4, scores_exp_5, scores_exp_6, scores_exp_7  = bloque_cargar_modelos_experimentos(
                                                  cargar, listaScores, scores_exp_1, scores_exp_2, scores_exp_3, scores_exp_4, scores_exp_5, scores_exp_6, scores_exp_7, units, epochs, batch_size, adam_opt, path_models_saved,
                                                  cn, paciente, exe, yTrain, yVal, yTest, xTrain_glucose, xTrain_Accel,
                                                  xTrain_DeltaInsulin, xTrain_Insulin, xTrain_Insulin_lispro,
                                                  xTrain_Insulin_lispro_regular, xTrain_Insulin_profiles,
                                                  xTrain_Insulin_exp, xTrain_Insulin_comidasDeltas,
                                                  xTrain_Insulin_comidasDeltas_profiles, xTrain_Insulin_comidasExp,
                                                  xTrain_Insulin_comidasExp_lispro, xTrain_Insulin_comidasExp_profiles,
                                                  xVal_glucose, xVal_Accel, xVal_DeltaInsulin, xVal_Insulin,
                                                  xVal_Insulin_lispro, xVal_Insulin_lispro_regular,
                                                  xVal_Insulin_profiles, xVal_Insulin_exp, xVal_Insulin_comidasDeltas,
                                                  xVal_Insulin_comidasDeltas_profiles, xVal_Insulin_comidasExp,
                                                  xVal_Insulin_comidasExp_lispro, xVal_Insulin_comidasExp_profiles,
                                                  xTest_glucose, xTest_Accel, xTest_DeltaInsulin, xTest_Insulin,
                                                  xTest_Insulin_lispro, xTest_Insulin_lispro_regular,
                                                  xTest_Insulin_profiles, xTest_Insulin_exp,
                                                  xTest_Insulin_comidasDeltas, xTest_Insulin_comidasDeltas_profiles,
                                                  xTest_Insulin_comidasExp, xTest_Insulin_comidasExp_lispro,
                                                  xTest_Insulin_comidasExp_profiles)



        # print('scores_exp_1: ', np.mean(scores_exp_1))
        # print(' -  Valor mínimo: ', np.amin(scores_exp_1))
        # print(' - Valor máximo: ', np.amax(scores_exp_1))

        # print('scores_exp_2: ', np.mean(scores_exp_2))
        # print(' -  Valor mínimo: ', np.amin(scores_exp_2))
        # print(' - Valor máximo: ', np.amax(scores_exp_2))

        # print('scores_exp_3: ', np.mean(scores_exp_3))
        # print(' -  Valor mínimo: ', np.amin(scores_exp_3))
        # print(' - Valor máximo: ', np.amax(scores_exp_3))

        # print('scores_exp_4: ', np.mean(scores_exp_4))
        # print(' -  Valor mínimo: ', np.amin(scores_exp_4))
        # print(' - Valor máximo: ', np.amax(scores_exp_4))

        # print('scores_exp_5: ', np.mean(scores_exp_5))
        # print(' -  Valor mínimo: ', np.amin(scores_exp_5))
        # print(' - Valor máximo: ', np.amax(scores_exp_5))

        # print('scores_exp_6: ', np.mean(scores_exp_6))
        # print(' -  Valor mínimo: ', np.amin(scores_exp_6))
        # print(' - Valor máximo: ', np.amax(scores_exp_6))

        # print('scores_exp_7: ', np.mean(scores_exp_7))
        # print(' -  Valor mínimo: ', np.amin(scores_exp_7))
        # print(' - Valor máximo: ', np.amax(scores_exp_7))

        listaScores.append([np.mean(scores_exp_1), np.mean(scores_exp_2), np.mean(scores_exp_3), np.mean(scores_exp_4), np.mean(scores_exp_5), np.mean(scores_exp_6), np.mean(scores_exp_7)])
        listaScores.append([np.amin(scores_exp_1), np.amin(scores_exp_2), np.amin(scores_exp_3), np.amin(scores_exp_4), np.amin(scores_exp_5), np.amin(scores_exp_6), np.amin(scores_exp_7)])
        listaScores.append([np.amax(scores_exp_1), np.amax(scores_exp_2), np.amax(scores_exp_3), np.amax(scores_exp_4), np.amax(scores_exp_5), np.amax(scores_exp_6), np.amax(scores_exp_7)])
        execution_list.append('mean_' + str(execution_number) + "_case_" + str(cn) + "_patient_" + str(paciente))
        execution_list.append('min_' + str(execution_number) + "_case_" + str(cn) + "_patient_" + str(paciente))
        execution_list.append('max_' + str(execution_number) + "_case_" + str(cn) + "_patient_" + str(paciente))

        #print(listaScores)
        #print(execution_list)
        df = pd.DataFrame(np.array(listaScores), columns=['score_exp_1', 'score_exp_2', 'score_exp_3', 'score_exp_4', 'score_exp_5', 'score_exp_6', 'score_exp_7'], index=execution_list)
        #print(df)
        path_scores = path_scores_dataset_processed[paciente - 1]
        df.to_csv(path_scores, index=True)

