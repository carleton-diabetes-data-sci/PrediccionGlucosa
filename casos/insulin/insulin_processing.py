

""""
3.3.2 Procesamiento de la insulina
En el directorio de cada paciente, creamos un fichero insulina_procesada que contiene la fecha y la hora de la muestra de insulina y los siguientes parámetros:


*   **Fast_insulin:** insulina rápida que tendría el paciente en el cuerpo, simulando la absorción como una exponencial creciente y decreciente.
*   **Slow_insulin:** insulina lenta que tendría el paciente en el cuerpo, simulando la absorción como una exponencial creciente y decreciente.
*   **Fast_insulin_exp:** insulina rápida que tendría el paciente en el cuerpo, simulando la absorción como una exponencial decreciente.  #no se usa
*   **Slow_insulin_exp:** insulina lenta que tendría el paciente en el cuerpo, simulando la absorción como una exponencial decreciente. #no  se usa


"""


def procesaDatosInsulina(root, paciente, posicion_glucosa):
    horas = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
             "18", "19", "20", "21", "22", "23"]
    minutos = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09",
               "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
               "20", "21", "22", "23", "24", "25", "26", "27", "28", "29",
               "30", "31", "32", "33", "34", "35", "36", "37", "38", "39",
               "40", "41", "42", "43", "44", "45", "46", "47", "48", "49",
               "50", "51", "52", "53", "54", "55", "56", "57", "58", "59"]


    insulin = pd.read_csv(root + paciente + '/insulin.csv')

    print('paciente: ', paciente)
    print('Tamaño del csv de insulin: ', insulin.shape)

    fechas = pd.unique(insulin["date"])

    insulina_procesada_deltas = np.zeros(len(fechas) * len(horas) * len(minutos) * 2).reshape((len(fechas) * len(horas) * len(minutos), 2))
    insulina_procesada = np.zeros(len(fechas) * len(horas) * len(minutos) * 2).reshape((len(fechas) * len(horas) * len(minutos), 2))
    insulina_procesada_lispro_regular = np.zeros(len(fechas) * len(horas) * len(minutos) * 2).reshape((len(fechas) * len(horas) * len(minutos), 2))
    insulina_procesada_exp = np.zeros(len(fechas) * len(horas) * len(minutos) * 2).reshape((len(fechas) * len(horas) * len(minutos), 2))

    print('Tamaño del csv de insulina_procesada: ', insulina_procesada.shape)
    insulina_procesada_profiles = np.zeros(len(fechas) * len(horas) * len(minutos) * 2).reshape((len(fechas) * len(horas) * len(minutos), 2))
    # https://dtc.ucsf.edu/types-of-diabetes/type2/treatment-of-type-2-diabetes/medications-and-therapies/type-2-insulin-rx/types-of-insulin/

    posicion_insulina_procesada = 0
    for fecha_position in range(len(fechas)):
        fecha = fechas[fecha_position]
        for hora_position in range(len(horas)):
            hora = horas[hora_position]
            for minuto_position in range(len(minutos)):
                minuto = minutos[minuto_position]

                for y in range(insulin.shape[0]):

                    if fecha == insulin['date'][y]:
                        if insulin['time'][y].startswith(hora + ':' + minuto):

                            fast_insulin = float(insulin['fast_insulin'][y])
                            slow_insulin = float(insulin['slow_insulin'][y])
                            if (not (math.isnan(fast_insulin))):

                                print('fecha: ', fecha)
                                print('hora: ', hora)
                                print('minuto: ', minuto)
                                tau2 = -((2 * 60) - 1) / np.log(0.01)
                                exp_rapida = fast_insulin * signal.exponential(2 * 60, 0, tau2, False)
                                print('exp rapida: ', exp_rapida)
                                print('signal_insulina_rapida: ', signal_insulina_rapida)

                                for posicion_exp in range(len(signal_insulina_rapida)):
                                    if (posicion_insulina_procesada + posicion_exp < insulina_procesada.shape[0]):
                                        insulina_procesada[posicion_insulina_procesada + posicion_exp][0] = \
                                        insulina_procesada[posicion_insulina_procesada + posicion_exp][
                                            0] + fast_insulin * float(signal_insulina_rapida[posicion_exp])

                                for posicion_exp in range(len(exp_rapida)):
                                    if (posicion_insulina_procesada + posicion_exp < insulina_procesada.shape[0]):
                                        insulina_procesada_exp[posicion_insulina_procesada + posicion_exp][0] = \
                                        insulina_procesada_exp[posicion_insulina_procesada + posicion_exp][0] + \
                                        exp_rapida[posicion_exp]

                                signal_insulina_lispro = generaSignalInsulinaLinspro(fast_insulin)
                                for posicion_exp in range(len(signal_insulina_lispro)):
                                    if (posicion_insulina_procesada + posicion_exp < insulina_procesada.shape[0]):
                                        insulina_procesada_lispro_regular[
                                            posicion_insulina_procesada + posicion_exp][0] = \
                                        insulina_procesada_lispro_regular[
                                            posicion_insulina_procesada + posicion_exp][0] + signal_insulina_lispro[
                                            posicion_exp]

                                lispro_insulin = generaSPerfilInsulinaLispro(fast_insulin)
                                for posicion_exp in range(len(lispro_insulin)):
                                    if (posicion_insulina_procesada + posicion_exp < insulina_procesada.shape[0]):
                                        insulina_procesada_profiles[posicion_insulina_procesada + posicion_exp][0] = \
                                        insulina_procesada_profiles[posicion_insulina_procesada + posicion_exp][0] + \
                                        lispro_insulin[posicion_exp]

                                insulina_procesada_deltas[posicion_insulina_procesada][0] = fast_insulin

                            if (not (math.isnan(slow_insulin))):

                                print('fecha: ', fecha)
                                print('hora: ', hora)
                                print('minuto: ', minuto)
                                tau2 = -((8 * 60) - 1) / np.log(0.01)
                                exp_lenta = slow_insulin * signal.exponential(8 * 60, 0, tau2, False)
                                print('exp lenta: ', exp_rapida)
                                print('signal_insulina_lenta¡: ', signal_insulina_lenta)

                                for posicion_exp in range(len(signal_insulina_lenta)):
                                    if (posicion_insulina_procesada + posicion_exp < insulina_procesada.shape[0]):
                                        insulina_procesada[posicion_insulina_procesada + posicion_exp][1] = \
                                        insulina_procesada[posicion_insulina_procesada + posicion_exp][
                                            1] + slow_insulin * float(signal_insulina_lenta[posicion_exp])

                                for posicion_exp in range(len(exp_lenta)):
                                    if (posicion_insulina_procesada + posicion_exp < insulina_procesada.shape[0]):
                                        insulina_procesada_exp[posicion_insulina_procesada + posicion_exp][1] = \
                                        insulina_procesada_exp[posicion_insulina_procesada + posicion_exp][1] + \
                                        exp_lenta[posicion_exp]

                                signal_insulina_regular = generaSignalInsulinaRegular(slow_insulin)
                                for posicion_exp in range(len(signal_insulina_regular)):
                                    if (posicion_insulina_procesada + posicion_exp < insulina_procesada.shape[0]):
                                        insulina_procesada_lispro_regular[
                                            posicion_insulina_procesada + posicion_exp][1] = \
                                        insulina_procesada_lispro_regular[
                                            posicion_insulina_procesada + posicion_exp][1] + \
                                        signal_insulina_regular[posicion_exp]

                                NPH_insulin = generaSPerfilInsulinaNPH(1)
                                for posicion_exp in range(len(lispro_insulin)):
                                    if (posicion_insulina_procesada + posicion_exp < insulina_procesada.shape[0]):
                                        insulina_procesada_profiles[posicion_insulina_procesada + posicion_exp][1] = \
                                        insulina_procesada_profiles[posicion_insulina_procesada + posicion_exp][1] + \
                                        NPH_insulin[posicion_exp]

                                insulina_procesada_deltas[posicion_insulina_procesada][1] = slow_insulin

                posicion_insulina_procesada = posicion_insulina_procesada + 1

    posicion_insulina_procesada = 0
    print('Tamaño del csv de insulina_procesada: ', insulina_procesada.shape)
    lista_insulina_procesada = []
    for fecha_position in range(len(fechas)):
        fecha = fechas[fecha_position]
        for hora_position in range(len(horas)):
            hora = horas[hora_position]
            for minuto_position in range(len(minutos)):
                minuto = minutos[minuto_position]
                print('Posición: ', fecha_position * hora_position * minuto_position)

                fast_insulin_delta = insulina_procesada_deltas[posicion_insulina_procesada][0]
                print('fast_insulin_delta: ', fast_insulin_delta)
                slow_insulin_delta = insulina_procesada_deltas[posicion_insulina_procesada][1]
                print('slow_insulin_delta: ', slow_insulin_delta)

                fast_insulin = insulina_procesada[posicion_insulina_procesada][0]
                print('fast_insulin: ', fast_insulin)
                slow_insulin = insulina_procesada[posicion_insulina_procesada][1]
                print('slow_insulin: ', slow_insulin)

                fast_insulin_exp = insulina_procesada_exp[posicion_insulina_procesada][0]
                print('fast_insulin: ', fast_insulin)
                slow_insulin_exp = insulina_procesada_exp[posicion_insulina_procesada][1]
                print('slow_insulin exp: ', slow_insulin)

                fast_insulin_lispro = insulina_procesada_lispro_regular[posicion_insulina_procesada][0]
                print('fast_insulin_lispro: ', fast_insulin_lispro)

                slow_insulin_regular = insulina_procesada_lispro_regular[posicion_insulina_procesada][1]
                print('slow_insulin_regular: ', slow_insulin_regular)

                fast_insulin_profile = insulina_procesada_profiles[posicion_insulina_procesada][0]
                print('fast_insulin_profile: ', fast_insulin_profile)

                slow_insulin_profile = insulina_procesada_profiles[posicion_insulina_procesada][1]
                print('slow_insulin_profile: ', slow_insulin_profile)

                lista_insulina_procesada.append(
                    [fecha, hora + ':' + minuto + ':00', fast_insulin_delta, slow_insulin_delta, fast_insulin,
                     slow_insulin, fast_insulin_exp, slow_insulin_exp, fast_insulin_lispro, slow_insulin_regular,
                     fast_insulin_profile, slow_insulin_profile])

                posicion_insulina_procesada = posicion_insulina_procesada + 1


    #OUT OF PATIENTS LOOP
    df = pd.DataFrame(np.array(lista_insulina_procesada),
                      columns=['Date', 'Time', 'Fast_insulin_delta', 'Slow_insulin_delta', 'Fast_insulin_process',
                               'Slow_insulin_process', 'Fast_insulin_exp', 'Slow_insulin_exp',
                               'Fast_insulin_lispro', 'Slow_insulin_regular', 'Fast_insulin_profile',
                               'Slow_insulin_profile'])
    df.to_csv(root + paciente + '/insulina_procesada.csv', index=False)



