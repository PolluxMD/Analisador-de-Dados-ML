from data_loader import carregar_dados
from data_cleaner import limpar_dados
from data_analysis import (
    validar_coluna,
    calcular_media,
    calcular_mediana,
    calcular_moda,
    calcular_desvio_padrao
)
from visualization import (
    grafico_dispersao,
    grafico_barras_idade_x_midterm,
    grafico_pizza_idades
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
    print("2. Gráfico de Dispersão (Horas de Sono x Nota Final)")
    print("3. Gráfico de Barras (Idade x Média das Notas Intermediária")
    print("4. Gráfico de Pizza para as idadess)")
    print("5. Sair)")
    escolha = input("Escolha uma opção (1, 2, 3, 4 ou 5): ")
    return escolha

if __name__ == "__main__":
    # Carrega os dados
    df = carregar_dados()
    if df is not None:
        # Limpa os dados
        df_cleaned, _ = limpar_dados(df)
        
        print("Bem-vindo ao sistema de análise de dados!\n")
        while True:
            # Exibe o menu de opções
            escolha = exibir_menu()
            
            if escolha == "1":
                # Solicita a coluna para análise
                coluna_usuario = input("\nDigite o nome da coluna que deseja analisar: ")
                
                # Valida a coluna escolhida
                if validar_coluna(df_cleaned, coluna_usuario):
                    print(f"\nAnalisando a coluna '{coluna_usuario}'...")
                    print(f"Média: {calcular_media(df_cleaned, coluna_usuario):.2f}")
                    print(f"Mediana: {calcular_mediana(df_cleaned, coluna_usuario):.2f}")
                    print(f"Moda: {calcular_moda(df_cleaned, coluna_usuario)}")
                    print(f"Desvio Padrão: {calcular_desvio_padrao(df_cleaned, coluna_usuario):.2f}")
                else:
                    print("Por favor, tente novamente com uma coluna válida.")

            elif escolha == "2":
                # Exibe o gráfico de dispersão
                print("\nGerando gráfico de dispersão...")
                grafico_dispersao(df_cleaned)
              
                     
            elif escolha == "3":
                # Exibe o gráfico de barras
                print("\nGerando gráfico de barras para Idade x Média das Notas Intermediárias...")
                grafico_barras_idade_x_midterm(df_cleaned)
                
            
            elif escolha == "4":
                # Exibe o gráfico de pizza
                print("\nGerando gráfico de pizza para distribuição das idades agrupadas...")
                grafico_pizza_idades(df_cleaned)
            

            elif escolha == "5":
                print("\nObrigado por utilizar o sistema! Até mais.")
                break
            
            else:
                print("Opção inválida. Por favor, escolha 1, 2, 3, 4 ou 5.")