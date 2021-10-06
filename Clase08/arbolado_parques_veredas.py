import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_veredas=pd.read_csv('../Data/arbolado-publico-lineal-2017-2018.csv', low_memory=False)
df_tipas_veredas=df_veredas[df_veredas['nombre_cientifico']=='Tipuana tipu'].copy()
df_tipas_veredas=df_tipas_veredas[['altura_arbol','diametro_altura_pecho']]
df_tipas_veredas=df_tipas_veredas.rename(columns={"altura_arbol": "altura", "diametro_altura_pecho": "diametro"})
df_tipas_veredas['ambiente']='vereda'


df_parques=pd.read_csv('../Data/arbolado-en-espacios-verdes.csv', low_memory=False)
df_tipas_parques=df_parques[df_parques['nombre_cie']=='Tipuana Tipu'].copy()
df_tipas_parques=df_tipas_parques[['altura_tot','diametro']]
df_tipas_parques=df_tipas_parques.rename(columns={"altura_tot": "altura"})
df_tipas_parques['ambiente']='parque'

df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])
#print(df_tipas)
df_tipas.boxplot(column=['diametro'], by = 'ambiente')
df_tipas.boxplot(column=['altura'], by = 'ambiente')
plt.show() 