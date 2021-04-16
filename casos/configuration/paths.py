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
                                path_dataset + r'\001\food.csv',
                                path_dataset + r'\002\food.csv',
                                path_dataset + r'\003\food.csv',
                                path_dataset + r'\004\food.csv',
                                path_dataset + r'\005\food.csv',
                                path_dataset + r'\006\food.csv',
                                path_dataset + r'\007\food.csv',
                                path_dataset + r'\008\food.csv',
                                path_dataset + r'\009\food.csv']            #PATH

    path_dataset_processed = path_project + r'\D1NAMO\processed_subset'  # PATH

    path_acceleration_dataset_processed = [
                                path_dataset_processed + r'\001\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_datosprocesadosAccel.csv',
                                path_dataset_processed + r'\002\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_datosprocesadosAccel.csv',
                                path_dataset_processed + r'\003\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_datosprocesadosAccel.csv',
                                path_dataset_processed + r'\004\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_datosprocesadosAccel.csv',
                                path_dataset_processed + r'\005\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_datosprocesadosAccel.csv',
                                path_dataset_processed + r'\006\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_datosprocesadosAccel.csv',
                                path_dataset_processed + r'\007\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_datosprocesadosAccel.csv',
                                path_dataset_processed + r'\008\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_datosprocesadosAccel.csv',
                                path_dataset_processed + r'\009\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_datosprocesadosAccel.csv']  # PATH
    path_insulin_dataset_processed = [
                                path_dataset_processed + r'\001\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_insulina_procesada.csv',
                                path_dataset_processed + r'\002\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_insulina_procesada.csv',
                                path_dataset_processed + r'\003\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_insulina_procesada.csv',
                                path_dataset_processed + r'\004\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_insulina_procesada.csv',
                                path_dataset_processed + r'\005\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_insulina_procesada.csv',
                                path_dataset_processed + r'\006\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_insulina_procesada.csv',
                                path_dataset_processed + r'\007\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_insulina_procesada.csv',
                                path_dataset_processed + r'\008\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_insulina_procesada.csv',
                                path_dataset_processed + r'\009\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_insulina_procesada.csv']  # PATH


    path_gai_dataset_processed = [
                                path_dataset_processed + r'\001\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_gai_procesados.csv',   #cambiar por path_gai_dataset_processed
                                path_dataset_processed + r'\002\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_gai_procesada.csv',
                                path_dataset_processed + r'\003\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_gai_procesada.csv',
                                path_dataset_processed + r'\004\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_gai_procesada.csv',
                                path_dataset_processed + r'\005\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_gai_procesada.csv',
                                path_dataset_processed + r'\006\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_gai_procesada.csv',
                                path_dataset_processed + r'\007\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_gai_procesada.csv',
                                path_dataset_processed + r'\008\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_gai_procesada.csv',
                                path_dataset_processed + r'\009\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_gai_procesada.csv']  # PATH


    path_food_dataset_processed = [
                                path_dataset_processed + r'\001\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_comidas_procesadas.csv',
                                path_dataset_processed + r'\002\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_comidas_procesadas.csv',
                                path_dataset_processed + r'\003\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_comidas_procesadas.csv',
                                path_dataset_processed + r'\004\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_comidas_procesadas.csv',
                                path_dataset_processed + r'\005\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_comidas_procesadas.csv',
                                path_dataset_processed + r'\006\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_comidas_procesadas.csv',
                                path_dataset_processed + r'\007\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_comidas_procesadas.csv',
                                path_dataset_processed + r'\008\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_comidas_procesadas.csv',
                                path_dataset_processed + r'\009\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_comidas_procesadas.csv']  # PATH

    path_full_dataset_processed = [
                                path_dataset_processed + r'\001\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_datos_procesados.csv',  #_ or not
                                path_dataset_processed + r'\002\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_datosprocesados.csv',
                                path_dataset_processed + r'\003\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_datosprocesados.csv',
                                path_dataset_processed + r'\004\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_datosprocesados.csv',
                                path_dataset_processed + r'\005\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_datosprocesados.csv',
                                path_dataset_processed + r'\006\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_datosprocesados.csv',
                                path_dataset_processed + r'\007\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_datosprocesados.csv',
                                path_dataset_processed + r'\008\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_datosprocesados.csv',
                                path_dataset_processed + r'\009\Caso_'+ str(cn) + '\Caso_'+ str(cn) + '_datosprocesados.csv']  # PATH

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
                                path_dataset_processed + r'\Caso_' + str(cn) + '\Caso_' + str(cn) + '_mean_scores_relevant_patients.csv']  # PATH

    #print(path_project, path_glucose_acceleration_graphs, path_insulin_graphs, path_food_graphs, path_dataset, path_glucose_dataset, path_acceleration_dataset, path_insulin_dataset, path_food_dataset, path_dataset_processed, path_acceleration_dataset_processed, path_insulin_dataset_processed, path_gai_dataset_processed, path_food_dataset_processed, path_full_dataset_processed, path_scores_dataset_processed)

    return path_project, path_glucose_acceleration_graphs, path_insulin_graphs, path_food_graphs, path_dataset, path_glucose_dataset, path_acceleration_dataset, path_insulin_dataset, path_food_dataset, path_dataset_processed, path_acceleration_dataset_processed, path_insulin_dataset_processed,  path_gai_dataset_processed, path_food_dataset_processed, path_full_dataset_processed, path_scores_dataset_processed