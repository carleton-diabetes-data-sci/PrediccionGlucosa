def bloque_glucosa_aceleracion(root, pacientes):
  print("PREPARAR DATOS DE GLUCOSA Y ACELERACION")
  print("-Se genera la gráfica de glucosa para el paciente 1...")
  path_glucosa = root+'graficas/glucosa/paulaglucosa_paciente_001.png'
  #crear_grafica_glucosa(path_glucosa)
  print("-Se procesan o importan los datos de aceleración...")
  #procesaDatosAccel(root, pacientes)    #Just once
  print("--Se genera la gráfica de aceleración sin procesar para el paciente 1...")
  path_aceleracion_sin_procesar = root+'graficas/aceleracion/paulaaccelSinProcesar_paciente_001.png'
  #crear_grafica_aceleracion(root, path_aceleracion_sin_procesar)
  print("--Se genera la gráfica de aceleración procesada para el paciente 1...")
  path_grafica_aceleracion_procesada = root+'graficas/aceleracion/paulaaccelProcesada_paciente_001.png'
  #crear_grafica_aceleracion_procesada(root, path_grafica_aceleracion_procesada)