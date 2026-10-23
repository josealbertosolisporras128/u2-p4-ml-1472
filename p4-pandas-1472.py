import pandas as pd
import numpy as np
# jose solis nc 1472
n_filas = 5
n_columnas = 5
tag_columna = tuple('ABCDE') # etiquetas para las columnas de una tupla
print(tag_columna)
matriz = np.random.randint(1, 7, size=(n_filas, n_columnas))
print("genera matriz de 5 filas por 5 columnas")
print("con numeros aleatorios comprendidos entre 1 y 10")
print(matriz)
# la variable df es dataframe
df = pd.DataFrame(matriz, columns= tag_columna)
print("------- la tabla o data frame -------")
print(df)
print("----jose solis nc 1472-----")
