import numpy as np
import pandas as pd


cn=0
pacientes=[1,2,4,6,7,8]
path_project = r'C:\Users\apula\PycharmProjects\PrediccionGlucosa'  # PATH


path_dataset_processed = path_project + r'\D1NAMO\processed_subset'  # PATH

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


print("--MEAN_SCORE: LA MEDIA DE RESULTADOS DE DIFERENTES PACIENTES EN CASO 0")
index_list = []

mean_index_list =["mean_patient_1", "mean_patient_2", "mean_patient_4", "mean_patient_6", "mean_patient_7", "mean_patient_8"]
min_index_list =["min_patient_1", "mean_patient_2", "mean_patient_4", "mean_patient_6", "mean_patient_7", "mean_patient_8"]
max_index_list =["max_patient_1", "mean_patient_2", "mean_patient_4", "mean_patient_6", "mean_patient_7", "mean_patient_8"]

mean_scores_list = []

mean_scores_exp_1=[]
mean_scores_exp_2=[]
mean_scores_exp_3=[]
mean_scores_exp_4=[]
mean_scores_exp_5=[]
mean_scores_exp_6=[]
mean_scores_exp_7=[]

min_scores_list = []

min_scores_exp_1=[]
min_scores_exp_2=[]
min_scores_exp_3=[]
min_scores_exp_4=[]
min_scores_exp_5=[]
min_scores_exp_6=[]
min_scores_exp_7=[]

max_scores_list = []

max_scores_exp_1=[]
max_scores_exp_2=[]
max_scores_exp_3=[]
max_scores_exp_4=[]
max_scores_exp_5=[]
max_scores_exp_6=[]
max_scores_exp_7=[]



pacientes = [1,2,4,6,7,8]
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

        mean_score_list = file_score.iloc[-3] # mean row of a patient
        min_score_list = file_score.iloc[-2]  # min row of a patient
        max_score_list = file_score.iloc[-1]  # max row of a patient

        #print(mean_score_list)
        #print(min_score_list)
        #print(max_score_list)
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

        #print(mean_scores_exp_1)

pcientes , paciente2...
mean_scores_list.append([mean_scores_exp_1, mean_scores_exp_2, mean_scores_exp_3, mean_scores_exp_4, mean_scores_exp_5, mean_scores_exp_6, mean_scores_exp_7, [np.mean(mean_scores_exp_1), np.mean(mean_scores_exp_2), np.mean(mean_scores_exp_3), np.mean(mean_scores_exp_4), np.mean(mean_scores_exp_5),np.mean(mean_scores_exp_6), np.mean(mean_scores_exp_7)]])
mean_scores_list = str(mean_scores_list)[1:-1]

#mean_scores_list.append()
#min_scores_list.append([np.amin(min_scores_exp_1), np.amin(min_scores_exp_2), np.amin(min_scores_exp_3), np.amin(min_scores_exp_4), np.amin(min_scores_exp_5),np.amin(min_scores_exp_6), np.amin(min_scores_exp_7)])
#max_scores_list.append([np.amax(max_scores_exp_1), np.amax(max_scores_exp_2), np.amax(max_scores_exp_3), np.amax(max_scores_exp_4), np.amax(max_scores_exp_5),np.amax(max_scores_exp_6), np.amax(max_scores_exp_7)])

print("p", mean_scores_list)



min_scores_list = [[1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1]
               ]
max_scores_list = [[1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1]
               ]

mean_index_list.append('mean_mean_relevant_patients_case_' + str(cn))
min_index_list.append('min_min_relevant_patients_case_' + str(cn))
max_index_list.append('max_max_relevant_patients_case_' + str(cn))

df_mean = pd.DataFrame(np.array(mean_scores_list), columns=['score_exp_1', 'score_exp_2', 'score_exp_3', 'score_exp_4', 'score_exp_5', 'score_exp_6', 'score_exp_7'], index=mean_index_list)
df_min = pd.DataFrame(np.array(min_scores_list), columns=['score_exp_1', 'score_exp_2', 'score_exp_3', 'score_exp_4', 'score_exp_5', 'score_exp_6', 'score_exp_7'], index=min_index_list)
df_max = pd.DataFrame(np.array(max_scores_list), columns=['score_exp_1', 'score_exp_2', 'score_exp_3', 'score_exp_4', 'score_exp_5', 'score_exp_6', 'score_exp_7'], index=max_index_list)

#print(df_mean)
#print(df_min)
#print(df_max)
path_mean_scores = path_scores_dataset_processed[9]  # the third last element of the array is the mean_scores of relevant patients in Case 0.
path_min_scores = path_scores_dataset_processed[10]  # the second last element of the array is the mean_scores of relevant patients in Case 0.
path_max_scores = path_scores_dataset_processed[11]  # the last element of the array is the mean_scores of relevant patients in Case 0.

df_mean.to_csv(path_mean_scores, index=True)
df_min.to_csv(path_min_scores, index=True)
df_max.to_csv(path_max_scores, index=True)

