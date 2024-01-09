
import pandas as pd
import numpy as np


file = pd.read_csv("Modules_traitement/data/dataset_olympics.csv")


sports = np.sort(pd.unique(file.Sport))
liste_sports = ["-",'Tous sports confondus']+list(sports)