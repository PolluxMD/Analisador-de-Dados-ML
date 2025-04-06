from data_cleaner import limpar_dados
from data_loader import carregar_dados
from data_loader import carregar_dados
from data_analysis import validar_coluna

if __name__ == "__main__":
    df = carregar_dados()  # Carrega os dados
    if df is not None:
        coluna_usuario = input("Digite o nome da coluna que deseja analisar: ")
        
        if validar_coluna(df, coluna_usuario):
            print(f"A coluna '{coluna_usuario}' é válida para análise.")
        else:
            print("Por favor, tente novamente com uma coluna válida.")


import pandas as pd

def limpar_dados(df):
    """
    Limpa os dados fornecidos, removendo registros e ajustando valores nulos.
    
    - Remove registros onde a coluna "Parent_Education_Level" está vazia.
    - Preenche valores nulos na coluna "Attendance (%)" com a mediana da própria coluna.
    - Calcula e retorna o somatório dos valores da coluna "Attendance (%)".
    
    Args:
        df (pd.DataFrame): DataFrame com os dados carregados.
    
    Returns:
        pd.DataFrame: DataFrame limpo.
        float: Somatório dos valores da coluna "Attendance (%)".
    """
    # Remove registros onde a coluna "Parent_Education_Level" está vazia
    df_cleaned = df.dropna(subset=["Parent_Education_Level"]).copy()  # Garante uma cópia independente

    # Preenche os valores nulos na coluna "Attendance (%)" com a mediana
    median_attendance = df_cleaned["Attendance (%)"].median()
    df_cleaned["Attendance (%)"] = df_cleaned["Attendance (%)"].fillna(median_attendance)

    # Calcula o somatório da coluna "Attendance (%)"
    total_attendance = df_cleaned["Attendance (%)"].sum()

    return df_cleaned, total_attendance