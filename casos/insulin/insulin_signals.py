

"""
3.3.1 Generación de señal de asimilación de insulina
A. Defino la función que generará las señales de insulina rápida y lenta como una exponencial creciente y decreciente
"""
def generaSignalInsulina(inicio, pico, duracion):
    signalInsulina = []

    tau_decreciente = -((duracio n -pico ) -1) / np.log(0.01)
    decreciente = signal.exponential((duracio n -pico), 0, tau_decreciente, False)

    tau_creciente = -(pic o -1) / np.log(0.01)
    creciente = signal.exponential(pico ,pico, tau_creciente, False)
    signalInsulina.extend(creciente)
    signalInsulina.extend(decreciente)


    signalInicio = [0] * inicio
    signalInicio.extend(signalInsulina)

    return signalInicio

def crear_grafica_SignalInsulina(signalInicio, path, i_type, duracion):
    plt.figure()
    plt.plot(signalInicio)
    plt.title(str(i_type) + " Insulin " + str(duracion) + " min peak")
    plt.ylabel(str(i_type) + " Insulin (mU/L)")
    plt.xlabel("Time instant (minutes)")

    plt.savefig(path)


"""
B. Modelo Funciones Lineales

Se define las señales de insulina como funciones lineales definidas con 2 expresiones. For simplicity, it is assumed that the glucose intakeGin(t) and insulin infusionIin(t) are periodicpiecewise linear functions defined by the two expressions over a period ofx.

Fuente: W. Haiya, L. Jianxu y K. Yang, “Mathematical modeling and qualitative analysis
of insulin therapies”, vol. 210, 2007. [En línea]. Disponible en: https://www.
sciencedirect.com/science/article/pii/S0025556407001058.

Link: https://reader.elsevier.com/reader/sd/pii/S0025556407001058?token=7C14F1C433E3BE90D86DF6DC85E8D082F1A04F3876F4FD22963FFC7FE832BD3D29F5F2D42A5E811836D871ED028B3D6F


Iin linspro(t)
*   0.25 de 0 a 5 min
*   0.25 + 1 + ((t-30)/(30-5)) de 5 a 30 min
*   0.25 + 1 -((t-30)/(120-30)) de 30 a 120 min
*   0.25 de 120 a 240 min

Iin regular(t)
*   0.25 de 0 a 30 min
*   0.25 + 1 +((t-120)/90) de 30 a 120 min
*   0.25 + 1 -0.5*((t-120)/120) de 120 a 240 min
*   0.25 + 0.5 - 0.5*((t-240)/240) 240 a 480 min

Iin regular30(t)
*   0.25 de 0 a 5 min
*   0.25 + 1 + ((t-30)/(30-5)) de 5 a 30 min
*   0.25 + 1 - 0.5*((t-30)/(150-30)) de 30 a 150 min
*   0.25 + 0.5 - 0.5*((t-150)/(390-150)) de 150 a 390 min
*   0.25 de 390 a 480 min
"""


def generaSignalInsulinaLispro(unidades):
    t = range(0, 241)
    I_in = np.zeros(len(t))

    I_in[0:5] = 0.25
    for x in range(5, 30):
        I_in[x] = 0.25 + unidades * (1 + ((t[x] - 30) / (30 - 5)))
    for x in range(30, 120):
        I_in[x] = 0.25 + unidades * (1 - ((t[x] - 30) / (120 - 30)))

    I_in[120:241] = 0.25

    return I_in


def crear_grafica_SignalInsulinaLispro(ejemploInsulinaLispro, path):
    plt.figure()
    plt.plot(ejemploInsulinaLispro)
    plt.title("Linspro Insulin 30 min peak")
    plt.ylabel("I Linspro Insulin (mU/L)")
    plt.xlabel("Time instant (minutes)")

    plt.savefig(path)


