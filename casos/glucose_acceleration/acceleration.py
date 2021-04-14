def procesaDatosAccel(root, pacientes):
    for paciente in pacientes:

        sensor_data = []

        glucose = pd.read_csv(root + paciente + '/glucose.csv')

        print('paciente: ', paciente)
        print('Tamaño del csv de glucosa: ', glucose.shape)

        posicion_inicial = 0
        fichero_aux = ''
        accel_data = []

        dataList = []

        fichero_completados = []
        ficherosAceleracion = os.listdir(root + paciente + '/sensor_data/Accel')
        print(ficherosAceleracion)

        for fichero_x in range(len(ficherosAceleracion)):
            accel_data.append(
                pd.read_csv(root + paciente + '/sensor_data/Accel/' + str(ficherosAceleracion[fichero_x])))

        for x in range(glucose.shape[0]):

            time = glucose['time'][x]

            fecha_separada = glucose['date'][x].split('-')
            fecha_glucosa = fecha_separada[2] + '/' + fecha_separada[1] + '/' + fecha_separada[0] + ' ' + time

            if (os.path.isdir(root + paciente + '/sensor_data/Accel')):

                aceleracion = 0
                for fichero_x in range(len(ficherosAceleracion)):

                    if not (ficherosAceleracion[fichero_x] in fichero_completados):

                        sensor_data = accel_data[fichero_x]

                        if (any(time_sensor.startswith(fecha_glucosa) for time_sensor in sensor_data['Time'])):
                            # Si mi fecha está en el fichero
                            # He cambiado de fichero, vuelvo a empezar las posiciones, quito el fichero anterior porque ya lo he revisado
                            if (ficherosAceleracion[fichero_x] != fichero_aux and fichero_aux != '' and (
                                    fichero_aux not in fichero_completados)):
                                fichero_completados.append(fichero_aux)
                                print('Cambio de fichero, fichero_completados: ', fichero_completados)
                                print('Tamaño del csv de acceleración: ', sensor_data.shape)
                                print('Cambio de fichero, posicion_inicial: ', posicion_inicial)
                                posicion_inicial = 0

                            x_muestras = []

                            # meto en un array todos mis datos
                            # también añadiré la desviación estandar la actividad física

                            for sensor_data_position in range(posicion_inicial, sensor_data.shape[0]):

                                if (sensor_data['Time'][sensor_data_position].split(' ')[1].startswith(
                                        time) and sensor_data_position > 30000):
                                    # He encontrado el último dato del sensor a mi hora
                                    posicion_inicial = sensor_data_position
                                    break

                            if (posicion_inicial > 30000 and posicion_inicial <= sensor_data.shape[0]):
                                # Hago la media de los 5 últimos minutos
                                aceleracion_aux = []

                                aceleracion_aux = [[sensor_data['Vertical'][sensor_data_position_def],
                                                    sensor_data['Lateral'][sensor_data_position_def],
                                                    sensor_data['Sagittal'][sensor_data_position_def]] for
                                                   sensor_data_position_def in
                                                   range(posicion_inicial - 30000, posicion_inicial)]
                                aceleracion = np.std(aceleracion_aux)

                            fichero_aux = ficherosAceleracion[fichero_x]
                            # Ya he encontrado mi fecha en uno de los ficheros

                            # if(posicion_inicial >= sensor_data.shape[0]-30000 and (fichero_aux not in fichero_completados)):
                            #     fichero_completados.append(fichero_aux)
                            #     print('Cambio de fichero, fichero_completados final: ', fichero_completados)
                            #     print('Tamaño del csv de acceleración: ',sensor_data.shape)
                            #     print('Cambio de fichero, posicion_inicial: ', posicion_inicial)
                            #     posicion_inicial = 0

                            # break;
                            dataList.append(
                                [glucose['date'][x], glucose['time'][x], glucose['glucose'][x], aceleracion])

                            # Si aún no he completado los ficheros sigo añadiendo, sino no
                # if(len(fichero_completados) != len(ficherosAceleracion)):
                # dataList.append([glucose['date'][x], glucose['time'][x], glucose['glucose'][x], aceleracion])

        df = pd.DataFrame(np.array(dataList),
                          columns=['Date', 'Time', 'Glucose', 'Accel'])

        df.to_csv(root + paciente + '/datos_procesadosAccel.csv', index=False)


def crear_grafica_aceleracion(root, path_grafica):
    ficherosAceleracion = os.listdir(root + '001' + '/sensor_data/Accel')

    aceleracionV = []
    aceleracionL = []
    aceleracionS = []
    accel_data = []

    for fichero_x in range(len(ficherosAceleracion)):
        accel_data.append(pd.read_csv(root + '001' + '/sensor_data/Accel/' + str(ficherosAceleracion[fichero_x])))

    print(ficherosAceleracion)
    for fichero_x in range(len(ficherosAceleracion)):
        print(fichero_x)

        aceleracionV.extend(accel_data[fichero_x]['Vertical'])
        aceleracionL.extend(accel_data[fichero_x]['Lateral'])
        aceleracionS.extend(accel_data[fichero_x]['Sagittal'])

    eje_x = np.arange(len(aceleracionS))
    # print(eje_x.shape)
    dim = 20  # elements showed in the zoom
    # print(eje_x)
    # print(eje_x[:dim])

    # Creates two subplots and unpacks the output array immediately
    f, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey=True, figsize=(18, 4))

    ax1.set_title('Patient 1 non processed_subset glucose_acceleration')
    ax1.set(xlabel='Time instant (sample)', ylabel='Acceleration (gal)')
    ax1.margins(0.05)  # Default margin is 0.05, value 0 means fit
    ax1.plot(eje_x, aceleracionV, color='red', label='Vertical accel')
    ax1.plot(eje_x, aceleracionL, color='blue', label='Lateral accel')
    ax1.plot(eje_x, aceleracionS, color='green', label='Sagittal accel')
    leg = ax1.legend()

    ax2.set_title('Zoomed in')
    ax2.set(xlabel='Time instant (sample)', ylabel='Acceleration (gal)')
    ax2.margins(0.00)  # Default margin is 0.05, value 0 means fit
    ax2.plot(eje_x[:dim], aceleracionV[:dim], color='red', label='Vertical accel')
    ax2.plot(eje_x[:dim], aceleracionL[:dim], color='blue', label='Lateral accel')
    ax2.plot(eje_x[:dim], aceleracionS[:dim], color='green', label='Sagittal accel')
    leg = ax2.legend()

    ax3.set_title('Zoomed in')
    ax3.set(xlabel='Time instant(sample)', ylabel='Acceleration (gal)')
    ax3.margins(x=-0.499, y=0)  # Values in (-0.5, 0.0) zooms in to center
    ax3.plot(eje_x, aceleracionV, color='red', label='Vertical accel')
    ax3.plot(eje_x, aceleracionL, color='blue', label='Lateral accel')
    ax3.plot(eje_x, aceleracionS, color='green', label='Sagittal accel')
    leg = ax3.legend()

    plt.show()

    plt.savefig(path_grafica)
