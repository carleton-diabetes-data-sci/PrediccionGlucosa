import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate


def crear_boxplot_paciente(cn, en, path_boxplot, paciente, file_score):
    print("---BOXPLOT: BOXPLOT CON RESULTADOS DE PACIENTE 00" + str(paciente) + " EN EL CASO 0")
    if(paciente==1):
        path = path_boxplot[2]
    elif(paciente==2):
        path = path_boxplot[3]
    elif(paciente==4):
        path = path_boxplot[4]
    elif(paciente==6):
        path = path_boxplot[5]
    elif(paciente==7):
        path = path_boxplot[6]
    elif(paciente==8):
        path = path_boxplot[7]

    print(file_score)
    old_columns = list(file_score.columns)
    new_columns = ['0', '1', '2', '3', '4', '5', '6', '7']
    col_dict = dict(zip(old_columns, new_columns))
    file_score.rename(columns=col_dict, inplace=True)

    ax = sns.boxplot(data=file_score, width=0.3)
    ax.set_title('70 scores of patient 00' + str(paciente) + ' by experiment number')
    ax.set_xlabel("Experiment number")
    ax.set_ylabel("Scores")
    ax.set_ylim(0,2)

    plt.savefig(path)
    # show plot
    plt.show()



def crear_boxplot_pacientes(cn, en, path_scores_dataset_processed, path_boxplot, pacientes):
    print("--BOXPLOT: BOXPLOT CON RESULTADOS DE PACIENTES EN CASO 0")
    path_table = path_boxplot[0]  # saved table with raw scores of relevant patients together
    path = path_boxplot[1]  # boxplot save for relevant patients

    files_scores_df = pd.DataFrame()

    for paciente in pacientes:
        path_scores = path_scores_dataset_processed[paciente - 1]
        file_score = pd.read_csv(path_scores)
        file_score = file_score.iloc[0:en]
        # print(file_score)
        crear_boxplot_paciente(cn, en, path_boxplot, paciente, file_score)  # create boxplot for all patients
        files_scores_df = files_scores_df.append(file_score)


    files_scores_df.to_csv(path_table, index=False)
    old_columns = list(files_scores_df.columns)
    new_columns = ['0', '1', '2', '3', '4', '5', '6', '7']
    col_dict = dict(zip(old_columns, new_columns))
    files_scores_df.rename(columns=col_dict, inplace=True)

    ax = sns.boxplot(data=files_scores_df, width=0.3)
    ax.set_title("420 scores of relevant patients by experiment number")
    ax.set_xlabel("Experiment number")
    ax.set_ylabel("Scores")
    ax.set_ylim(0,2)

    plt.savefig(path)
    # show plot
    plt.show()







def crear_boxplot_experimento(cn, en, path_boxplot, try_number, exp_df):
    print("---BOXPLOT: BOXPLOT CON RESULTADOS DE EXPERIMENTO " + str(try_number) + " EN EL CASO 0")
    if (try_number == 1):
        path = path_boxplot[17]
    elif (try_number == 2):
        path = path_boxplot[18]
    elif (try_number == 3):
        path = path_boxplot[19]
    elif (try_number == 4):
        path = path_boxplot[20]
    elif (try_number == 5):
        path = path_boxplot[21]
    elif (try_number == 6):
        path = path_boxplot[22]
    elif (try_number == 7):
        path = path_boxplot[23]

    df = exp_df
    old_columns = list(df.columns)
    new_columns = ['', '001', '002', '004', '006', '007', '008']
    col_dict = dict(zip(old_columns, new_columns))
    df.rename(columns=col_dict, inplace=True)

    ax = sns.boxplot(data=df, width=0.3)
    ax.set_title('60 scores of try number ' + str(try_number) + ' by patient number')
    ax.set_xlabel("Patient number")
    ax.set_ylabel("Scores")
    ax.set_ylim(0,2)

    plt.savefig(path)
    # show plot
    plt.show()





