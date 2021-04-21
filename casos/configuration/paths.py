from casos.configuration.variables import parser_variables

def define_paths():
    cn, en, tn, ph, pn, pi, st, a, fw = parser_variables()

    print("--PATHS: DEFINIR PATHS")
    path_project = r'C:\Users\apula\PycharmProjects\PrediccionGlucosa'             #PATH
    path_glucose_acceleration_graphs = path_project + r'\casos\glucose_acceleration\graphs'            #PATH
    path_insulin_graphs = path_project + r'\casos\insulin\graphs'            #PATH
    path_food_graphs = path_project + r'\casos\food\graphs'            #PATH

    path_dataset = path_project + r'\D1NAMO\diabetes_subset'            #PATH
    path_glucose_dataset = [
                                path_dataset + r'\001\glucose.csv',
                                path_dataset + r'\002\glucose.csv',
                                path_dataset + r'\003\glucose.csv',
                                path_dataset + r'\004\glucose.csv',
                                path_dataset + r'\005\glucose.csv',
                                path_dataset + r'\006\glucose.csv',
                                path_dataset + r'\007\glucose.csv',
                                path_dataset + r'\008\glucose.csv',
                                path_dataset + r'\009\glucose.csv']            #PATH
    path_acceleration_dataset = [
                                path_dataset + r'\001\acceleration.csv',
                                path_dataset + r'\002\acceleration.csv',
                                path_dataset + r'\003\acceleration.csv',
                                path_dataset + r'\004\acceleration.csv',
                                path_dataset + r'\005\acceleration.csv',
                                path_dataset + r'\006\acceleration.csv',
                                path_dataset + r'\007\acceleration.csv',
                                path_dataset + r'\008\acceleration.csv',
                                path_dataset + r'\009\acceleration.csv']            #PATH  Does not exist
    path_insulin_dataset = [
                                path_dataset + r'\001\insulin.csv',
                                path_dataset + r'\002\insulin.csv',
                                path_dataset + r'\003\insulin.csv',
                                path_dataset + r'\004\insulin.csv',
                                path_dataset + r'\005\insulin.csv',
                                path_dataset + r'\006\insulin.csv',
                                path_dataset + r'\007\insulin.csv',
                                path_dataset + r'\008\insulin.csv',
                                path_dataset + r'\009\insulin.csv']            #PATH
    path_food_dataset = [
                                path_dataset + r'\001\food_dates_001.csv',
                                path_dataset + r'\002\food_dates_002.csv',
                                path_dataset + r'\003\food_dates_003.csv',
                                path_dataset + r'\004\food_dates_004.csv',
                                path_dataset + r'\005\food_dates_005.csv',
                                path_dataset + r'\006\food_dates_006.csv',
                                path_dataset + r'\007\food_dates_007.csv',
                                path_dataset + r'\008\food_dates_008.csv',
                                path_dataset + r'\009\food_dates_009.csv']            #PATH

    path_dataset_processed = path_project + r'\D1NAMO\processed_subset'  # PATH
    path_acceleration_dataset_processed = [                                                                                                         #se puede poner como datos sin procesar
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\001\Caso_'+ str(cn) + '_paciente_001_datosprocesadosAccel.csv',
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\002\Caso_'+ str(cn) + '_paciente_002_datosprocesadosAccel.csv',
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\003\Caso_'+ str(cn) + '_paciente_003_datosprocesadosAccel.csv',
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\004\Caso_'+ str(cn) + '_paciente_004_datosprocesadosAccel.csv',
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\005\Caso_'+ str(cn) + '_paciente_005_datosprocesadosAccel.csv',
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\006\Caso_'+ str(cn) + '_paciente_006_datosprocesadosAccel.csv',
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\007\Caso_'+ str(cn) + '_paciente_007_datosprocesadosAccel.csv',
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\008\Caso_'+ str(cn) + '_paciente_008_datosprocesadosAccel.csv',
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\009\Caso_'+ str(cn) + '_paciente_009_datosprocesadosAccel.csv']  # PATH
    path_insulin_dataset_processed = [
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\001\Caso_'+ str(cn) + '_paciente_001_insulina_procesada.csv',
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\002\Caso_'+ str(cn) + '_paciente_002_insulina_procesada.csv',
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\003\Caso_'+ str(cn) + '_paciente_003_insulina_procesada.csv',
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\004\Caso_'+ str(cn) + '_paciente_004_insulina_procesada.csv',
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\005\Caso_'+ str(cn) + '_paciente_005_insulina_procesada.csv',
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\006\Caso_'+ str(cn) + '_paciente_006_insulina_procesada.csv',
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\007\Caso_'+ str(cn) + '_paciente_007_insulina_procesada.csv',
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\008\Caso_'+ str(cn) + '_paciente_008_insulina_procesada.csv',
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\009\Caso_'+ str(cn) + '_paciente_009_insulina_procesada.csv']  # PATH
    path_gai_dataset_processed = [
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\001\Caso_'+ str(cn) + '_paciente_001_gai_procesados.csv',   #cambiar por path_gai_dataset_processed
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\002\Caso_'+ str(cn) + '_paciente_002_gai_procesada.csv',
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\003\Caso_'+ str(cn) + '_paciente_003_gai_procesada.csv',
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\004\Caso_'+ str(cn) + '_paciente_004_gai_procesada.csv',
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\005\Caso_'+ str(cn) + '_paciente_005_gai_procesada.csv',
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\006\Caso_'+ str(cn) + '_paciente_006_gai_procesada.csv',
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\007\Caso_'+ str(cn) + '_paciente_007_gai_procesada.csv',
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\008\Caso_'+ str(cn) + '_paciente_008_gai_procesada.csv',
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\009\Caso_'+ str(cn) + '_paciente_009_gai_procesada.csv']  # PATH
    path_food_dataset_processed = [
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\001\Caso_'+ str(cn) + '_paciente_001_comidas_procesadas.csv',
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\002\Caso_'+ str(cn) + '_paciente_002_comidas_procesadas.csv',
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\003\Caso_'+ str(cn) + '_paciente_003_comidas_procesadas.csv',
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\004\Caso_'+ str(cn) + '_paciente_004_comidas_procesadas.csv',
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\005\Caso_'+ str(cn) + '_paciente_005_comidas_procesadas.csv',
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\006\Caso_'+ str(cn) + '_paciente_006_comidas_procesadas.csv',
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\007\Caso_'+ str(cn) + '_paciente_007_comidas_procesadas.csv',
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\008\Caso_'+ str(cn) + '_paciente_008_comidas_procesadas.csv',
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\009\Caso_'+ str(cn) + '_paciente_009_comidas_procesadas.csv']  # PATH
    path_full_dataset_processed = [
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\001\Caso_'+ str(cn) + '_paciente_001_datos_procesados.csv',  #_ or not
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\002\Caso_'+ str(cn) + '_paciente_002_datos_procesados.csv',
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\003\Caso_'+ str(cn) + '_paciente_003_datos_procesados.csv',
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\004\Caso_'+ str(cn) + '_paciente_004_datos_procesados.csv',
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\005\Caso_'+ str(cn) + '_paciente_005_datos_procesados.csv',
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\006\Caso_'+ str(cn) + '_paciente_006_datos_procesados.csv',
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\007\Caso_'+ str(cn) + '_paciente_007_datos_procesados.csv',
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\008\Caso_'+ str(cn) + '_paciente_008_datos_procesados.csv',
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\009\Caso_'+ str(cn) + '_paciente_009_datos_procesados.csv']  # PATH
    path_scores_dataset_processed = [
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\001\Caso_'+ str(cn) + '_paciente_001_scores.csv',
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\002\Caso_'+ str(cn) + '_paciente_002_scores.csv',
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\003\Caso_'+ str(cn) + '_paciente_003_scores.csv',
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\004\Caso_'+ str(cn) + '_paciente_004_scores.csv',
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\005\Caso_'+ str(cn) + '_paciente_005_scores.csv',
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\006\Caso_'+ str(cn) + '_paciente_006_scores.csv',
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\007\Caso_'+ str(cn) + '_paciente_007_scores.csv',
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\008\Caso_'+ str(cn) + '_paciente_008_scores.csv',
                                path_dataset_processed + r'\Caso_'+ str(cn) + r'\009\Caso_'+ str(cn) + '_paciente_009_scores.csv',
                                path_dataset_processed + r'\Caso_' + str(cn) + r'\Caso_' + str(cn) + '_mean_scores_relevant_patients.csv',
                                path_dataset_processed + r'\Caso_' + str(cn) + r'\Caso_' + str(cn) + '_min_scores_relevant_patients.csv',
                                path_dataset_processed + r'\Caso_' + str(cn) + r'\Caso_' + str(cn) + '_max_scores_relevant_patients.csv',
                                path_dataset_processed + r'\Caso_' + str(cn) + r'\Caso_' + str(cn) + '_mean_scores_relevant_patients_graph.png',
                                path_dataset_processed + r'\Caso_' + str(cn) + r'\Caso_' + str(cn) + '_min_scores_relevant_patients_graph.png',
                                path_dataset_processed + r'\Caso_' + str(cn) + r'\Caso_' + str(cn) + '_max_scores_relevant_patients_graph.png'    ]  # PATH


    path_models_saved = path_project + r'\models'  # PATH


    #print(path_project, path_glucose_acceleration_graphs, path_insulin_graphs, path_food_graphs, path_dataset, path_glucose_dataset, path_acceleration_dataset, path_insulin_dataset, path_food_dataset, path_dataset_processed, path_acceleration_dataset_processed, path_insulin_dataset_processed, path_gai_dataset_processed, path_food_dataset_processed, path_full_dataset_processed, path_scores_dataset_processed, path_models_saved)

    return path_project, path_glucose_acceleration_graphs, path_insulin_graphs, path_food_graphs, path_dataset, path_glucose_dataset, path_acceleration_dataset, path_insulin_dataset, path_food_dataset, path_dataset_processed, path_acceleration_dataset_processed, path_insulin_dataset_processed,  path_gai_dataset_processed, path_food_dataset_processed, path_full_dataset_processed, path_scores_dataset_processed, path_models_saved