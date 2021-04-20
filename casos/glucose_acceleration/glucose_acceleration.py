from casos.glucose_acceleration.glucose import crear_grafica_glucosa

def bloque_glucosa_aceleracion(cn, pi, patient_digit, path_glucose_acceleration_graphs, path_glucose_dataset, pacientes):
  print("-GLUCOSE_ACCELERATION: PREPARAR DATOS DE GLUCOSA Y ACELERACION")
  print("-Se genera la gráfica de glucosa para el paciente 1...")
  crear_grafica_glucosa(cn, patient_digit, path_glucose_acceleration_graphs,  path_glucose_dataset)
  print("-Se procesan o importan los datos de aceleración...")
  #procesaDatosAccel(root, pacientes)    #Just once
  print("-Se genera la gráfica de aceleración sin procesar para el paciente 1...")
  path_aceleracion_sin_procesar = r+'\glucose_acceleration\graphs\Caso2_acceleracion_sin_procesar_paciente_001.png'            #PATH
  #crear_grafica_aceleracion(r, path_aceleracion_sin_procesar)
  print("-Se genera la gráfica de aceleración procesada para el paciente 1...")
  path_grafica_aceleracion_procesada = r+'\glucose_acceleration\graphs\Caso2_acceleracion_procesada_paciente_001.png'             #PATH
  #crear_grafica_aceleracion_procesada(r, path_grafica_aceleracion_procesada)