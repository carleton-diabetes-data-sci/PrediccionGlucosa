def anadeComidaProcesada(root, pacientes, posicion_glucosa):
    for paciente in pacientes:
        # if (paciente == '001'):
        datosProcesados = pd.read_csv(root + paciente + '/datos_procesados.csv')

        comidas_procesadas = pd.read_csv(root + paciente + '/comidas_procesadas.csv')

        print('paciente: ', paciente)
        print('Tamaño del csv de insulin: ', comidas_procesadas.shape)

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
                          columns=['Date', 'Time', 'Glucose', 'Accel', 'Fast_insulin', 'Slow_insulin',
                                   'Fast_insulin_process', 'Slow_insulin_process', 'Fast_insulin_process_exp',
                                   'Slow_insulin_process_exp', 'Delta_calories', 'Calories_exp', 'Fast_insulin_lispro',
                                   'Slow_insulin_regular', 'Fast_insulin_profile', 'Slow_insulin_profile'])
        # print(df['Delta_calories'])
        df.to_csv(root + paciente + '/datos_procesados.csv', index=False)