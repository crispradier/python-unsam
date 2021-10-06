import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def abrir(fname='../Data/arbolado-publico-lineal-2017-2018.csv', cols_sel= ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']):
    df=pd.read_csv(fname, low_memory=False)
    df_lineal=df[cols_sel]
    return df_lineal

def mas_frecuentes(n, df_lineal=abrir()):
    frec = df_lineal['nombre_cientifico'].value_counts()
    print(frec.head(n))

def seleccion_plots(df_lineal=abrir(), especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']):
    df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)]
    df_lineal_seleccion.boxplot(column=['altura_arbol'], by = 'nombre_cientifico')
    sns.pairplot(data = df_lineal_seleccion[['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']], hue = 'nombre_cientifico')
    plt.show()

    


if __name__=='__main__':
    mas_frecuentes(10)
    seleccion_plots()
   
   
    
    