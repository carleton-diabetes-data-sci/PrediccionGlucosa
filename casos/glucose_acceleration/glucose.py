import pandas as pd
import numpy as np
import os
import sys
import matplotlib.pyplot as plt

def crear_grafica_glucosa(cn, pi, path_glucose_acceleration_graphs,  path_glucose_dataset):
    print("--GLUCOSE: CREAR GRÁFICA DE GLUCOSA PARA 1 PACIENTE")

    print("El ID de paciente tiene el valor: ", pi, ". Si es 0 se hallan las gráficas para el paciente 001. Si no, para el paciente correspondiente.")

    if(pi==0):
        print("--Definir el path para importar datos de glucosa...")
        print("El path del fichero inicial de glucosa del paciente 001 es: ", path_glucose_dataset[0])  #r'C:\Users\apula\PycharmProjects\PrediccionGlucosa\D1NAMO\diabetes_subset\001\glucose.csv'
        path_fichero_glucosa = path_glucose_dataset[0]            #PATH

        print("--Definir el path para guardar la gráfica...")
        path_glucosa = path_glucose_acceleration_graphs + '\Caso_' + str(cn) + '_glucosa_paciente_001.png'            #PATH

    else:
        print("--Definir el path para importar datos de glucosa...")
        path_fichero_glucosa = path_glucose_dataset[pi-1]
        print(path_fichero_glucosa)

        print("--Definir el path para guardar la gráfica...")
        path_glucosa = path_glucose_acceleration_graphs + '\Caso_' + str(cn) + '_glucosa_paciente_00' + pi + '.png'            #PATH


    print("--Importamos fichero...")
    glucose = pd.read_csv(path_fichero_glucosa)        #r'C:\Users\apula\PycharmProjects\PrediccionGlucosa\D1NAMO\diabetes_subset\001\glucose.csv'
    # print(glucose.shape[0])
    eje_x = np.arange(glucose.shape[0])
    # print(eje_x.shape)
    dim = 20  # elements showed in the zoom
    print(eje_x)
    print(eje_x[:dim])

    # Creates two subplots and unpacks the output array immediately
    f, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey=True, figsize=(18, 4))
    ax1.set_title('Patient 1 Glucose levels')
    ax1.set(xlabel='Time instant (sample)', ylabel='Glucose level (mmol/L)')
    ax1.margins(0.05)  # Default margin is 0.05, value 0 means fit
    ax1.plot(eje_x, glucose['glucose'], color='red', label='glucose')
    leg = ax1.legend()

    ax2.set_title('Zoomed in')
    ax2.set(xlabel='Time instant (sample)', ylabel='Glucose level (mmol/L)')
    ax2.margins(0.00)  # Default margin is 0.05, value 0 means fit
    ax2.plot(eje_x[:dim], glucose['glucose'][:dim], color='red', label='glucose')
    leg = ax2.legend()

    ax3.set_title('Zoomed in')
    ax3.set(xlabel='Time instant (sample)', ylabel='Glucose level (mmol/L)')
    ax3.margins(x=-0.3, y=0)  # Values in (-0.5, 0.0) zooms in to center
    ax3.plot(eje_x, glucose['glucose'], color='red', label='glucose')
    leg = ax3.legend()


    print("--Guardamos gráfica...")
    plt.savefig(path_glucosa)

    plt.show()