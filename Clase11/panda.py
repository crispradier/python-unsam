import pandas as pd
df=pd.read_csv('Data\camion.csv', index_col='precio')
df2=df.to_dict('index')
print(df2[32.2]['nombre'])