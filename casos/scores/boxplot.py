import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def crear_boxplot_paciente(cn, en, path_scores_dataset_processed, paciente, file_score):
    print("---BOXPLOT: BOXPLOT CON RESULTADOS DE PACIENTE 00" + str(paciente) + " EN EL CASO 0")
    if(paciente==1):
        path = path_scores_dataset_processed[17]
    elif(paciente==2):
        path = path_scores_dataset_processed[18]
    elif(paciente==4):
        path = path_scores_dataset_processed[19]
    elif(paciente==6):
        path = path_scores_dataset_processed[20]
    elif(paciente==7):
        path = path_scores_dataset_processed[21]
    elif(paciente==8):
        path = path_scores_dataset_processed[22]

    df=file_score
    old_columns = list(df.columns)
    new_columns = ['0', '1', '2', '3', '4', '5', '6', '7']
    col_dict = dict(zip(old_columns, new_columns))
    df.rename(columns=col_dict, inplace=True)

    ax = sns.boxplot(data=df, width=0.3)
    ax.set_title('70 scores of patient 00' + str(paciente) + ' by experiment number')
    ax.set_xlabel("Experiment number")
    ax.set_ylabel("Scores")

    plt.savefig(path)
    # show plot
    plt.show()


def crear_boxplot(cn, en, path_scores_dataset_processed, pacientes):
    print("--BOXPLOT: BOXPLOT CON RESULTADOS DE PACIENTES EN CASO 0")
    path=path_scores_dataset_processed[16]                #boxplot save for relevant patients
    path_table=path_scores_dataset_processed[15]          #saved table with raw scores of relevant patients together

    df = pd.DataFrame()

    for paciente in pacientes:
        path_scores = path_scores_dataset_processed[paciente - 1]
        file_score = pd.read_csv(path_scores)
        file_score = file_score.iloc[0:en]
        #print(file_score)
        crear_boxplot_paciente(cn, en, path_scores_dataset_processed, paciente, file_score)
        df = df.append(file_score)

    #print(df)
    df.to_csv(path_table, index=False)
    old_columns = list(df.columns)
    new_columns = ['0', '1', '2', '3', '4', '5', '6', '7']
    col_dict = dict(zip(old_columns, new_columns))
    df.rename(columns=col_dict, inplace=True)

    ax = sns.boxplot(data=df, width=0.3)
    ax.set_title("420 scores of relevant patients by experiment number")
    ax.set_xlabel("Experiment number")
    ax.set_ylabel("Scores")

    plt.savefig(path)
    # show plot
    plt.show()
