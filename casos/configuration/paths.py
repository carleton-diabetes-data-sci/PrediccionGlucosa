
def define_paths():
    print("--PATHS: DEFINIR PATHS")
    path_project = r'C:\Users\apula\PycharmProjects\PrediccionGlucosa'


    path_glucose_acceleration_graphs = path_project + r'\casos\glucose_acceleration\graphs'
    path_insulin_graphs = path_project + r'\casos\insulin\graphs'
    path_food_graphs = path_project + r'\casos\food\graphs'

    path_dataset = path_project + r'\D1NAMO\diabetes_subset'

    path_glucose_dataset = [
                                path_dataset + r'\001\glucose.csv',
                                path_dataset + r'\002\glucose.csv',
                                path_dataset + r'\003\glucose.csv',
                                path_dataset + r'\004\glucose.csv',
                                path_dataset + r'\005\glucose.csv',
                                path_dataset + r'\006\glucose.csv',
                                path_dataset + r'\007\glucose.csv',
                                path_dataset + r'\008\glucose.csv',
                                path_dataset + r'\009\glucose.csv']
    path_acceleration_dataset = [
                                path_dataset + r'\001\glucose.csv',
                                path_dataset + r'\002\glucose.csv',
                                path_dataset + r'\003\glucose.csv',
                                path_dataset + r'\004\glucose.csv',
                                path_dataset + r'\005\glucose.csv',
                                path_dataset + r'\006\glucose.csv',
                                path_dataset + r'\007\glucose.csv',
                                path_dataset + r'\008\glucose.csv',
                                path_dataset + r'\009\glucose.csv']

    path_insulin_dataset = [
                                path_dataset + r'\001\insulin.csv',
                                path_dataset + r'\002\insulin.csv',
                                path_dataset + r'\003\insulin.csv',
                                path_dataset + r'\004\insulin.csv',
                                path_dataset + r'\005\insulin.csv',
                                path_dataset + r'\006\insulin.csv',
                                path_dataset + r'\007\insulin.csv',
                                path_dataset + r'\008\insulin.csv',
                                path_dataset + r'\009\insulin.csv']

    path_food_dataset = [
                                path_dataset + r'\001\food.csv',
                                path_dataset + r'\002\food.csv',
                                path_dataset + r'\003\food.csv',
                                path_dataset + r'\004\food.csv',
                                path_dataset + r'\005\food.csv',
                                path_dataset + r'\006\food.csv',
                                path_dataset + r'\007\food.csv',
                                path_dataset + r'\008\food.csv',
                                path_dataset + r'\009\food.csv']

    #print(path_project, path_glucose_acceleration_graphs, path_insulin_graphs, path_food_graphs, path_dataset, path_glucose_dataset, path_acceleration_dataset, path_insulin_dataset, path_food_dataset)

    return path_project, path_glucose_acceleration_graphs, path_insulin_graphs, path_food_graphs, path_dataset, path_glucose_dataset, path_acceleration_dataset, path_insulin_dataset, path_food_dataset