import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


def generaSignalComidas(inicio, calorias, duracion):
    signalInsulina = []
    signalReturn = []
    pico = 15

    tau_decreciente = -((duracion-pico)-1) / np.log(0.01)
    decreciente = signal.exponential((duracion-pico), 0, tau_decreciente, False)

    tau_creciente = -(pico-1) / np.log(0.01)
    creciente = signal.exponential(pico,pico, tau_creciente, False)
    signalInsulina.extend(creciente)
    signalInsulina.extend(decreciente)

    signalInicio = [0] * inicio
    signalInicio.extend(signalInsulina)

    for x in signalInicio:
        signalReturn.append(x*(calorias/100))

    #print(signalReturn)
    return signalReturn


def crear_grafica_comidas_Procesadas(cn, pi, patient_digit, path_food_graphs, posicion_glucosa, paciente):
    path_comidas_procesadas = path_food_graphs + '/Caso_' + str(cn) + '_comidasProcesadas.png'

    signal_comida_caloria = generaSignalComidas(0, 1000, 4*60)                     #inicio==0, calorias==1000, duración==4h

    eje_x = np.arange(4*60)
    print(eje_x.shape)

    fig, ax = plt.subplots()
    ax.plot(eje_x, signal_comida_caloria, color='red', label='1000 calorie food')
    plt.title('Processed signal of 1000 calorie food')
    plt.xlabel('Time instant (min)')
    plt.ylabel('Calories (cal)')
    leg = ax.legend()

    plt.savefig(path_comidas_procesadas)

    plt.show()

    #print(len(signal_comida))