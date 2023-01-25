import pandas as pd
import numpy as np

from scores.boxplot import crear_boxplot_pacientes
from scores.boxplot import crear_boxplot_experimentos

from scores.mean_score import media_resultados_pacientes
from scores.mean_score_graph import crear_grafica_media_resultados_pacientes


def bloque_scores(cn, en, path_scores_dataset_processed, path_dataset_scores, path_boxplot, path_processed_scores_dataset, pacientes):
    print("-BLOQUE SCORES: CREAR BOXPLOTS...")
    crear_boxplot_pacientes(cn, en, path_scores_dataset_processed, path_boxplot, pacientes)
    #crear_boxplot_experimentos(cn, en, path_scores_dataset_processed, path_boxplot, pacientes)


    print("-BLOQUE SCORES: CREAR GRAFICAS CON SCORES...")
    #media_resultados_pacientes(cn, path_scores_dataset_processed, path_processed_scores_dataset, pacientes)
    #crear_grafica_media_resultados_pacientes(cn, path_scores_dataset_processed, path_processed_scores_dataset, pacientes)