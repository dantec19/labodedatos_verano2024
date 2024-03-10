from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from func_aux import atributos_random
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV


def resultados_knn(df, cant_vecinos, cant_atributos, matriz_confusion=False):
    """
    Calcula y devuelve la precisión de un modelo KNN en un conjunto de datos.

    Parametros:
        - df (DataFrame): DataFrame que contiene los datos.
        - cant_vecinos (int): Número de vecinos a considerar en el modelo KNN.
        - cant_atributos (int): Número de atributos a utilizar en el modelo.
        - matriz_confusion (bool, opcional): Indica si se debe mostrar la matriz de confusión. Por defecto, False.

    Devuelve:
        float: Precisión del modelo KNN en el conjunto de prueba.
    """
    atributos = atributos_random(cant_atributos)

    X = df[list(map(lambda a: "pixel" + str(a), atributos))]
    y = df["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    neigh = KNeighborsClassifier(n_neighbors=cant_vecinos)
    neigh.fit(X_train, y_train)

    score = neigh.score(X_test, y_test)

    if matriz_confusion:
        labels = y_test.unique()
        y_pred = neigh.predict(X_test)
        ax = plt.subplot()
        ax.set_title(
            f"cant_atributos: {cant_atributos}, k: {cant_vecinos}, score = {score}"
        )
        generar_matriz_confusion(y_test, y_pred, labels, ax)

    return score


def obtener_mejores_hiperparametros(
    dicc_hiperparametros, X_dev, y_dev, ver_detalles=False
):
    """
    Realiza una búsqueda de hiperparámetros óptimos para un clasificador de árboles de decisión.

    Parameters:
        - dicc_hiperparametros (dict): Diccionario con los hiperparámetros a ajustar.
        - X_dev (array-like): Conjunto de características de desarrollo.
        - y_dev (array-like): Etiquetas de desarrollo.
        - ver_detalles (bool, opcional): Indica si se deben mostrar detalles de la búsqueda. Por defecto, False.

    Devuelve:
        dict: Mejores hiperparámetros encontrados.
    """
    arbol = DecisionTreeClassifier()
    clf = GridSearchCV(arbol, dicc_hiperparametros)
    search = clf.fit(X_dev, y_dev)
    if ver_detalles:
        print(search.cv_results_)
    return search.best_params_


def evaluar_mejores_hiperparametros(
    hiperparametros, X_dev, X_eval, y_dev, y_eval, matriz_confusion=True
):
    """
    Evalúa el rendimiento de un modelo de árbol de decisión con los mejores hiperparámetros en un conjunto de evaluación.

    Parametros:
        - hiperparametros (dict): Mejores hiperparámetros encontrados.
        - X_dev (array-like): Conjunto de características de desarrollo.
        - X_eval (array-like): Conjunto de características de evaluación.
        - y_dev (array-like): Etiquetas de desarrollo.
        - y_eval (array-like): Etiquetas de evaluación.
        - matriz_confusion (bool, opcional): Indica si se debe mostrar la matriz de confusión. Por defecto, True.
        
    Devuelve:
        None
    """
    arbol = DecisionTreeClassifier(
        criterion=hiperparametros["criterion"],
        max_depth=hiperparametros["max_depth"],
        random_state=0,
    )
    arbol.fit(X_dev, y_dev)
    y_pred = arbol.predict(X_eval)
    score = arbol.score(X_eval, y_eval)

    ax = plt.subplot()
    ax.set_title(
        f"Criterio: {hiperparametros['criterion']}, Profundidad: {hiperparametros['max_depth']}, score={score}"
    )
    conf_matrix_display = ConfusionMatrixDisplay(
        confusion_matrix(y_eval, y_pred), display_labels=["A", "E", "I", "O", "U"]
    )
    conf_matrix_display.plot(ax=ax)

    plt.rcParams["figure.figsize"] = (10, 6)
    plt.show()


def generar_matriz_confusion(y_test, y_pred, labels, ax):
    
    """
    Genera y muestra la matriz de confusión.

    Parameters:
        - y_test (array-like): Etiquetas reales.
        - y_pred (array-like): Etiquetas predichas.
        - labels (list): Lista de etiquetas de clases.
        - ax (Axes): Objeto AxesSubplot de Matplotlib.
        
    Devuelve:
        None
    """
    
    conf_matrix_display = ConfusionMatrixDisplay(
        confusion_matrix(y_test, y_pred), display_labels=labels
    )
    conf_matrix_display.plot(ax=ax)

    plt.rcParams["figure.figsize"] = (10, 6)
    plt.show()