from data_cleaner import limpar_dados
from data_loader import carregar_dados

# Exemplo de uso no main.py
if __name__ == "__main__":
    df = carregar_dados()  # Carrega os dados
    if df is not None:
        df_cleaned, total_attendance = limpar_dados(df)  # Limpa os dados
        print("Dados limpos com sucesso!")
        print(f"Somatório de 'Attendance (%)': {total_attendance}")
        print(df_cleaned.head())  # Exibe as 5 primeiras linhas dos dados limpos

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

