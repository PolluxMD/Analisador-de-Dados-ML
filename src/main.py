from data_cleaner import limpar_dados
from data_loader import carregar_dados
from data_analysis import (
    validar_coluna,
    calcular_media,
    calcular_mediana,
    calcular_moda,
    calcular_desvio_padrao
)

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

def exibir_menu():
    """
    Exibe o menu de opções para o usuário.
    """
    print("\nMenu:")
    print("1. Escolher uma coluna para análise")
    print("2. Sair")
    escolha = input("Escolha uma opção (1 ou 2): ")
    return escolha



from data_loader import carregar_dados
from data_analysis import (
    validar_coluna,
    calcular_media,
    calcular_mediana,
    calcular_moda,
    calcular_desvio_padrao
)

def exibir_menu():
    """
    Exibe o menu de opções para o usuário.
    """
    print("\nMenu:")
    print("1. Escolher uma coluna para análise")
    print("2. Sair")
    escolha = input("Escolha uma opção (1 ou 2): ")
    return escolha

if __name__ == "__main__":
    # Carrega os dados
    df = carregar_dados()
    if df is not None:
        print("Bem-vindo ao sistema de análise de dados!\n")

        while True:
            # Exibe o menu de opções
            escolha = exibir_menu()
            
            if escolha == "1":
                # Solicita a coluna para análise
                coluna_usuario = input("\nDigite o nome da coluna que deseja analisar: ")
                
                # Valida a coluna escolhida
                if validar_coluna(df, coluna_usuario):
                    print(f"\nAnalisando a coluna '{coluna_usuario}'...")
                    print(f"Média: {calcular_media(df, coluna_usuario):.2f}")
                    print(f"Mediana: {calcular_mediana(df, coluna_usuario):.2f}")
                    print(f"Moda: {calcular_moda(df, coluna_usuario)}")
                    print(f"Desvio Padrão: {calcular_desvio_padrao(df, coluna_usuario):.2f}")
                else:
                    print("Por favor, tente novamente com uma coluna válida.")
            
            elif escolha == "2":
                print("\nObrigado por utilizar o sistema! Até mais.")
                break
            
            else:
                print("Opção inválida. Por favor, escolha 1 ou 2.")






