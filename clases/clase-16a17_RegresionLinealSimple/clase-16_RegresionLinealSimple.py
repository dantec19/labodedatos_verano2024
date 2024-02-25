# -*- coding: utf-8 -*-
"""
Materia     : Laboratorio de datos - FCEyN - UBA
Clase       : Clase Regresion Lineal
Detalle     : Modelo de Regresion Lineal Simple
Autores     : Maria Soledad Fernandez y Pablo Turjanski
Modificacion: 2023-10-13
"""

# Importamos bibliotecas
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import seaborn as sns
from inline_sql import sql, sql_val

#%%
####################################################################
########  DEFINICION DE FUNCIONES AUXILIARES
####################################################################

# Dibuja una recta. Toma como parametros pendiente e intercept
def plotRectaRegresion(slope, intercept):
    """Plot a line from slope and intercept"""
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, color="red")

#%%

####################################################################
########  MAIN
####################################################################
# Cargamos el archivo 
carpeta = 'datasets/'
data_train = pd.read_csv(carpeta + "datos_roundup.txt", sep=" ", encoding='utf-8')


# ----------------------------------
# ----------------------------------
#       Modelo Lineal Simple (rls)
# ----------------------------------
# ----------------------------------
#  X = RU (variable predictora) [Dosis de Roundup]
#  Y = ID (variable a predecir) [Damage Index]
########################
## Generacion del modelo
########################
# Declaramos las variables

X = data_train[['RU']]
Y = data_train[['ID']]
# Declaramos el tipo de modelo
rls = linear_model.LinearRegression()

# Entrenamos el modelo
rls.fit(X, Y)

# Observamos los valores obtenidos (pendiente e intercept)
print("Coeficientes")
print("=============")
print("     intercept :  ", rls.intercept_[0])
print("     pendiente :  ", rls.coef_[0][0])

###############################################
## Visualizacion del modelo vs valores de TRAIN
###############################################
# Graficamos una dispersion de puntos de ID en funcion de la Dosis de RU

ax = sns.scatterplot(data= data_train, x = 'RU', y = 'ID', s = 40, color = 'black')

ax.set_xlabel("Dosis de RU (ug/huevo)")
ax.set_ylabel("Indice d Daño")
plotRectaRegresion(rls.coef_[0][0], rls.intercept_[0])


#####################################
## Prediccion
#####################################
# Cargamos el archivo (no posee valores para ID)
data_a_predecir = pd.read_csv(carpeta + "datos_a_predecir.txt", sep=" ", encoding='utf-8')

# Realizamos la prediccion de ID utilizando el modelo y
# la asignamos a la columna ID
data_a_predecir[['ID']] = rls.predict(data_a_predecir[['RU']])

# Graficamos una dispersion de puntos de ID en funcion de la Dosis de RU
# Graficamos tanto los puntos de entrenamiento del modelo como los predichos

ax = sns.scatterplot(data= data_train, x = 'RU', y = 'ID', s = 40, color = 'black')

ax = sns.scatterplot(data= data_a_predecir, x = 'RU', y = 'ID', s = 40, color = 'red')

ax.set_xlabel("Dosis de RU (ug/huevo)")
ax.set_ylabel("Indice d Daño")
plotRectaRegresion(rls.coef_[0][0], rls.intercept_[0])

#####################################
## Evaluacion del modelo contra TRAIN
#####################################
#  R2


data_libreta = pd.read_csv(carpeta + "datos_libreta_90622.txt", sep=" ", encoding='utf-8')

X = data_libreta [['RU']]
Y = data_libreta [['ID']]
rls = linear_model.LinearRegression()

rls.fit(X, Y)

rls.score(X, Y)

ax = sns.scatterplot(data= data_train, x = 'RU', y = 'ID', s = 40, color = 'black')
ax = sns.scatterplot(data= data_libreta, x = 'RU', y = 'ID', s = 40, color = 'red')

ax.set_xlabel("Dosis de RU (ug/huevo)")
ax.set_ylabel("Indice d Daño")
plotRectaRegresion(rls.coef_[0][0], rls.intercept_[0])

X = data_libreta [['Ordenada estimada']]
Y = data_libreta [['Pendiente estimada']]

fig, ax = plt.subplots()
plt.hist([X,Y])
plt.show()


#%%

########################
# Declaramos las variables

X = data_train[['RU']]
Y = data_train[['ID']]
# Declaramos el tipo de modelo
rls = linear_model.LinearRegression()

# Entrenamos el modelo
rls.fit(X, Y)

# Observamos los valores obtenidos (pendiente e intercept)
print("Coeficientes")
print("=============")
print("     intercept :  ", rls.intercept_[0])
print("     pendiente :  ", rls.coef_[0][0])

###############################################
## Visualizacion del modelo vs valores de TRAIN
###############################################
# Graficamos una dispersion de puntos de ID en funcion de la Dosis de RU

ax = sns.scatterplot(data= data_train, x = 'RU', y = 'ID', s = 40, color = 'black')

ax.set_xlabel("Dosis de RU (ug/huevo)")
ax.set_ylabel("Indice d Daño")
plotRectaRegresion(rls.coef_[0][0], rls.intercept_[0])


