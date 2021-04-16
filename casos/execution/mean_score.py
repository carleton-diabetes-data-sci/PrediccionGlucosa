import pandas as pd



def media_resultados_pacientes(path_scores_dataset_processed, pacientes):
    print("--MEAN_SCORE: LA MEDIA DE RESULTADOS DE DIFERENTES PACIENTES EN CASO 0")
    for paciente in pacientes:
        path_scores = path_scores_dataset_processed[paciente - 1]
        file_score = pd.read_csv(path_scores)
        print('paciente: ', paciente)
        print('Tamaño del csv de con los resultados de un paciente (en el caso 0: ', file_score.shape)

        print(file_score)