# insulin

* PREPARAR DATOS DE INSULINA
    * Se procesa la insulina como una exponencial creciente y decreciente...
        * Se genera la insulina rapida como exponencial creciente y decreciente... ->      
                * generaSignalInsulina()
                * crear_grafica_SignalInsulina()
        * Se genera la insulina lenta como exponencial creciente y decreciente...
                * generaSignalInsulina()
                * crear_grafica_SignalInsulina()

    * Se procesa la insulina como una función lineal a trozos...
        * Se genera la gráfica de la insulina Linspro...
            * generaSignalInsulinaLinspro()    
            * crear_grafica_SignalInsulinaLinspro()

        * Se genera la gráfica de la insulina Regular...
            * generaSignalInsulinaRegular()     
            * crear_grafica_SignalInsulinaRegular()
            
    * Se genera la gráfica de los perfiles de insulina Linspro, Regular y NPH...
            * generaSPerfilInsulinaLispro()
            * generaSPerfilInsulinaRegular()
            * generaSPerfilInsulinaNPH(1)
            * crear_graficas_perfiles_insulina()

    * Se genera la señal de asimilación de la insulina...

    * Se procesa la insulina...
        * procesaDatosInsulina()

        * Se muestran las gráficas con exponencial, lineal decreciente y perfiles...
            * crear_grafica_insulina_procesada_cre_dec()
            * crear_grafica_insulina_procesada_michaelis()
            * crear_grafica_insulina_procesada_perfiles()

    * Se añade los datos de la insulina...
        * anadeInsulinaProcesada()