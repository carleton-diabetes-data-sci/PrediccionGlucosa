import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split



def bloque_matriz(path_full_dataset_processed, pacientes, posicion_glucosa):
    """
    :param path_full_dataset_processed:
    :param pacientes:
    :param posicion_glucosa:
    :return:

    Damos forma a los datos
    Contruimos la matriz de entrenamiento y de test con los datos de glucosa obtenidos de un paciente.
    En base a 24 datos, el objetivo es predecir la glucosa dentro de media hora.
    A estos datos añadimos los valores de ejercicio físico

    """
    x_glucose = []
    y_glucose = []

    for paciente in pacientes:
        path_fichero_full_procesados = path_full_dataset_processed[paciente - 1]  # cambiar por path_gai_dataset_processed
        datosProcesados = pd.read_csv(path_fichero_full_procesados)
        print('paciente: ', paciente)
        print('Tamaño del csv de datos procesados gai previo a comida: ', datosProcesados.shape)

        for x in range(datosProcesados.shape[0] - 24 - posicion_glucosa):

            if datosProcesados['Date'][x] == datosProcesados['Date'][x + 24 + posicion_glucosa]:

                x_muestras = []

                for y in range(24):
                    # meto en un array todos mis datos
                    x_muestras.append([datosProcesados['Glucose'][x + y],
                                       datosProcesados['Accel'][x + y],
                                       datosProcesados['Fast_insulin'][x + y],
                                       datosProcesados['Slow_insulin'][x + y],
                                       datosProcesados['Fast_insulin_process'][x + y],
                                       datosProcesados['Slow_insulin_process'][x + y],
                                       datosProcesados['Fast_insulin_process_exp'][x + y],
                                       datosProcesados['Slow_insulin_process_exp'][x + y],
                                       datosProcesados['Delta_calories'][x + y],
                                       datosProcesados['Calories_exp'][x + y],
                                       datosProcesados['Fast_insulin_lispro'][x + y],
                                       datosProcesados['Slow_insulin_regular'][x + y],
                                       datosProcesados['Fast_insulin_profile'][x + y],
                                       datosProcesados['Slow_insulin_profile'][x + y]])

                x_glucose.append(x_muestras)
                y_glucose.append(datosProcesados['Glucose'][x + 24 + posicion_glucosa])

    x = np.array(x_glucose)
    print('Tamaño de x: ', x.shape)

    y = np.array(y_glucose)
    print('Tamaño de y: ', y.shape)

    return x, y


