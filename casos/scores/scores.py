import pandas as pd
import numpy as np

from casos.scores.boxplot import crear_boxplot
from casos.scores.mean_score import media_resultados_pacientes
from casos.scores.mean_score_graph import crear_grafica_media_resultados_pacientes


def bloque_scores(cn, en, path_scores_dataset_processed, pacientes):
    print("-BLOQUE SCORES: CREAR BOXPLOTS...")
    #crear_boxplot(cn, en, path_scores_dataset_processed, pacientes)
    print("-BLOQUE SCORES: CREAR GRAFICAS CON SCORES...")
    #media_resultados_pacientes(cn, path_scores_dataset_processed, pacientes)
    #crear_grafica_media_resultados_pacientes(cn, path_scores_dataset_processed, pacientes)