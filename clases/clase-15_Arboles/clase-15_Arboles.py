#!/usr/bin/env python
# coding: utf-8

# ## Podemos predecir quienes sobrevivieron en el Titanic? 
# 
# Tenemos un dataset muy famoso con datos de los pasajeros del titanic. El mismo está disponible en: 
# 
# https://www.kaggle.com/c/titanic/data 

# In[1]:


import utilsTitanic as utils
from IPython.display import display
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ### Cargamos los datos

# In[2]:

carpeta = 'datasets/'

df_titanic, X, y = utils.cargar_datos(carpeta + 'titanic_training.csv') # X tiene todas las columnas del dataframe menos la que queremos predecir,
                                        # Y tiene la columna que indica si sobrevivieron
df_titanic.head()


# ### Exploren estos datos!! Ideas: histogramas, pairplots, etc 

# In[3]:


fig, ax = plt.subplots()

plt.rcParams['font.family'] = 'sans-serif'           
plt.rcParams['axes.spines.left']  = False       # Remueve linea derecha  del recuadro

ax.bar(data=df_titanic, x='Age', height='Survived')
       
ax.set_title('Sobrevivieron por edad')
ax.set_xlabel('Age', fontsize='medium')                       
ax.set_ylabel('Survived', fontsize='medium')    
ax.set_xlim(0, 80)
ax.set_ylim(0, 3)

ax.set_xticks(range(1,11,1))                            # Muestra todos los ticks del eje x
ax.set_yticks([])                                       # Remueve los ticks del eje y
ax.bar_label(ax.containers[0], fontsize=8) 


# ## Competencia: Armen sus Reglas !!

def clasificador_naive_instance(x):
   contador = 0
   if x.Fare < 10.49:
      contador += 7
   if x.Pclass == 3:
       contador += 3
   if x.Age > 60:
       contador += 6
   if x.Sex == "male":
       contador += 2
   if x.Pclass == 1:
       contador += 1.5
   if x.SibSp == 0:
       contador += 1
   if x.Fare > 80:
       contador -= 3
   if x.Age <= 28:
       contador -= 3
   if x.Pclass == 3:
       contador += 3
   if x.Age >= 40 and x.Age <= 50:
       contador += 2.5
   return contador <= 2



# In[3]:


def clasificador_naive_instance(x):
    ## Completen con sus reglas por ej
    if x.Pclass == 1:
        return True
    else:
        return False


# In[4]:[True, True, True, True, True, True, True, True, True, True]



def clasificador_naive(X):
    y_predict = []
    for x in X.itertuples(index=False): 
        y_predict.append(clasificador_naive_instance(x))
    return y_predict


# In[5]:


def score(y, y_pred):
    print("Le pego a " + str(np.sum(y==y_pred)) + " de " + str(len(y)))


# #### Usemos nuestro clasificador sobre los datos 

# In[6]:


y_predict = clasificador_naive(X)
score(y_predict, y)


# In[9]:


X_comp = utils.cargar_datos_competencia(carpeta + "titanic_competencia.csv")
y_pred_comp = clasificador_naive(X_comp)
y_pred_comp


# ## Ahora armemos un clasificador usando árboles de decisión

# In[7]:


# Algo de procesamiento de los datos
X = utils.encode_sex_column(X)


# ## Decision Tree
# Para saber más: <https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html>

# In[9]:


# planta tu árbol aquí
from sklearn.tree import DecisionTreeClassifier,plot_tree, export_graphviz
arbol = DecisionTreeClassifier(criterion="entropy", max_depth= 2)
arbol.fit(X, y) #Entrenamiento
prediction = arbol.predict(X)

arbol.score(X, y)

# #### Generamos el gráfico de nuestro árbol
# Para saber más <https://scikit-learn.org/stable/modules/generated/sklearn.tree.export_graphviz.html#sklearn.tree.export_graphviz>

# In[10]:


# plot arbol
import graphviz
dot_data = export_graphviz(arbol, out_file=None, feature_names= X.columns, class_names= ["Not Survived", "Survived"], filled=True, rounded=True, special_characters=True)
graph = graphviz.Source(dot_data) #Armamos el grafo
graph.render("titanic", format= "png") #Guardar la imágen
graph
# ### ¿Cuál es el mejor corte? 

# In[8]:


utils.plot_hist_sex_survived(df_titanic)


# In[9]:


utils.plot_hist_age_survived(df_titanic)


# ## ¿Todos los árboles son iguales?
# 
# veamos dos ejemplos

# In[13]:


## Armar un árbol de altura 2


# In[14]:


## Armar un arbol con altura indefinida


# ## Veamos la performance de estos árboles sobre un conjunto de test

# In[10]:


#Cargamos los datos de tests
X_test, y_test = utils.cargar_datos_test(carpeta + 'test_titanic.csv')


# In[ ]:


# Veamos el score del arbol de altura 2 sobre los datos de entrenamiento y los datos de tests


# In[ ]:


# Veamos el score del arbol de altura inf sobre los datos de entrenamiento y los datos de tests

