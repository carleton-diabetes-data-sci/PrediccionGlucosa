import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def grafica_mean(df, path):
    t_list=[]
    s_list=[]
    for index, row in df.iterrows():
        r = row.values.tolist()  #each row
        t = r[0]                 #title of the row
        s = r[1:]                #content of the row
        t_list.append(t)
        s_list.append(s)
        #print(index, t, s)


    # eje_x = np.arange(comidas_procesadas.shape[0])
    eje_x = list(range(1, 8))
    print(len(eje_x))

    fig, ax = plt.subplots()
    ax.plot(eje_x, s_list[0], color='blue', label='001: ' + str(t_list[0]))
    ax.plot(eje_x, s_list[1], color='green', label='002: ' + str(t_list[1]))
    ax.plot(eje_x, s_list[2], color='red', label='004: ' + str(t_list[2]))
    ax.plot(eje_x, s_list[3], color='cyan', label='006: ' + str(t_list[3]))
    ax.plot(eje_x, s_list[4], color='pink', label='007: ' + str(t_list[4]))
    ax.plot(eje_x, s_list[5], color='yellow', label='008: ' + str(t_list[5]))
    ax.plot(eje_x, s_list[6], color='black', label='Mean: ' + str(t_list[6]))

    #ax.plot(eje_x, df_mean_scores[2], color='blue', label='Patient 3 mean')
    plt.title('Mean scores graph')
    plt.xlabel('Experiment number')
    plt.ylabel('Score')
    leg = ax.legend()
    plt.savefig(path)
    plt.show()


def grafica_min(df, path):
    t_list=[]
    s_list=[]
    for index, row in df.iterrows():
        r = row.values.tolist()  #each row
        t = r[0]                 #title of the row
        s = r[1:]                #content of the row
        t_list.append(t)
        s_list.append(s)
        #print(index, t, s)


    # eje_x = np.arange(comidas_procesadas.shape[0])
    eje_x = list(range(1, 8))
    print(len(eje_x))

    fig, ax = plt.subplots()
    ax.plot(eje_x, s_list[0], color='blue', label='001: ' + str(t_list[0]))
    ax.plot(eje_x, s_list[1], color='green', label='002: ' + str(t_list[1]))
    ax.plot(eje_x, s_list[2], color='red', label='004: ' + str(t_list[2]))
    ax.plot(eje_x, s_list[3], color='cyan', label='006: ' + str(t_list[3]))
    ax.plot(eje_x, s_list[4], color='pink', label='007: ' + str(t_list[4]))
    ax.plot(eje_x, s_list[5], color='yellow', label='008: ' + str(t_list[5]))
    ax.plot(eje_x, s_list[6], color='black', label='Mean: ' + str(t_list[6]))

    #ax.plot(eje_x, df_mean_scores[2], color='blue', label='Patient 3 mean')
    plt.title('Min scores graph')
    plt.xlabel('Experiment number')
    plt.ylabel('Score')
    leg = ax.legend()
    plt.savefig(path)
    plt.show()


def grafica_max(df, path):
    t_list=[]
    s_list=[]
    for index, row in df.iterrows():
        r = row.values.tolist()  #each row
        t = r[0]                 #title of the row
        s = r[1:]                #content of the row
        t_list.append(t)
        s_list.append(s)
        #print(index, t, s)


    # eje_x = np.arange(comidas_procesadas.shape[0])
    eje_x = list(range(1, 8))
    print(len(eje_x))

    fig, ax = plt.subplots()
    ax.plot(eje_x, s_list[0], color='blue', label='001: ' + str(t_list[0]))
    ax.plot(eje_x, s_list[1], color='green', label='002: ' + str(t_list[1]))
    ax.plot(eje_x, s_list[2], color='red', label='004: ' + str(t_list[2]))
    ax.plot(eje_x, s_list[3], color='cyan', label='006: ' + str(t_list[3]))
    ax.plot(eje_x, s_list[4], color='pink', label='007: ' + str(t_list[4]))
    ax.plot(eje_x, s_list[5], color='yellow', label='008: ' + str(t_list[5]))
    ax.plot(eje_x, s_list[6], color='black', label='Mean: ' + str(t_list[6]))

    #ax.plot(eje_x, df_mean_scores[2], color='blue', label='Patient 3 mean')
    plt.title('Max scores graph')
    plt.xlabel('Experiment number')
    plt.ylabel('Score')
    leg = ax.legend()
    plt.savefig(path)
    plt.show()


def crear_grafica_media_resultados_pacientes(cn, path_scores_dataset_processed, pacientes):
    print("--MEAN_SCORE_GRAPH: LA GRÁFICA CON LA MEDIA DE RESULTADOS DE DIFERENTES PACIENTES EN CASO 0")
    path_mean_scores = path_scores_dataset_processed[9]  # the 9 element of the array is the mean_scores of relevant patients in Case 0.
    path_min_scores = path_scores_dataset_processed[10]  # the 10 element of the array is the mean_scores of relevant patients in Case 0.
    path_max_scores = path_scores_dataset_processed[11]  # the 11 of the array is the mean_scores of relevant patients in Case 0.

    df_mean_scores = pd.read_csv(path_mean_scores)
    print('Tamaño del csv de con la media de todos los pacientes (en el caso 0): ', df_mean_scores.shape)
    df_min_scores = pd.read_csv(path_min_scores)
    print('Tamaño del csv de con los mínimos de todos los pacientes (en el caso 0): ', df_min_scores.shape)
    df_max_scores = pd.read_csv(path_max_scores)
    print('Tamaño del csv de con los máximos de todos los pacientes (en el caso 0): ', df_max_scores.shape)

    path_mean_scores_graph = path_scores_dataset_processed[12]  # the third last element of the array is the mean_scores_graph of relevant patients in Case 0.
    path_min_scores_graph = path_scores_dataset_processed[13]  # the second last element of the array is the mean_scores_graph of relevant patients in Case 0.
    path_max_scores_graph = path_scores_dataset_processed[14]  # the last element of the array is the mean_scores_graph of relevant patients in Case 0.

    grafica_mean(df_mean_scores, path_mean_scores_graph)
    grafica_min(df_min_scores, path_min_scores_graph)
    grafica_max(df_max_scores, path_max_scores_graph)

