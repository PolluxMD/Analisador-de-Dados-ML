import pandas as pd

# Carregar o arquivo JSON
df = pd.read_json("data/Students_Grading_Dataset.json")

# Mostrar as primeiras linhas
print(df.head())