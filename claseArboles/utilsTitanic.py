"""
"""

from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def cargar_datos(file, filter = True):
    df = pd.read_csv(file, index_col=0)
    df = df.dropna()
    if filter: 
        df = df.drop(columns = ["Name", "Ticket",  "Cabin", "Embarked"])
    X = df.drop(columns = ["Survived"]) 
    y = df.Survived
    return df, X, y

def cargar_datos_test(file):
    df_test, X_test, y_test = cargar_datos(file, False)
    X_test = encode_sex_column(X_test)
    X_test.columns
    X_test = X_test.drop(columns =['PassengerId'])
    return X_test, y_test

def cargar_datos_competencia(file):
    X_test= pd.read_csv(file, index_col=0)
    X_test = encode_sex_column(X_test)
    X_test.columns
    X_test = X_test.drop(columns =['PassengerId'])
    return X_test

def encode_sex_column(X):
    cols = ['Sex']
    encode_sex = OneHotEncoder(sparse_output=False, drop="first") #female = 0 and male = 1 
    encode_sex.fit(X[cols])
    transformed_sex = encode_sex.transform(X[cols])
    X['Sex'] = transformed_sex
    return X


## Gráficos 
def plot_histogramas(df):
    df.hist(figsize= (15, 10))
    plt.show()
    return 

def plot_pairplot_hue_survived(df):
    sns.pairplot(df, hue = "Survived", diag_kind="hist")
    plt.show()
    return

def plot_pairplot_hue_sex(df):
    df_filtrado = df[["Sex", "Pclass","Age",  "Survived"]]
    sns.pairplot(df_filtrado, hue = "Sex", diag_kind="hist")
    plt.show()
    return

def plot_paiplot_hue_survived_filtered(df):
    df_filtrado = df[["Pclass","Age",  "Survived"]]
    sns.pairplot(df_filtrado, hue = "Survived", diag_kind="hist")
    plt.show()
    return

def plot_hist_sex_survived(df):
    sns.histplot(df, x = "Sex" , hue= "Survived", multiple="stack", palette= "Set2", legend=False)
    plt.legend(title='Survived', loc='upper right', labels=['Si', 'No'])
    #plt.savefig("hist_sex_survived.png")
    return

def plot_hist_age_survived(df):
    sns.histplot(df, x = "Age" , hue= "Survived", multiple="stack", legend=False)
    plt.legend(title='Survived', loc='upper right', labels=['Si', 'No'])    
    return

#Score
def score(y_predict, y):
    print("Le pegaste a " + str(np.sum(y_predict == y)) + " instancias de " + str(y.size)) 