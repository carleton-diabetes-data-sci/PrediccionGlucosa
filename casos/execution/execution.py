import pandas as pd
import numpy as np

from casos.execution.model import ejecutaModeloSinPrint

from casos.matrices.matrices import bloque_matriz
from casos.matrices.separation import separar_x_y
from casos.matrices.separation import bloque_dividir_datos


def bloque_ejecucion(cn, pi, path_full_dataset_processed, path_scores_dataset_processed, execution_number, pacientes, posicion_glucosa):
    for paciente in pacientes:
        path_fichero_full_procesados = path_full_dataset_processed[paciente - 1]  # cambiar por path_gai_dataset_processed
        datosProcesados = pd.read_csv(path_fichero_full_procesados)
        print('paciente: ', paciente)
        print('Tamaño del csv de datos procesados gai previo a comida: ', datosProcesados.shape)

        print("MAIN: BLOQUE EJECUCIÓN...")
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

        for exe in range(execution_number):
            print('EJECUCION: ', exe)
            execution_list.append("execution_" + str(exe+1) + "_case_" + str(cn) + "_patient_" + str(paciente))

            x, y = bloque_matriz(path_full_dataset_processed, pacientes, posicion_glucosa)
            xTrain, xVal, xTest, yTrain, yVal, yTest = separar_x_y(x, y)
            xTrain_glucose, xTrain_Accel, xTrain_DeltaInsulin, xTrain_Insulin, xTrain_Insulin_lispro, xTrain_Insulin_lispro_regular, xTrain_Insulin_profiles, xTrain_Insulin_exp, xTrain_Insulin_comidasDeltas, xTrain_Insulin_comidasDeltas_profiles, xTrain_Insulin_comidasExp, xTrain_Insulin_comidasExp_lispro, xTrain_Insulin_comidasExp_profiles, xVal_glucose, xVal_Accel, xVal_DeltaInsulin, xVal_Insulin, xVal_Insulin_lispro, xVal_Insulin_lispro_regular, xVal_Insulin_profiles, xVal_Insulin_exp, xVal_Insulin_comidasDeltas, xVal_Insulin_comidasDeltas_profiles, xVal_Insulin_comidasExp, xVal_Insulin_comidasExp_lispro, xVal_Insulin_comidasExp_profiles, xTest_glucose, xTest_Accel, xTest_DeltaInsulin, xTest_Insulin, xTest_Insulin_lispro, xTest_Insulin_lispro_regular, xTest_Insulin_profiles, xTest_Insulin_exp, xTest_Insulin_comidasDeltas, xTest_Insulin_comidasDeltas_profiles, xTest_Insulin_comidasExp, xTest_Insulin_comidasExp_lispro, xTest_Insulin_comidasExp_profiles = bloque_dividir_datos(
                xTrain, xVal, xTest)

            # y_pred_exp_1, score_exp_1 = ejecutaModeloSinPrint(xTrain_DeltaInsulin, yTrain, xVal_DeltaInsulin, yVal, xTest_DeltaInsulin, yTest)
            # y_pred_exp_2, score_exp_2 = ejecutaModeloSinPrint(xTrain_Insulin, yTrain, xVal_Insulin, yVal, xTest_Insulin, yTest)
            # y_pred_exp_3, score_exp_3 = ejecutaModeloSinPrint(xTrain_Insulin_lispro, yTrain, xVal_Insulin_lispro, yVal, xTest_Insulin_lispro, yTest)
            # _pred_exp_4, score_exp_4 = ejecutaModeloSinPrint(xTrain_Insulin_comidasDeltas, yTrain, xVal_Insulin_comidasDeltas, yVal, xTest_Insulin_comidasDeltas, yTest)
            # y_pred_exp_5, score_exp_5 = ejecutaModeloSinPrint(xTrain_Insulin_comidasExp, yTrain, xVal_Insulin_comidasExp, yVal, xTest_Insulin_comidasExp, yTest)
            # y_pred_exp_6, score_exp_6 = ejecutaModeloSinPrint(xTrain_Insulin_comidasExp_lispro, yTrain, xVal_Insulin_comidasExp_lispro, yVal, xTest_Insulin_comidasExp_lispro, yTest)
            # y_pred_exp_7, score_exp_7 = ejecutaModeloSinPrint(xTrain_Insulin_comidasExp_profiles, yTrain, xVal_Insulin_comidasExp_profiles, yVal, xTest_Insulin_comidasExp_profiles, yTest)
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

            scores_exp_1.append(score_exp_1)
            scores_exp_2.append(score_exp_2)
            scores_exp_3.append(score_exp_3)
            scores_exp_4.append(score_exp_4)
            scores_exp_5.append(score_exp_5)
            scores_exp_6.append(score_exp_6)
            scores_exp_7.append(score_exp_7)

            listaScores.append(
                [score_exp_1, score_exp_2, score_exp_3, score_exp_4, score_exp_5, score_exp_6, score_exp_7])

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

        listaScores.append([np.mean(scores_exp_1), np.mean(scores_exp_2), np.mean(scores_exp_3), np.mean(scores_exp_4),
                            np.mean(scores_exp_5), np.mean(scores_exp_6), np.mean(scores_exp_7)])
        listaScores.append([np.amin(scores_exp_1), np.amin(scores_exp_2), np.amin(scores_exp_3), np.amin(scores_exp_4),
                            np.amin(scores_exp_5), np.amin(scores_exp_6), np.amin(scores_exp_7)])
        listaScores.append([np.amax(scores_exp_1), np.amax(scores_exp_2), np.amax(scores_exp_3), np.amax(scores_exp_4),
                            np.amax(scores_exp_5), np.amax(scores_exp_6), np.amax(scores_exp_7)])
        execution_list.append('mean_' + str(execution_number) + "_case_" + str(cn) + "_patient_" + str(paciente))
        execution_list.append('min_' + str(execution_number) + "_case_" + str(cn) + "_patient_" + str(paciente))
        execution_list.append('max_' + str(execution_number) + "_case_" + str(cn) + "_patient_" + str(paciente))

        df = pd.DataFrame(np.array(listaScores),
                          columns=['score_exp_1', 'score_exp_2', 'score_exp_3', 'score_exp_4', 'score_exp_5',
                                   'score_exp_6', 'score_exp_7'],
                          index=execution_list)
        print(df)
        path_scores = path_scores_dataset_processed[paciente - 1]
        df.to_csv(path_scores, index=True)

