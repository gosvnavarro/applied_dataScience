import pandas as pd
import numpy as np

# Criar a tabela
np.random.seed(12345)
df = pd.DataFrame([np.random.normal(32000,200000,3650), np.random.normal(43000,100000,3650), 
                   np.random.normal(43500,140000,3650), np.random.normal(48000,70000,3650)], 
                  index=[A,B,C,D])
df

# Inverter a tabela e ver as metricas
df = df.transpose()
df.describe()

# Calcular o intervalo de confianca para cada variavel 
import math

mean = list(df.mean())
std = list(df.std())
letter_1 = []

for i in range (4) :
    letter_1.append(1.96*(std[i]/math.sqrt(len(df))))
    
letter_1

nearest = 100
Y = 39500

df_p = pd.DataFrame()
df_p['diff'] = nearest * ((Y - df.mean())//nearest)
df_p['sign'] = df_p['diff'].abs()/df_p['diff']
old_range = abs(df_p['diff']).min(), df_p['diff'].abs().max()
new_range = .5,1
df_p['shade'] = df_p['sign']*np.interp(df_p['diff'].abs(), old_range, new_range)
