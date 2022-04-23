import pandas as pd
import numpy as np
import math
from matplotlib import cm
import matplotlib.pyplot as plt

# Criar a tabela
np.random.seed(12345)
df = pd.DataFrame([np.random.normal(32000,200000,3650), np.random.normal(43000,100000,3650), 
                   np.random.normal(43500,140000,3650), np.random.normal(48000,70000,3650)], 
                  index=['A','B','C','D'])
df

# Inverter a tabela e ver as metricas
df = df.transpose()
df.describe()

# Calcular o intervalo de confianca para cada variavel 
mean = list(df.mean())
std = list(df.std())
letter_1 = []

for i in range (4) :
    letter_1.append(1.96*(std[i]/math.sqrt(len(df))))
    
letter_1

nearest = 100
Y = 35000

df_p = pd.DataFrame()
df_p['diff'] = nearest * ((Y - df.mean())//nearest)
df_p['sign'] = df_p['diff'].abs()/df_p['diff']
old_range = abs(df_p['diff']).min(), df_p['diff'].abs().max()
new_range = .5,1
df_p['shade'] = df_p['sign']*np.interp(df_p['diff'].abs(), old_range, new_range)

# Cores das barras
shade = list(df_p['shade'])

blues = cm.Blues
reds = cm.Reds

# Azul se positivo e vermelho se negativo
color = ['White' if  x == 0 else reds(abs(x))
         if x<0 else blues(abs(x)) for x in shade]

# Grafico
%matplotlib inline

plt.figure(num = None, figsize = (6, 6), dpi = 80, facecolor = 'w', edgecolor = 'k')
plt.bar(range(len(df.columns)), height = df.values.mean(axis = 0), 
        yerr = letter_1, error_kw = {'capsize': 10, 'elinewidth': 2, 'alpha':0.7}, color = color)

plt.axhline(y=Y, color = 'black', label = 'Y')
plt.text(3.5, 35000, "35000")
plt.xticks(range(len(df.columns)), df.columns)
plt.title('Generated Data between A, B, C and D')

plt.tick_params(top='off', bottom='off',  right='off', labelbottom='on')

for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.show()