def generaSignalInsulinaRegular(unidades):
    t = range(0, 481)

    I_in = np.zeros(len(t))

    I_in[0:30] = 0.25
    for x in range(30, 120):
        I_in[x] = 0.25 + unidades * (1 + ((t[x] - 120) / (90)))
    for x in range(120, 240):
        I_in[x] = 0.25 + unidades * (1 - 0.5 * ((t[x] - 120) / (120)))
    for x in range(240, 481):
        I_in[x] = 0.25 + unidades * 0.5 * (1 - ((t[x] - 240) / (240)))
    return I_in


def crear_grafica_SignalInsulinaRegular(ejemploInsulinaRegular, path):
    plt.figure()
    plt.plot(ejemploInsulinaRegular)
    plt.title("Regular Insulin 120 min peak")
    plt.ylabel("I Regular Insulin (mU/L)")
    plt.xlabel("Time instant (minutes)")

    plt.savefig(path)


def generaSignalInsulinaRegular30(unidades):
    t = range(0, 481)

    I_in = np.zeros(len(t))

    I_in[0:5] = 0.25
    for x in range(5, 30):
        I_in[x] = 0.25 + unidades * (1 + ((t[x] - 30) / (30 - 5)))
    for x in range(30, 150):
        I_in[x] = 0.25 + unidades * (1 - 0.5 * ((t[x] - 30) / (150 - 30)))
    for x in range(150, 390):
        I_in[x] = 0.25 + unidades * 0.5 * (1 - ((t[x] - 150) / (390 - 150)))
    for x in range(390, 481):
        I_in[x] = 0.25

    return I_in


def crear_grafica_SignalInsulinaRegular30(ejemploInsulinaRegular30, path):
    plt.figure()
    plt.plot(ejemploInsulinaRegular30)
    plt.title("Regular Insulin 30 min peak")
    plt.ylabel("I regular insulin")
    plt.xlabel("Time instant (minutes)")

    plt.savefig(path)


"""
C. Perfiles de insulina
"""


def generaSPerfilInsulinaLispro(unidades):
    lispro_insulin = np.zeros(24 * 60)

    lispro = signal.gaussian(4 * 60, std=30) * 7 * unidades

    for x in range(0, 4 * 60):
        lispro_insulin[x] = lispro[x]

    return lispro_insulin


def generaSPerfilInsulinaRegular(unidades):
    regular_insulin = np.zeros(24 * 60)

    regular = signal.gaussian(8 * 60, std=70) * 5.5 * unidades

    for x in range(0, 8 * 60):
        regular_insulin[x] = regular[x]

    return regular_insulin


def generaSPerfilInsulinaNPH(unidades):
    NPH_insulin = np.zeros(24 * 60)

    NPH_gaussian = signal.gaussian(9 * 60, std=100) * 4 * unidades

    for x in range(0, (4 * 60) + 30):
        NPH_insulin[x] = NPH_gaussian[x]

    for x in range((4 * 60) + 30, 12 * 60):
        NPH_insulin[x] = NPH_insulin[(4 * 60) + 29] - (NPH_insulin[(4 * 60) + 29] - 2.5) / (
                    (12 * 60) - ((4 * 60) + 30)) * (x - ((4 * 60) + 30))

    for x in range(12 * 60, 18 * 60):
        NPH_insulin[x] = NPH_insulin[(12 * 60) - 1] - (NPH_insulin[(12 * 60) - 1]) / ((18 * 60) - ((12 * 60))) * (
                    x - (12 * 60))

    return NPH_insulin


def crear_graficas_perfiles_insulina(path, lispro_insulin, regular_insulin, NPH_insulin):
    eje_x = np.arange(24 * 60)
    fig, ax = plt.subplots()
    ax.plot(eje_x, lispro_insulin, color='red', label='lispro_insulin')
    ax.plot(eje_x, regular_insulin, color='blue', label='regular_insulin')
    ax.plot(eje_x, NPH_insulin, color='green', label='NPH_insulin')
    plt.title('Insuline profiles')
    plt.xlabel('Time instant (minutes)')
    plt.ylabel('Glucose Infusion rate (mg/kg/min)')
    leg = ax.legend()

    plt.savefig(path)

