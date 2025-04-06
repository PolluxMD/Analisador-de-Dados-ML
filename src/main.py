from logger import validar_nome_usuario, registrar_acao
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
    Exibe o menu de opções para o usuário e garante que a entrada seja válida.
    
    Returns:
        str: Opção escolhida pelo usuário.
    """
    while True:
        print("\nMenu:")
        print("1. Escolher uma coluna para análise")
        print("2. Gráfico de Dispersão (Horas de Sono x Nota Final)")
        print("3. Gráfico de Barras (Idade x Média das Notas Intermediárias)")
        print("4. Gráfico de Pizza (Distribuição das Idades Agrupadas)")
        print("5. Sair")
        
        escolha = input("Escolha uma opção (1, 2, 3, 4 ou 5): ")
        
        if escolha in ["1", "2", "3", "4", "5"]:
            return escolha
        else:
            print("Opção inválida! Por favor, escolha um número entre 1 e 5.")

if __name__ == "__main__":
    # Solicita o nome do usuário
    while True:
        nome_usuario = input("Digite seu nome: ")
        if validar_nome_usuario(nome_usuario):
            registrar_acao(nome_usuario, "Iniciou o sistema")
            break
        else:
            print("Nome inválido. Certifique-se de que tem ao menos 3 caracteres e contém apenas letras.")
    
    # Carrega os dados
    df = carregar_dados()
    if df is not None:
        # Limpa os dados
        df_cleaned, _ = limpar_dados(df)
        registrar_acao(nome_usuario, "Carregou e limpou os dados")
        
        print("Bem-vindo ao sistema de análise de dados!\n")
        
        # Loop do menu principal
        while True:
            # Exibe o menu de opções
            escolha = exibir_menu()
            registrar_acao(nome_usuario, f"Escolheu a opção {escolha} no menu")

            if escolha == "1":
                print("Opção 1: Escolhendo uma coluna para análise")

                # Exibe as 5 primeiras linhas do dataset
                print("\nPreview dos dados:")
                print(df_cleaned.head())
                
                coluna_usuario = input("\nDigite o nome da coluna que deseja analisar: ")
                registrar_acao(nome_usuario, f"Escolheu analisar a coluna '{coluna_usuario}'")
                
                if validar_coluna(df_cleaned, coluna_usuario):
                    print(f"\nAnalisando a coluna '{coluna_usuario}'...")
                    print(f"Média: {calcular_media(df_cleaned, coluna_usuario):.2f}")
                    print(f"Mediana: {calcular_mediana(df_cleaned, coluna_usuario):.2f}")
                    print(f"Moda: {calcular_moda(df_cleaned, coluna_usuario)}")
                    print(f"Desvio Padrão: {calcular_desvio_padrao(df_cleaned, coluna_usuario):.2f}")
                    registrar_acao(nome_usuario, f"Analisou coluna '{coluna_usuario}' com sucesso")
                else:
                    print("Erro: A coluna escolhida não é válida ou não é numérica.")
                    registrar_acao(nome_usuario, f"Falha ao analisar a coluna '{coluna_usuario}'")

            elif escolha == "2":
                print("\nOpção 2: Gerando gráfico de dispersão...")
                registrar_acao(nome_usuario, "Tentou exibir o gráfico de dispersão")
                grafico_dispersao(df_cleaned)

            elif escolha == "3":
                print("\nOpção 3: Gerando gráfico de barras...")
                registrar_acao(nome_usuario, "Tentou exibir o gráfico de barras")
                grafico_barras_idade_x_midterm(df_cleaned)

            elif escolha == "4":
                print("\nOpção 4: Gerando gráfico de pizza...")
                registrar_acao(nome_usuario, "Tentou exibir o gráfico de pizza")
                grafico_pizza_idades(df_cleaned)

            elif escolha == "5":
                print("\nObrigado por utilizar o sistema! Até mais.")
                registrar_acao(nome_usuario, "Encerrou o sistema")
                break

            else:
                print("Opção inválida! Por favor, escolha uma opção válida.")
                registrar_acao(nome_usuario, "Escolheu uma opção inválida no menu")