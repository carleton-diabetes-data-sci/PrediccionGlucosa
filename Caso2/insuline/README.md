("PREPARAR DATOS DE INSULINA")
("-Se procesa la insulina como una exponencial creciente y decreciente...")
("--Se genera la insulina rapida como exponencial creciente y decreciente...")
signal_insulina_rapida = generaSignalInsulina(inicio, pico, duracion)#crear_grafica_SignalInsulina(signal_insulina_rapida, path_grafica_insulina_fast, i_type, duracion)
print("--Se genera la insulina lenta como exponencial creciente y decreciente...")

signal_insulina_lenta = generaSignalInsulina(inicio, pico, duracion)
crear_grafica_SignalInsulina(signal_insulina_lenta, path_grafica_insulina_slow, i_type, duracion)

("-Se procesa la insulina como una función lineal a trozos...")
("--Se genera la gráfica de la insulina Linspro...")
ejemploInsulinaLispro = generaSignalInsulinaLinspro(1)      #Contains graph
crear_grafica_SignalInsulinaLinspro(ejemploInsulinaLispro, path_grafica_insulina_linspro)

("--Se genera la gráfica de la insulina Regular...")
ejemploInsulinaRegular = generaSignalInsulinaRegular(1)      #Contains graph
crear_grafica_SignalInsulinaRegular(ejemploInsulinaRegular, path_grafica_insulina_regular)

("-Se genera la gráfica de los perfiles de insulina Linspro, Regular y NPH...")
lispro_insulin = generaSPerfilInsulinaLispro(1)
regular_insulin = generaSPerfilInsulinaRegular(1)
NPH_insulin = generaSPerfilInsulinaNPH(1)
 = root+'graficas/insulina/perfiles/paulaperfilesInsulina.png'
crear_graficas_perfiles_insulina(path_perfiles_insulina, lispro_insulin, regular_insulin, NPH_insulin)



("-Se genera la señal de asimilación de la insulina...")

("-Se procesa la insulina...")
procesaDatosInsulina(root, pacientes, posicion_glucosa)

("--Se muestran las gráficas con exponencial, lineal decreciente y perfiles...")
crear_grafica_insulina_procesada_cre_dec(root, path_grafica_insulina_creciente_decreciente)

crear_grafica_insulina_procesada_michaelis(root, path_grafica_insulina_michaelis)

crear_grafica_insulina_procesada_perfiles(root, path_grafica_insulina_procesada_perfiles)

print("-Se añade los datos de la insulina...")
anadeInsulinaProcesada(root, pacientes, posicion_glucosa)