import pandas as pd
import numpy as np



def media_resultados_pacientes(cn, path_scores_dataset_processed, pacientes):
    print("--MEAN_SCORE: LA MEDIA DE RESULTADOS DE DIFERENTES PACIENTES EN CASO 0")
    #mean_index_list = ["mean_patient_1", "mean_patient_2", "mean_patient_4", "mean_patient_6", "mean_patient_7", "mean_patient_8"]
    #min_index_list = ["min_patient_1", "mean_patient_2", "mean_patient_4", "mean_patient_6", "mean_patient_7", "mean_patient_8"]
    #max_index_list = ["max_patient_1", "mean_patient_2", "mean_patient_4", "mean_patient_6", "mean_patient_7","mean_patient_8"]
    #mean_index_list.append('mean_mean_relevant_patients_case_' + str(cn))
    #min_index_list.append('min_min_relevant_patients_case_' + str(cn))
    #max_index_list.append('max_max_relevant_patients_case_' + str(cn))

    mean_scores_list = []
    mean_scores_exp_1 = []
    mean_scores_exp_2 = []
    mean_scores_exp_3 = []
    mean_scores_exp_4 = []
    mean_scores_exp_5 = []
    mean_scores_exp_6 = []
    mean_scores_exp_7 = []

    min_scores_list = []
    min_scores_exp_1 = []
    min_scores_exp_2 = []
    min_scores_exp_3 = []
    min_scores_exp_4 = []
    min_scores_exp_5 = []
    min_scores_exp_6 = []
    min_scores_exp_7 = []

    max_scores_list = []
    max_scores_exp_1 = []
    max_scores_exp_2 = []
    max_scores_exp_3 = []
    max_scores_exp_4 = []
    max_scores_exp_5 = []
    max_scores_exp_6 = []
    max_scores_exp_7 = []

    #pacientes = [1, 2, 4, 6, 7, 8]         #Maybe put in configuration

    for paciente in pacientes:
        scores_exp_1 = []
        scores_exp_2 = []
        scores_exp_3 = []
        scores_exp_4 = []
        scores_exp_5 = []
        scores_exp_6 = []
        scores_exp_7 = []

        mean_score_list = []
        min_score_list = []
        max_score_list = []

        path_scores = path_scores_dataset_processed[paciente - 1]
        file_score = pd.read_csv(path_scores)
        print('paciente: ', paciente)
        print('Tamaño del csv de con los resultados de un paciente (en el caso 0: ', file_score.shape)

        mean_score_list = file_score.iloc[-3].values.tolist()  # mean row of a patient
        min_score_list = file_score.iloc[-2].values.tolist()  # min row of a patient
        max_score_list = file_score.iloc[-1].values.tolist()  # max row of a patient
        # print(mean_score_list)
        # print(min_score_list)
        # print(max_score_list)

        mean_scores_list.append(mean_score_list)
        min_scores_list.append(min_score_list)
        max_scores_list.append(max_score_list)

        mean_scores_exp_1.append(mean_score_list[1])
        mean_scores_exp_2.append(mean_score_list[2])
        mean_scores_exp_3.append(mean_score_list[3])
        mean_scores_exp_4.append(mean_score_list[4])
        mean_scores_exp_5.append(mean_score_list[5])
        mean_scores_exp_6.append(mean_score_list[6])
        mean_scores_exp_7.append(mean_score_list[7])

        min_scores_exp_1.append(min_score_list[1])
        min_scores_exp_2.append(min_score_list[2])
        min_scores_exp_3.append(min_score_list[3])
        min_scores_exp_4.append(min_score_list[4])
        min_scores_exp_5.append(min_score_list[5])
        min_scores_exp_6.append(min_score_list[6])
        min_scores_exp_7.append(min_score_list[7])

        max_scores_exp_1.append(max_score_list[1])
        max_scores_exp_2.append(max_score_list[2])
        max_scores_exp_3.append(max_score_list[3])
        max_scores_exp_4.append(max_score_list[4])
        max_scores_exp_5.append(max_score_list[5])
        max_scores_exp_6.append(max_score_list[6])
        max_scores_exp_7.append(max_score_list[7])

    mean_scores_list.append(['mean_mean_case_' + str(cn) + '_relevant_patients', np.mean(mean_scores_exp_1), np.mean(mean_scores_exp_2),np.mean(mean_scores_exp_3), np.mean(mean_scores_exp_4), np.mean(mean_scores_exp_5), np.mean(mean_scores_exp_6), np.mean(mean_scores_exp_7)])
    min_scores_list.append(['min_min_case_' + str(cn) +'_relevant_patients', np.amin(min_scores_exp_1), np.amin(min_scores_exp_2),np.amin(min_scores_exp_3), np.amin(min_scores_exp_4), np.amin(min_scores_exp_5), np.amin(min_scores_exp_6), np.amin(min_scores_exp_7)])
    max_scores_list.append(['max_max_case_' + str(cn) +'_relevant_patients', np.amax(max_scores_exp_1), np.amax(max_scores_exp_2), np.amax(max_scores_exp_3), np.amax(max_scores_exp_4), np.amax(max_scores_exp_5), np.amax(max_scores_exp_6), np.amax(max_scores_exp_7)])
    # mean_scores_list = str(mean_scores_list)[1:-1]        #in case we need to delete [ ]

    df_mean = pd.DataFrame(np.array(mean_scores_list), columns=['GLOBAL_MEAN', 'score_exp_1', 'score_exp_2', 'score_exp_3', 'score_exp_4','score_exp_5', 'score_exp_6', 'score_exp_7'])
    df_min = pd.DataFrame(np.array(min_scores_list), columns=['GLOBAL_MIN', 'score_exp_1', 'score_exp_2', 'score_exp_3', 'score_exp_4', 'score_exp_5', 'score_exp_6', 'score_exp_7'])
    df_max = pd.DataFrame(np.array(max_scores_list), columns=['GLOBAL_MAX', 'score_exp_1', 'score_exp_2', 'score_exp_3', 'score_exp_4','score_exp_5', 'score_exp_6', 'score_exp_7'])

    print(df_mean)
    #print(df_min)
    #print(df_max)

    path_mean_scores = path_scores_dataset_processed[9]  # the 9 element of the array is the mean_scores of relevant patients in Case 0.
    path_min_scores = path_scores_dataset_processed[10]  # the 10 element of the array is the mean_scores of relevant patients in Case 0.
    path_max_scores = path_scores_dataset_processed[11]  # the 11 of the array is the mean_scores of relevant patients in Case 0.

    df_mean.to_csv(path_mean_scores, index=False)
    df_min.to_csv(path_min_scores, index=False)
    df_max.to_csv(path_max_scores, index=False)