def crear_bbboxplot_experimentos(cn, en, path_scores_dataset_processed, path_boxplot, pacientes):  #sin terminar
    print("--BOXPLOT: BOXPLOT CON RESULTADOS EN CASO 0")
    path_table = path_boxplot[8]
    path = path_boxplot[16]
    files_scores_df = pd.DataFrame()
    try_numbers = [x + 1 for x in range(7)]
    f_df = pd.DataFrame()

    patient_count = 0
    for paciente in pacientes:
        patient_count = patient_count + 1
        path_scores = path_scores_dataset_processed[paciente - 1]
        file_score = pd.read_csv(path_scores)
        file_score = file_score.iloc[0:en]
        # print(file_score)
        # crear_boxplot_paciente(cn, en, path_boxplot, paciente, file_score)
        files_scores_df = files_scores_df.append(file_score)

        if (patient_count == 1):  # en la columna de titulos. Para el primer paciente, se cogen los titulos de las 10 ejecuciones y se sustituye el nombre paciente por try_number
            new_name_list = []
            old_name_list = file_score["Unnamed: 0"].values
            for n in old_name_list:
                new_name = n.replace("patient", "_by_try_number")  # change patient by try_number
                new_name = new_name[:-1] + "*"  # delete the old patient number

                new_name_list.append(new_name)
            f_df['BY_TRY_NUMBER'] = new_name_list

        for try_number in try_numbers:
            print("--BOXPLOT: TABLA CON RESULTADOS DE PACIENTE " + str(paciente) + " Y EXPERIMENTO " + str(
                try_number) + " EN CASO 0")
            # print(try_number)
            name_list = f_df['BY_TRY_NUMBER'].values

            if (patient_count == 1):
                last_name_list = []
                # print(name_list)
                for n in name_list:
                    name = n.replace("*", str(try_number))
                    last_name_list.append(name)
                f_df["name"] = last_name_list

                # print(last_name_list)

            val = file_score["score_exp_" + str(try_number)].values
            f_df["score_patient_00" + str(paciente)] = val
            # if (patient_count == len(try_numbers) - 1):
            # print(tabulate(f_df, headers='keys', tablefmt='psql'))

            # f_df = f_df.drop(columns=['BY_TRY_NUMBER'], axis=1, inplace=True)
            path_experiment_scores = path_boxplot[try_number + 8]  # PATH
            f_df.to_csv(path_experiment_scores, index=False)

            print(tabulate(f_df, headers='keys', tablefmt='psql'))

            # each try_number, it changes into another df
            # crear_boxplot_experimentos(cn, en, path_boxplot, try_number, exp_df)

    # print(files_scores_df)

    # f_df["name"] = file_score[].values


        
        files_scores_df.to_csv(path_table, index=False)
        old_columns = list(files_scores_df.columns)
        new_columns = ['001', '002', '004', '006', '007', '008']
        col_dict = dict(zip(old_columns, new_columns))
        files_scores_df.rename(columns=col_dict, inplace=True)

        ax = sns.boxplot(data=files_scores_df, width=0.3)
        ax.set_title("420 scores of try numbers by patient number")
        ax.set_xlabel("Patient number")
        ax.set_ylabel("Scores")

        plt.savefig(path)
        # show plot
        plt.show()


def crear_boxplot_experimentos(cn, en, path_scores_dataset_processed, path_boxplot, pacientes):
    print("--BOXPLOT: BOXPLOT CON RESULTADOS EN CASO 0")
    path_table = path_boxplot[8]
    path = path_boxplot[16]
    files_scores_df = pd.DataFrame()
    try_numbers = [x + 1 for x in range(7)]
    f_df = pd.DataFrame()

    for paciente in pacientes:
        path_scores = path_scores_dataset_processed[paciente - 1]
        col = ["Patient 00" + str(paciente),
               "score_patient_00" + str(paciente) + "_exp_1",
               "score_patient_00" + str(paciente) + "_exp_2",
               "score_patient_00" + str(paciente) + "_exp_3",
               "score_patient_00" + str(paciente) + "_exp_4",
               "score_patient_00" + str(paciente) + "_exp_5",
               "score_patient_00" + str(paciente) + "_exp_6",
               "score_patient_00" + str(paciente) + "_exp_7"]
        file_score = pd.read_csv(path_scores, names=col)
        file_score = file_score.iloc[1:en+1]           #delete last 3 columns  #or 0:en if head it is different
        #crear_boxplot_paciente(cn, en, path_boxplot, paciente, file_score)
        files_scores_df = pd.concat([files_scores_df, file_score], axis=1)
    print(tabulate(files_scores_df, headers='keys', tablefmt='psql'))

    for try_n in try_numbers:
        selected_columns = ["Patient 001",
                            "score_patient_001_exp_" + str(try_n),
                            "score_patient_002_exp_" + str(try_n),
                            "score_patient_004_exp_" + str(try_n),
                            "score_patient_006_exp_" + str(try_n),
                            "score_patient_007_exp_" + str(try_n),
                            "score_patient_008_exp_" + str(try_n)
        ]
        last_name_list = []
        old_name_list = files_scores_df["Patient 001"].values
        #print(old_name_list)
        for n in old_name_list:
            new_name = n.replace("patient", "try_number")  # change patient by try_number
            new_name = new_name[:-1] + "*"  # delete the old patient number
            new_name = new_name.replace("*", str(try_n))
            #print(new_name)
            last_name_list.append(new_name)
        files_scores_df["Patient 001"] = last_name_list
        print(files_scores_df.loc[:, selected_columns])
        exp_df = files_scores_df.loc[:, selected_columns]
        path_experiment_scores = path_boxplot[try_n + 8]  # PATH
        exp_df.to_csv(path_experiment_scores, index=False)
        crear_boxplot_experimento(cn, en, path_boxplot, try_n, exp_df)

