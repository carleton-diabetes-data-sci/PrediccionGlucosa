
("PREPARAR DATOS DE COMIDA")

("-Se genera la gráfica de las comidas procesadas del paciente 1...")
crear_grafica_comidas_Procesadas(path_comidas_procesadas)

("-Se procesa los deltas de comida ...")
procesaDatosComidas(root, pacientes, posicion_glucosa)      #Error in dia and comidaProcesada shape
    
("-Se genera la gráfica de comida Exponencial ...")
crear_grafica_comidasExp(path_comidas_exp)
    
("-Se anade la comida procesada ...")                #Depends of insuline
anadeComidaProcesada(root, pacientes, posicion_glucosa)
    
("-Se procesa los deltas de comida ...")
crear_grafica_calidad(root, pacientes_all, path_grafica_comidas_calidad)