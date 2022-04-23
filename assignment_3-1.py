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
