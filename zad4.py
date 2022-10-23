import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dataFrame = pd.read_excel("practice_lab_1.xlsx", sep=";") # otwarcie pliku
columnNames = list(dataFrame.columns) # nazwy kolumn
correlationArray = dataFrame.corr() # macierz korelacji 7x7

fig, ax = plt.subplots(len(columnNames), len(columnNames), figsize=(10,10))
for i in range(len(columnNames)):
    for j in range(len(columnNames)):
        ax[i,j].scatter(dataFrame.iloc[:,i], dataFrame.iloc[:,j])

plt.show()