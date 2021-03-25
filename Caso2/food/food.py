def bloque_comida(root, pacientes, posicion_glucosa):
    print("PREPARAR DATOS DE COMIDA")
    print("-Se genera la gráfica de las comidas procesadas del paciente 1...")
    path_comidas_procesadas = root+'graficas/comidas/paulacomidasProcesadas.png'
    #crear_grafica_comidas_Procesadas(path_comidas_procesadas)
    print("-Se procesa los deltas de comida ...")
    ###procesaDatosComidas(root, pacientes, posicion_glucosa)      #Error in dia and comidaProcesada shape
    print("-Se genera la gráfica de comida Exponencial ...")
    path_comidas_exp = root+'graficas/comidas/paulacomidasExpPaciente.png'
    #crear_grafica_comidasExp(path_comidas_exp)
    print("-Se anade la comida procesada ...")                #Depends of insuline
    anadeComidaProcesada(root, pacientes, posicion_glucosa)
    print("-Se procesa los deltas de comida ...")
    path_grafica_comidas_calidad = root+'graficas/comidas/paulacomidasProcesadas.png'
    #crear_grafica_calidad(root, pacientes_all, path_grafica_comidas_calidad)