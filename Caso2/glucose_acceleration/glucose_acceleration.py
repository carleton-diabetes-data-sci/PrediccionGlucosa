from glucose_acceleration.glucose import crear_grafica_glucosa

def bloque_glucosa_aceleracion(r, pacientes):
  print("PREPARAR DATOS DE GLUCOSA Y ACELERACION")
  print("-Se genera la gráfica de glucosa para el paciente 1...")
  path_glucosa = r+'\glucose_acceleration\graphs\Caso2_glucosa_paciente_001.png'
  crear_grafica_glucosa(r, path_glucosa)
  print("-Se procesan o importan los datos de aceleración...")
  #procesaDatosAccel(root, pacientes)    #Just once
  print("--Se genera la gráfica de aceleración sin procesar para el paciente 1...")
  path_aceleracion_sin_procesar = r+'\glucose_acceleration\graphs\Caso2_acceleracion_sin_procesar_paciente_001.png'
  #crear_grafica_aceleracion(r, path_aceleracion_sin_procesar)
  print("--Se genera la gráfica de aceleración procesada para el paciente 1...")
  path_grafica_aceleracion_procesada = r+'\glucose_acceleration\graphs\Caso2_acceleracion_procesada_paciente_001.png'
  #crear_grafica_aceleracion_procesada(r, path_grafica_aceleracion_procesada)