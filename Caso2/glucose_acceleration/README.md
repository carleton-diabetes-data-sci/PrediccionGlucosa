("PREPARAR DATOS DE GLUCOSA Y ACELERACION")
("-Se genera la gráfica de glucosa para el paciente 1...")
crear_grafica_glucosa(path_glucosa)

("-Se procesan o importan los datos de aceleración...")
procesaDatosAccel(root, pacientes)    #Just once

("--Se genera la gráfica de aceleración sin procesar para el paciente 1...")
crear_grafica_aceleracion(root, path_aceleracion_sin_procesar)

("--Se genera la gráfica de aceleración procesada para el paciente 1...")
crear_grafica_aceleracion_procesada(root, path_grafica_aceleracion_procesada)


Laura_modificados

Paula