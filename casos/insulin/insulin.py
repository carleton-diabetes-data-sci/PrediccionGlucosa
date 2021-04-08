def bloque_insulina(cn, pi, path_insulin_graphs, path_insulin_dataset):


    print("PREPARAR DATOS DE INSULINA")

    print("-Se preparan los path de entrada (insulina)  y de salida (insulina procesada y graficas)...")
    print("-El ID de paciente tiene el valor: ", pi, ". Si es 0 se hallan las gráficas para el paciente 001. Si no, para el paciente correspondiente.")
    if (pi == 0):
        patient_digit == 1
        print("--Definir el path para importar datos de insulina...")
        print("El path del fichero inicial de insulina del paciente 001 es: ", path_insuline_dataset[0])  # r'C:\Users\apula\PycharmProjects\PrediccionGlucosa\D1NAMO\diabetes_subset\001\insulin.csv'
        path_fichero_insulina = path_insulin_dataset[0]

    else:
        patient_digit ==pi
        print("--Definir el path para importar datos de insulina...")
        print("El path del fichero inicial de insulina del paciente 001 es: ", path_insuline_dataset[pi-1])  # r'C:\Users\apula\PycharmProjects\PrediccionGlucosa\D1NAMO\diabetes_subset\001\insulin.csv'
        path_fichero_insulina = path_insulin_dataset[pi-1]


    print("--Definir el path para guardar la gráfica de insulina rapida como exponencial...")
    path_grafica_insulina_fast = path_insulin_graphs + '\exponentials\Caso_' + str(cn) + '_insulina_exponencial_fastSignal' + str(duracion) + '_paciente00' + str(patient_digit) + '.png'

    print("--Definir el path para guardar la gráfica de insulina lenta como exponencial...")
    path_grafica_insulina_slow = path_insulin_graphs + '\exponentials\Caso_' + str(cn) + '_insulina_exponencial_slowSignal' + str(duracion) + '_paciente00' + str(patient_digit) + '.png'

    print("--Definir el path para guardar la gráfica de insulina rápida lispro con el modelo Michaelis Menten")
    path_grafica_insulina_lispro = path_insulin_graphs + '\menten\Caso_' + str(cn) + '_insulina_menten_lisproSignal_paciente00' + str(patient_digit) + '.png'

    print("--Definir el path para guardar la gráfica de insulina rápida regular con el modelo Michaelis Menten")
    path_grafica_insulina_regular = path_insulin_graphs + '\menten\Caso_' + str(cn) + '_insulina_menten_regularSignal_paciente00' + str(patient_digit) + '.png'


    print("-Se procesa la insulina como una exponencial creciente y decreciente...")

    print("--Se genera la insulina rapida como exponencial creciente y decreciente...")
    inicio = 15
    pico = 2 * 60
    duracion = 5 * 60
    i_type = "Fast"

    signal_insulina_rapida = generaSignalInsulina(inicio, pico, duracion)
    #crear_grafica_SignalInsulina(signal_insulina_rapida, path_grafica_insulina_fast, i_type, duracion)

    print("--Se genera la insulina lenta como exponencial creciente y decreciente...")
    inicio = 60
    pico = 6 * 60
    duracion = 12 * 60
    i_type = "Slow"

    signal_insulina_lenta = generaSignalInsulina(inicio, pico, duracion)
    # crear_grafica_SignalInsulina(signal_insulina_lenta, path_grafica_insulina_slow, i_type, duracion)

    print("-Se procesa la insulina como una función lineal a trozos de Michaelis Menten...")
    print("--Se genera la gráfica de la insulina Lispro...")
    ejemploInsulinaLispro = generaSignalInsulinaLispro(1)  # Contains graph
    #crear_grafica_SignalInsulinaLispro(ejemploInsulinaLispro, path_grafica_insulina_lispro)

    print("--Se genera la gráfica de la insulina Regular...")
    ejemploInsulinaRegular = generaSignalInsulinaRegular(1)  # Contains graph
    #crear_grafica_SignalInsulinaRegular(ejemploInsulinaRegular, path_grafica_insulina_regular)

    print("-Se genera la gráfica de los perfiles de insulina Lispro, Regular y NPH...")
    lispro_insulin = generaSPerfilInsulinaLispro(1)
    regular_insulin = generaSPerfilInsulinaRegular(1)
    NPH_insulin = generaSPerfilInsulinaNPH(1)
    path_perfiles_insulina = root + 'graficas/insulina/profiles/paulaperfilesInsulina.png'
    # crear_graficas_perfiles_insulina(path_perfiles_insulina, lispro_insulin, regular_insulin, NPH_insulin)

    return signal_insulina_rapida, signal_insulina_lenta, ejemploInsulinaLispro, path_grafica_insulina_regular, lispro_insulin, regular_insulin, NPH_insulin


def bloque_insulina_2(signal_insulina_rapida, signal_insulina_lenta, ejemploInsulinaLispro,
                      path_grafica_insulina_regular, lispro_insulin, regular_insulin, NPH_insulin):
    print("-Se genera la señal de asimilación de la insulina...")

    print("-Se procesa la insulina...")
    # procesaDatosInsulina(root, pacientes, posicion_glucosa)

    print("--Se muestran las gráficas con exponencial, lineal decreciente y perfiles...")
    path_grafica_insulina_creciente_decreciente = root + 'graficas/insulina/exp_creciente_decreciente/paulainsulinaProcesadaExp.png'
    # crear_grafica_insulina_procesada_cre_dec(root, path_grafica_insulina_creciente_decreciente)

    path_grafica_insulina_michaelis = root + 'graficas/insulina/lineal_decreciente/paulainsulinaProcesadamichaelis.png'
    # crear_grafica_insulina_procesada_michaelis(root, path_grafica_insulina_michaelis)

    path_grafica_insulina_procesada_perfiles = root + 'graficas/insulina/perfiles/paulainsulinaProcesadaPerfiles.png'
    # crear_grafica_insulina_procesada_perfiles(root, path_grafica_insulina_procesada_perfiles)

    print("-Se añade los datos de la insulina...")
    # anadeInsulinaProcesada(root, pacientes, posicion_glucosa)