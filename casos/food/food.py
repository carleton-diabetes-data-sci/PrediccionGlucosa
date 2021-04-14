from casos.food.food_signal import crear_grafica_comidas_Procesadas
from casos.food.food_graph import crear_grafica_comidasExp
from casos.food.food_add import anadeComidaProcesada

def bloque_comida(cn, pi, patient_digit, path_food_graphs, path_food_dataset, path_gai_dataset_processed, path_food_dataset_processed, path_full_dataset_processed, posicion_glucosa, pacientes):
    print("PREPARAR DATOS DE COMIDA")
    print("-Se genera la gráfica de las comidas procesadas del paciente 1...")        #food_signal.py
    #crear_grafica_comidas_Procesadas(cn, pi, patient_digit, path_food_graphs, posicion_glucosa, pacientes)
    print("-Se procesa los deltas de comida ...")
    ###procesaDatosComidas(root, pacientes, posicion_glucosa)      #Error in dia and comidaProcesada shape
    print("-Se genera la gráfica de comida Exponencial ...")                         #food_graph.py
    #crear_grafica_comidasExp(cn, pi, patient_digit, path_food_graphs, path_food_dataset_processed, posicion_glucosa, pacientes)
    print("-Se anade la comida procesada ...")                #Depends of insulin
    anadeComidaProcesada(cn, pi, patient_digit, path_gai_dataset_processed, path_food_dataset_processed,  path_full_dataset_processed, posicion_glucosa, pacientes)
