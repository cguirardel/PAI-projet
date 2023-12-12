import pandas as pd
import numpy as np


file = pd.read_csv("DATA/dataset_olympics.csv")

hist = file[file.Medal=='Gold'].groupby('NOC').Medal.count().sort_values()
print(hist)

df = file.loc[:,['NOC','Medal']]
df = df.astype({"NOC":"category"})
df = df[df.Medal=='Gold'].groupby('NOC').Medal.count().sort_values()

print(df)