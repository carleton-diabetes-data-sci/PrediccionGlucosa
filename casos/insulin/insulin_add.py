"""
Añadimos los datos de la insulina

Añado cuando el paciente se puso insulina (slow o fast) en la hora de la toma de glucos. Se añade cuanta insulina se puso justo en esa hora o antes de la toma de glucos, en función de si hay una muestra a esa hora.
"""


def anadeInsulinaProcesada(root, paciente, posicion_glucosa):  # modificado
    # datosProcesados = pd.read_csv(root+paciente+'/datos_procesadosAccel.csv')
    datosProcesados = pd.read_csv(root + paciente + '/glucose.csv')

    insulina_procesada = pd.read_csv(root + paciente + '/insulina_procesada.csv')

    print('paciente: ', paciente)
    print('Tamaño del csv de insulin: ', insulina_procesada.shape)

    dataList = []
    for x in range(1, datosProcesados.shape[0]):

        fast_insulin = 0
        slow_insulin = 0
        fast_insulin_procesada = 0
        slow_insulin_procesada = 0
        fast_insulin_procesada_exp = 0
        slow_insulin_procesada_exp = 0
        fast_insulin_lispro = 0
        slow_insulin_regular = 0

        fast_insulin_profile = 0
        slow_insulin_profile = 0

        for y in range(insulina_procesada.shape[0]):
            if datosProcesados['date'][x] == insulina_procesada['Date'][y]:  # Date  datosProcesados['Date'][x]
                time_datosProcesados = tm.datetime.strptime(datosProcesados['time'][x], '%H:%M:%S')  # Time
                time_datosProcesadosAnterior = tm.datetime.strptime(datosProcesados['time'][x - 1], '%H:%M:%S')
                time_insulina_procesada = tm.datetime.strptime(insulina_procesada['Time'][y],
                                                               '%H:%M:%S')  # time -> Time  insulina_procesada['time'][y]
                if time_insulina_procesada <= time_datosProcesados and time_insulina_procesada > time_datosProcesadosAnterior:

                    fast_insulin_aux = float(insulina_procesada['Fast_insulin_delta'][y])
                    slow_insulin_aux = float(insulina_procesada['Slow_insulin_delta'][y])
                    fast_insulin_procesada = float(insulina_procesada['Fast_insulin_process'][y])
                    slow_insulin_procesada = float(insulina_procesada['Slow_insulin_process'][y])
                    fast_insulin_procesada_exp = float(insulina_procesada['Fast_insulin_exp'][y])
                    slow_insulin_procesada_exp = float(insulina_procesada['Slow_insulin_exp'][y])
                    fast_insulin_lispro = float(insulina_procesada['Fast_insulin_lispro'][y])
                    slow_insulin_regular = float(insulina_procesada['Slow_insulin_regular'][y])

                    fast_insulin_profile = float(insulina_procesada['Fast_insulin_profile'][y])
                    slow_insulin_profile = float(insulina_procesada['Slow_insulin_profile'][y])

                    if (not (math.isnan(fast_insulin_aux)) and fast_insulin_aux > 0):
                        fast_insulin = fast_insulin_aux

                    if (not (math.isnan(slow_insulin_aux)) and slow_insulin_aux > 0):
                        slow_insulin = slow_insulin_aux

                    if (math.isnan(fast_insulin_procesada)):
                        fast_insulin_procesada = 0

                    if (math.isnan(slow_insulin_procesada)):
                        slow_insulin_procesada = 0

                    if (math.isnan(fast_insulin_procesada_exp)):
                        fast_insulin_procesada_exp = 0

                    if (math.isnan(slow_insulin_procesada_exp)):
                        slow_insulin_procesada_exp = 0

                    if (math.isnan(fast_insulin_lispro)):
                        fast_insulin_lispro = 0

                    if (math.isnan(slow_insulin_regular)):
                        slow_insulin_regular = 0

                    if (math.isnan(fast_insulin_profile)):
                        fast_insulin_profile = 0

                    if (math.isnan(slow_insulin_profile)):
                        slow_insulin_profile = 0

                        # Date, Time, Glucose...
        acceleration = 0  # datosProcesados['Accel'][x]
        dataList.append(
            [datosProcesados['date'][x], datosProcesados['time'][x], datosProcesados['glucose'][x], acceleration,
             fast_insulin, slow_insulin, fast_insulin_procesada, slow_insulin_procesada, fast_insulin_procesada_exp,
             slow_insulin_procesada_exp, fast_insulin_lispro, slow_insulin_regular, fast_insulin_profile,
             slow_insulin_profile])

    df = pd.DataFrame(np.array(dataList),
                      columns=['Date', 'Time', '0_Glucose', '1_Accel', '2_Fast_insulin', '3_Slow_insulin',
                               '4_Fast_insulin_process', '5_Slow_insulin_process', '6_Fast_insulin_process_exp',
                               '7_Slow_insulin_process_exp', '10_Fast_insulin_lispro', '11_Slow_insulin_regular',
                               '12_Fast_insulin_profile', '13_Slow_insulin_profile'])  #Más adelante 8_Delta_calories y 9_Calories_exp
    df.to_csv(root + paciente + '/datos_procesados.csv', index=False)


