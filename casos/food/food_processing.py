import pandas as pd
import numpy as np
import datetime as tm
import math

def procesaDatosComidas(path_food_dataset, path_gai_dataset_processed, path_food_dataset_processed, paciente, posicion_glucosa):
    horas = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
             "18", "19", "20", "21", "22", "23"]
    minutos = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09",
               "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
               "20", "21", "22", "23", "24", "25", "26", "27", "28", "29",
               "30", "31", "32", "33", "34", "35", "36", "37", "38", "39",
               "40", "41", "42", "43", "44", "45", "46", "47", "48", "49",
               "50", "51", "52", "53", "54", "55", "56", "57", "58", "59"]

    path_comida_raw=path_food_dataset[paciente-1]
    path_datos_gai=path_gai_dataset_processed[paciente-1]
    path_comida_procesada= [paciente-1]

    comidas = pd.read_csv(path_comida_raw)
    datos_procesados = pd.read_csv(path_datos_gai)


    print('paciente: ', paciente)
    print('Tamaño del csv de comidas: ', comidas.shape)

    lista_comidas = []
    dia = 0
    fecha_aux = ''
    diccionario = {}

    # print(datos_procesados.shape[0])

    for x in range(datos_procesados.shape[0]):
        fecha = datos_procesados['Date'][x]

        if (fecha != fecha_aux):
            fecha_aux = fecha
            dia = dia + 1
            diccionario[dia] = fecha
            print(dia)

    # print('diccionario: ', diccionario)

    """ERROR in dia, reshape ComidaProcesada[][x]"""
    dia = 0  # by paula dia -> dia_2
    fecha_aux = ''

    # print(comidas.shape[0])
    for x in range(comidas.shape[0]):
        fecha_hora = comidas['datetime'][x].split(' ')
        fecha = fecha_hora[0]

        if (fecha != fecha_aux):
            fecha_aux = fecha
            dia = dia + 1  # by paula dia -> dia_2
            print(dia_2)

        hora = fecha_hora[1]
        hora_split = hora.split(':')
        if dia in diccionario:
            fecha_real = diccionario[dia]
            lista_comidas.append([fecha_real, hora_split[0] + ':' + hora_split[1] + ':00', comidas['calories'][x]])
            # print(lista_comidas, fecha_real)

    """ERROR in dia"""
    # print('lista_comidas: ', lista_comidas)
    comidaProcesada = np.zeros(dia * len(horas) * len(minutos) * 2).reshape((dia * len(horas) * len(minutos),
                                                                             2))  # dia== 6 len(horas)==24 dia*len(horas)*len(minutos)==120 . reshape-> 8640, 7200 or 5760

    posicion_comida_procesada = 0
    for fecha_position in diccionario.values():
        # print(fecha_position)
        # print('fecha_position: ',fecha_position)
        for hora_position in range(len(horas)):
            hora = horas[hora_position]
            for minuto_position in range(len(minutos)):
                minuto = minutos[minuto_position]

                for y in range(len(lista_comidas)):

                    if fecha_position == lista_comidas[y][0]:
                        if lista_comidas[y][1].startswith(hora + ':' + minuto):

                            hayBolo = False
                            calorias = 0
                            time_comida_procesada = tm.datetime.strptime(hora + ':' + minuto + ':00', '%H:%M:%S')
                            for posicion_datos in range(1, datos_procesados.shape[0] - 6):

                                time_datosProcesados = tm.datetime.strptime(
                                    datos_procesados['Time'][posicion_datos], '%H:%M:%S')
                                time_datosProcesadosAnterior = tm.datetime.strptime(
                                    datos_procesados['Time'][posicion_datos - 1], '%H:%M:%S')
                                # print('time_datosProcesados: ',time_datosProcesados)
                                # print('time_datosProcesadosAnterior: ',time_datosProcesadosAnterior)

                                if time_comida_procesada <= time_datosProcesados and time_comida_procesada > time_datosProcesadosAnterior:
                                    if posicion_datos >= 12:
                                        for x in range(posicion_datos - 12, posicion_datos + 6):
                                            if (datos_procesados['Fast_insulin'][x] != 0):
                                                hayBolo = True
                                                # print('hayBolo')
                                    else:
                                        for x in range(posicion_datos, posicion_datos + 6):
                                            if (datos_procesados['Fast_insulin'][x] != 0):
                                                hayBolo = True
                                                # print('hayBolo')

                            if hayBolo:
                                calorias = float(lista_comidas[y][2])

                            if (not (math.isnan(calorias))):
                                """ERROR in dia and comidaProcesada patient 6, 7, 8"""
                                comidaProcesada[posicion_comida_procesada][0] = calorias

                                signal_comida = generaSignalComidas(0, calorias,
                                                                    4 * 60)  # 4 h de exponencial de calorías
                                # print(signal_comida)
                                for posicion_exp in range(len(signal_comida)):
                                    if (posicion_comida_procesada + posicion_exp < comidaProcesada.shape[0]):
                                        comidaProcesada[posicion_comida_procesada + posicion_exp][1] = \
                                        comidaProcesada[posicion_comida_procesada + posicion_exp][1] + float(
                                            signal_comida[posicion_exp])
                                        # print(comidaProcesada[posicion_comida_procesada+posicion_exp][1])

                posicion_comida_procesada = posicion_comida_procesada + 1
                # print(posicion_comida_procesada)

    posicion_comida_procesada = 0
    print('Tamaño de comidaProcesada: ', comidaProcesada.shape)  # error in patient 6
    lista_insulina_procesada = []
    for fecha_position in diccionario.values():
        for hora_position in range(len(horas)):
            hora = horas[hora_position]
            for minuto_position in range(len(minutos)):
                minuto = minutos[minuto_position]
                # print(minuto)
                # print(posicion_comida_procesada, comidaProcesada[posicion_comida_procesada])             #[0.        0.2456723]
                calorias = comidaProcesada[posicion_comida_procesada][0]
                # print(calorias)
                calorias_exp = comidaProcesada[posicion_comida_procesada][1]
                # print(calorias_exp)
                # print(calorias, calorias_exp)
                # print([fecha_position, hora+':'+minuto+':00', calorias, calorias_exp])
                lista_insulina_procesada.append(
                    [fecha_position, hora + ':' + minuto + ':00', calorias, calorias_exp])
                # print(lista_insulina_procesada)
                # print(posicion_comida_procesada )
                posicion_comida_procesada = posicion_comida_procesada + 1
                # print("posicion + 1", posicion_comida_procesada )

    # print(lista_insulina_procesada)
    df = pd.DataFrame(np.array(lista_insulina_procesada), columns=['Date', 'Time', 'calories', 'calories_exp'])
    df.to_csv(path_comida_procesada, index=False)