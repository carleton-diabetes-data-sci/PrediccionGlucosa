import pandas as pd
import numpy as np



def media_resultados_pacientes(cn, path_scores_dataset_processed, pacientes):
    print("--MEAN_SCORE: LA MEDIA DE RESULTADOS DE DIFERENTES PACIENTES EN CASO 0")
    scores_list = []
    scores_pat_1 = []
    scores_pat_2 = []
    scores_pat_4 = []
    scores_pat_6 = []
    scores_pat_7 = []
    scores_pat_8 = []

    pacientes = [1,2,4,6,7,8]
    for paciente in pacientes:
        scores_exp_1 = []
        scores_exp_2 = []
        scores_exp_3 = []
        scores_exp_4 = []
        scores_exp_5 = []
        scores_exp_6 = []
        scores_exp_7 = []

        path_scores = path_scores_dataset_processed[paciente - 1]
        file_score = pd.read_csv(path_scores)
        print('paciente: ', paciente)
        print('Tamaño del csv de con los resultados de un paciente (en el caso 0: ', file_score.shape)

        #print(file_score)


        score_pat_1 = file_score['score_exp_1']
        score_pat_2 = file_score['score_exp_2']
        score_pat_4 = file_score['score_exp_3']
        score_pat_6 = file_score['score_exp_4']
        score_pat_7 = file_score['score_exp_5']
        score_pat_8 = file_score['score_exp_6']

        ###################poner score_list.append([score_exp_1....

        #print('score_pat_1: ', score_pat_1)
        #print('score_pat_2: ', score_pat_2)
        #print('score_pat_4: ', score_pat_4)
        #print('score_pat_6: ', score_pat_6)
        #print('score_pat_7: ', score_pat_7)
        #print('score_pat_8: ', score_pat_8)

        #scores_pat_1.append(score_pat_1)
        #scores_pat_2.append(score_pat_2)
        #scores_pat_4.append(score_pat_4)
        #scores_pat_6.append(score_pat_6)
        #scores_pat_7.append(score_pat_7)
        #scores_pat_8.append(score_pat_8)

        index_list.append('mean_patient_' + str(paciente) + "_case_" + str(cn))
        scores_list.append([score_pat_1, score_pat_2, score_pat_4, score_pat_6, score_pat_7, score_pat_8])

        #scores_list.append([score_pat_1, score_pat_2, score_pat_4, score_pat_6, score_pat_7, score_pat_8])

    print('scores_pat_1: ', np.mean(scores_pat_1))
    print(' -  Valor mínimo: ', np.amin(scores_pat_1))
    print(' - Valor máximo: ', np.amax(scores_pat_1))

    print('scores_pat_2: ', np.mean(scores_pat_2))
    print(' -  Valor mínimo: ', np.amin(scores_pat_2))
    print(' - Valor máximo: ', np.amax(scores_pat_2))

    print('scores_pat_4: ', np.mean(scores_pat_4))
    print(' -  Valor mínimo: ', np.amin(scores_pat_4))
    print(' - Valor máximo: ', np.amax(scores_pat_4))

    print('scores_pat_6: ', np.mean(scores_pat_6))
    print(' -  Valor mínimo: ', np.amin(scores_pat_6))
    print(' - Valor máximo: ', np.amax(scores_pat_6))

    print('scores_pat_7: ', np.mean(scores_pat_7))
    print(' -  Valor mínimo: ', np.amin(scores_pat_7))
    print(' - Valor máximo: ', np.amax(scores_pat_7))

    print('scores_pat_8: ', np.mean(scores_pat_8))
    print(' -  Valor mínimo: ', np.amin(scores_pat_8))
    print(' - Valor máximo: ', np.amax(scores_pat_8))


    scores_list.append([np.mean(scores_pat_1), np.mean(scores_pat_2), np.mean(scores_pat_4), np.mean(scores_pat_5), np.mean(scores_pat_7), np.mean(scores_pat_8)])
    scores_list.append([np.amin(scores_pat_1), np.amin(scores_pat_2), np.amin(scores_pat_4), np.amin(scores_pat_6), np.amin(scores_pat_7), np.amin(scores_pat_8)])
    scores_list.append([np.amax(scores_pat_1), np.amax(scores_pat_2), np.amax(scores_pat_4), np.amax(scores_pat_6), np.amax(scores_pat_7), np.amax(scores_pat_8)])
    index_list.append('mean_patient_' + str(paciente) + "_case_" + str(cn))
    index_list.append('min_patient_' + str(paciente) + "_case_" + str(cn))
    index_list.append('max_patient_' + str(paciente) + "_case_" + str(cn))



    df = pd.DataFrame(np.array(scores_list),
                      columns=['score_exp_1', 'score_exp_2', 'score_exp_3', 'score_exp_4', 'score_exp_5',
                               'score_exp_6', 'score_exp_7'],
                      index=index_list)
    print(df)
    path_scores = path_scores_dataset_processed[9]      #the last element of the array is the mean_scores of relevant patients in Case 0.
    df.to_csv(path_scores, index=True)
