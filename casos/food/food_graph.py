import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def crear_grafica_comidasExp(cn, pi, patient_digit, path_food_graphs, path_food_dataset_processed, posicion_glucosa, paciente):
    print("--FOOD_GRAPH_ CREAR GRÁFICA DE EXPONENCIALES DE COMIDA PARA 1 PACIENTE")

    print("El ID de paciente tiene el valor: ", pi, ". Si es 0 se hallan las gráficas para el paciente 001. Si no, para el paciente correspondiente.")
    print("--Definir el path para importar datos de comida procesada...")
    path_fichero_comidas_procesadas = path_food_dataset_processed[patient_digit-1]
    print(path_fichero_comidas_procesadas)                                       #PATH

    print("--Definir el path para guardar la gráfica...")
    path_comidas_exp = path_food_graphs + '\Caso_' + str(cn) + '_comidasExponential_paciente_00' + str(patient_digit) + '.png'            #PATH

    print("--Importamos fichero...")
    comidas_procesadas = pd.read_csv(path_fichero_comidas_procesadas)


    eje_x = np.arange(comidas_procesadas.shape[0])
    print(eje_x.shape)

    fig, ax = plt.subplots()
    ax.plot(eje_x, comidas_procesadas['calories_exp'], color='blue', label='Calories')
    plt.title('Calorie absorption (Patient '+str(patient_digit)+')')
    plt.xlabel('Time instant (min)')
    plt.ylabel('Calories (cal)')

    ax.set_xticks([1, 4, 5])
    ax.set_xticklabels([1, 4, 5], fontsize=12)

    
    leg = ax.legend()

    plt.savefig(path_comidas_exp)

    plt.show()



