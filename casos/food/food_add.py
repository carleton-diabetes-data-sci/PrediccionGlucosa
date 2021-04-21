import pandas as pd
import numpy as np
import datetime as tm
import math



def anadeComidaProcesada(cn, pi, patient_digit, path_gai_dataset_processed, path_food_dataset_processed,  path_full_dataset_processed, posicion_glucosa, paciente):
    print("--FOOD_ADD_ AÑADIR LA INFORMACION DE LA COMIDA PROCESADA A LA TABLA DE TODOS LOS DATOS PROCESADOS, 1 POR PACIENTE")

    print("El ID de paciente tiene el valor: ", pi, ". Si es 0 se hallan las gráficas para el paciente 001. Si no, para el paciente correspondiente.")

    print("--Definir el path para importar datos de comida procesada...")
    path_fichero_comidas_procesadas = path_food_dataset_processed[paciente-1]
    #print(path_fichero_comidas_procesadas)  # PATH

    print("--Definir el path para importar el resto de datos...")
    path_fichero_gai_procesados = path_gai_dataset_processed[paciente-1]   #cambiar por path_gai_dataset_processed
    #print(path_fichero_gai_procesados)  # PATH

    print("--Definir el path para guardar la tabla con todos los datos de glucosa, aceleración, insulina y comida procesados...")
    path_anadecomida = path_full_dataset_processed[paciente-1]         # PATH

    print("--Importamos ficheros...")
    comidas_procesadas = pd.read_csv(path_fichero_comidas_procesadas)
    datosProcesados = pd.read_csv(path_fichero_gai_procesados)          #cambiar a gai_procesados.csv para distinguir de todos_datos_procesados.csv


    print('PACIENTE: ', paciente)
    print('Tamaño del csv de comidas procesadas: ', comidas_procesadas.shape)
    print('Tamaño del csv de datos procesados gai previo a comida: ', datosProcesados.shape)


    dataList = []

    for x in range(1, datosProcesados.shape[0]):

        calorias = 0

        for y in range(comidas_procesadas.shape[0]):
            if datosProcesados['Date'][x] == comidas_procesadas['Date'][y]:
                time_datosProcesados = tm.datetime.strptime(datosProcesados['Time'][x], '%H:%M:%S')
                time_datosProcesadosAnterior = tm.datetime.strptime(datosProcesados['Time'][x - 1], '%H:%M:%S')
                time_comida_procesada = tm.datetime.strptime(comidas_procesadas['Time'][y], '%H:%M:%S')

                if time_comida_procesada <= time_datosProcesados and time_comida_procesada > time_datosProcesadosAnterior:

                    calorias_aux = float(comidas_procesadas['calories'][y])
                    calories_exp = float(comidas_procesadas['calories_exp'][y])
                    if (not (math.isnan(calorias_aux)) and calorias_aux > 0):
                        calorias = calorias_aux
                        # print(x, y, calorias, calories_exp)

        # print(x, calorias, calories_exp)
        dataList.append([datosProcesados['Date'][x], datosProcesados['Time'][x], datosProcesados['Glucose'][x],
                         datosProcesados['Accel'][x], datosProcesados['Fast_insulin'][x],
                         datosProcesados['Slow_insulin'][x], datosProcesados['Fast_insulin_process'][x],
                         datosProcesados['Slow_insulin_process'][x], datosProcesados['Fast_insulin_process_exp'][x],
                         datosProcesados['Slow_insulin_process_exp'][x], calorias, calories_exp,
                         datosProcesados['Fast_insulin_lispro'][x], datosProcesados['Slow_insulin_regular'][x],
                         datosProcesados['Fast_insulin_profile'][x], datosProcesados['Slow_insulin_profile'][x]])
        # print(dataList[0][10], dataList[0][11])

    df = pd.DataFrame(np.array(dataList),
                      columns=['Date', 'Time', '0_Glucose', '1_Accel', '2_Fast_insulin', '3_Slow_insulin',
                               '4_Fast_insulin_process', '5_Slow_insulin_process', '6_Fast_insulin_process_exp',
                               '7_Slow_insulin_process_exp', '8_Delta_calories', '9_Calories_exp', '10_Fast_insulin_lispro',
                               '11_Slow_insulin_regular', '12_Fast_insulin_profile', '13_Slow_insulin_profile'])

    df.to_csv(path_anadecomida, index=False)