import pandas as pd

from data_cleaner import clean_data
from data_analysis import plot_data

# Carregar o arquivo CSV
df = pd.read_json(r"C:\Users\erica\OneDrive\Semestre 5 2k25 - Análise e Desenvolvimento de Sistemas\MachineLeaning\Analisador_De_Dados\Analisador-de-Dados-ML\data\Students_Grading_Dataset.json")

# Visualizar as primeiras linhas do dataset
#print(df.head())

# Mostrar informações gerais
#print(df.info())

# Resumo estatístico
#print(df.describe())

# Conta valores nulos em cada coluna
#print(df.isnull().sum())

# Conta as duplicatas
#print(df.duplicated().sum()) 

