import numpy as np
import pandas as pd


execution_number = 10
execution_list = []

scores_exp_1 = []
scores_exp_2 = []
scores_exp_3 = []
scores_exp_4 = []
scores_exp_5 = []
scores_exp_6 = []
scores_exp_7 = []
listaScores = []

#paciente='1'
#cn = '0'
for x in range(execution_number):
        print('EJECUCION: ', x)
        execution_list.append("execution_" + str(x+1) + "_case_" + str(cn)+ "_patient_" + str(paciente))

        y_pred_exp_1, score_exp_1 = 1,1+x
        y_pred_exp_2, score_exp_2 = 1,2+x
        y_pred_exp_3, score_exp_3 = 1,3+x
        y_pred_exp_4, score_exp_4 = 1,4+x
        y_pred_exp_5, score_exp_5 = 1,5+x
        y_pred_exp_6, score_exp_6 = 1,6+x
        y_pred_exp_7, score_exp_7 = 1,7+x

        scores_exp_1.append(score_exp_1)
        scores_exp_2.append(score_exp_2)
        scores_exp_3.append(score_exp_3)
        scores_exp_4.append(score_exp_4)
        scores_exp_5.append(score_exp_5)
        scores_exp_6.append(score_exp_6)
        scores_exp_7.append(score_exp_7)

        listaScores.append([score_exp_1, score_exp_2, score_exp_3, score_exp_4, score_exp_5, score_exp_6, score_exp_7])

#print('scores_exp_1: ', np.mean(scores_exp_1))
#print(' -  Valor mínimo: ', np.amin(scores_exp_1))
#print(' - Valor máximo: ', np.amax(scores_exp_1))

#print('scores_exp_2: ', np.mean(scores_exp_2))
#print(' -  Valor mínimo: ', np.amin(scores_exp_2))
#print(' - Valor máximo: ', np.amax(scores_exp_2))

#print('scores_exp_3: ', np.mean(scores_exp_3))
#print(' -  Valor mínimo: ', np.amin(scores_exp_3))
#print(' - Valor máximo: ', np.amax(scores_exp_3))

#print('scores_exp_4: ', np.mean(scores_exp_4))
#print(' -  Valor mínimo: ', np.amin(scores_exp_4))
#print(' - Valor máximo: ', np.amax(scores_exp_4))

#print('scores_exp_5: ', np.mean(scores_exp_5))
#print(' -  Valor mínimo: ', np.amin(scores_exp_5))
#print(' - Valor máximo: ', np.amax(scores_exp_5))

#print('scores_exp_6: ', np.mean(scores_exp_6))
#print(' -  Valor mínimo: ', np.amin(scores_exp_6))
#print(' - Valor máximo: ', np.amax(scores_exp_6))

#print('scores_exp_7: ', np.mean(scores_exp_7))
#print(' -  Valor mínimo: ', np.amin(scores_exp_7))
#print(' - Valor máximo: ', np.amax(scores_exp_7))

listaScores.append([np.mean(scores_exp_1), np.mean(scores_exp_2), np.mean(scores_exp_3), np.mean(scores_exp_4), np.mean(scores_exp_5),np.mean(scores_exp_6), np.mean(scores_exp_7)])
listaScores.append([np.amin(scores_exp_1), np.amin(scores_exp_2), np.amin(scores_exp_3), np.amin(scores_exp_4), np.amin(scores_exp_5),np.amin(scores_exp_6), np.amin(scores_exp_7)])
listaScores.append([np.amax(scores_exp_1), np.amax(scores_exp_2), np.amax(scores_exp_3), np.amax(scores_exp_4), np.amax(scores_exp_5),np.amax(scores_exp_6), np.amax(scores_exp_7)])
execution_list.append('mean_'+ str(execution_number) + "_case_" + str(cn) + "_patient_" + str(paciente))
execution_list.append('min_'+ str(execution_number) + "_case_" + str(cn) + "_patient_" + str(paciente))
execution_list.append('max_'+ str(execution_number) + "_case_" + str(cn) + "_patient_" + str(paciente))

df = pd.DataFrame(np.array(listaScores),
                  columns=['score_exp_1', 'score_exp_2', 'score_exp_3', 'score_exp_4', 'score_exp_5', 'score_exp_6', 'score_exp_7'],
                  index= execution_list)
print(df)

path_project = r'C:\Users\apula\PycharmProjects\PrediccionGlucosa'  # PATH

path_dataset_processed = path_project + r'\D1NAMO\processed_subset'  # PATH
path_scores = path_dataset_processed + r'\008\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_scores.csv'

df.to_csv(path_scores, index=True)
