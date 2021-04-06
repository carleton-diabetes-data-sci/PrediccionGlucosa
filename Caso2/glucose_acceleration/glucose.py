import pandas as pd
import numpy as np
import os
import sys
import matplotlib.pyplot as plt

def crear_grafica_glucosa(root, path):
    #p = os.path.join(root, "001\glucose.csv")       #p = root + r'\001\glucose.csv'  r'C:\Users\apula\PycharmProjects\PrediccionGlucosa\Caso2\D1NAMO\diabetes_subset\001\glucose.csv'
    #glucose = pd.read_csv(os.path.join(root, '001\glucose.csv'))
    glucose = pd.read_csv(r"C:\Users\apula\PycharmProjects\PrediccionGlucosa\D1NAMO\diabetes_subset\001\glucose.csv")

    # (glucose)
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



    plt.savefig(path)

    plt.show()