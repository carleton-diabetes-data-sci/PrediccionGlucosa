def bloque_insulina():
    print("PREPARAR DATOS DE INSULINA")
    print("-Se procesa la insulina como una exponencial creciente y decreciente...")
    print("--Se genera la insulina rapida como exponencial creciente y decreciente...")
    inicio = 15
    pico = 2 * 60
    duracion = 5 * 60
    i_type = "Fast"
    path_grafica_insulina_fast = root + 'graficas/insulina/exp_creciente_decreciente/paulafastsignalInsulinaExp' + str(
        duracion) + '.png'
    signal_insulina_rapida = generaSignalInsulina(inicio, pico, duracion)
    # crear_grafica_SignalInsulina(signal_insulina_rapida, path_grafica_insulina_fast, i_type, duracion)

    print("--Se genera la insulina lenta como exponencial creciente y decreciente...")
    inicio = 60
    pico = 6 * 60
    duracion = 12 * 60
    i_type = "Slow"
    path_grafica_insulina_slow = root + 'graficas/insulina/exp_creciente_decreciente/paulaslowsignalInsulinaExp' + str(
        duracion) + '.png'
    signal_insulina_lenta = generaSignalInsulina(inicio, pico, duracion)
    # crear_grafica_SignalInsulina(signal_insulina_lenta, path_grafica_insulina_slow, i_type, duracion)

    print("-Se procesa la insulina como una función lineal a trozos...")
    print("--Se genera la gráfica de la insulina Linspro...")
    path_grafica_insulina_linspro = root + 'graficas/insulina/lineal_decreciente/paulasignalInsulinaLinsproExp.png'
    ejemploInsulinaLispro = generaSignalInsulinaLinspro(1)  # Contains graph
    # crear_grafica_SignalInsulinaLinspro(ejemploInsulinaLispro, path_grafica_insulina_linspro)

    print("--Se genera la gráfica de la insulina Regular...")
    path_grafica_insulina_regular = root + 'graficas/insulina/lineal_decreciente/paulasignalInsulinaRegularExp.png'
    ejemploInsulinaRegular = generaSignalInsulinaRegular(1)  # Contains graph
    # crear_grafica_SignalInsulinaRegular(ejemploInsulinaRegular, path_grafica_insulina_regular)

    print("-Se genera la gráfica de los perfiles de insulina Linspro, Regular y NPH...")
    lispro_insulin = generaSPerfilInsulinaLispro(1)
    regular_insulin = generaSPerfilInsulinaRegular(1)
    NPH_insulin = generaSPerfilInsulinaNPH(1)
    path_perfiles_insulina = root + 'graficas/insulina/perfiles/paulaperfilesInsulina.png'
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