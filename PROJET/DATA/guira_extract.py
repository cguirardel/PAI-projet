
import pandas as pd
import numpy as np


file = pd.read_csv("DATA/dataset_olympics.csv")


sports = np.sort(pd.unique(file.Sport))