#Exponencial creciente decreciente
def crear_grafica_insulina_procesada_cre_dec(root, path):
  datosInsulina_profiles = pd.read_csv(root+'001'+'/insulina_procesada.csv')

  eje_x = np.arange(datosInsulina_profiles.shape[0])
  print(eje_x.shape)

  fig, ax = plt.subplots()
  ax.plot(eje_x, datosInsulina_profiles['Fast_insulin_exp'], color='red', label='Fast insulin exponential')
  ax.plot(eje_x, datosInsulina_profiles['Slow_insulin_exp'], color='blue', label='Slow insulin exponential')
  plt.title('Patient 1. Exponential. Processed Insulin')
  plt.xlabel('Time instant (minutes)')
  plt.ylabel('Insulin level (mU/L)')
  leg = ax.legend()

  plt.savefig(path)

#Michaelis Menten Lineales decreciente
def crear_grafica_insulina_procesada_michaelis(root, path):

  datosInsulina_profiles = pd.read_csv(root+'001'+'/insulina_procesada.csv')

  eje_x = np.arange(datosInsulina_profiles.shape[0])
  print(eje_x.shape)

  fig, ax = plt.subplots()
  ax.plot(eje_x, datosInsulina_profiles['Fast_insulin_lispro'], color='red', label='Fast insulin Lyspro')
  ax.plot(eje_x, datosInsulina_profiles['Fast_insulin_delta'], color='blue', label='Insulin Deltas')
  plt.title('Patient 1. Michaelis-Menten Lyspro. Processed Insulin')
  plt.xlabel('Time instant (minutes)')
  plt.ylabel('Insulin level (mU/L)')
  leg = ax.legend()

  plt.savefig(path)

#Perfiles
def crear_grafica_insulina_procesada_perfiles(root, path):

    datosInsulina_profiles = pd.read_csv(root+'001'+'/insulina_procesada.csv')

    eje_x = np.arange(datosInsulina_profiles.shape[0])
    print(eje_x.shape)

    fig, ax = plt.subplots()
    ax.plot(eje_x, datosInsulina_profiles['Fast_insulin_profile'], color='red', label='Fast insulin')
    ax.plot(eje_x, datosInsulina_profiles['Slow_insulin_profile'], color='blue', label='Slow insulin')
    plt.title('Patient 1. Profiles. Processed Insulin')
    plt.xlabel('Time instant (minutes)')
    plt.ylabel('Insuline level (mU/L)')
    leg = ax.legend()

    plt.savefig(path)
