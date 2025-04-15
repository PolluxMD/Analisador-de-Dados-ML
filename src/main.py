from logger import validar_nome_usuario, registrar_acao
from data_loader import carregar_dados_usuario
from data_cleaner import limpar_dados
from resume_data import gerar_resumo_dados
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

def exibir_menu():
    while True:
        print("\nMenu:")
        print("1 - Escolher uma Coluna para análise")
        print("2 - Gráfico de Dispersão (Horas de Sono x Nota Final)")
        print("3 - Gráfico de Barras (Idade x Média das Notas Intermediárias)")
        print("4 - Gráfico de Pizza (Distribuição das Idades Agrupadas)")
        print("5 - Sair")

        escolha = input("Escolha uma opção (1, 2, 3, 4 ou 5): ")

        if escolha in ["1", "2", "3", "4", "5"]:
            return escolha
        else:
            print("Opção inválida! Por favor, escolha um número entre 1 e 5.")

def exibir_submenu(df_cleaned, df_raw):
    from data_cleaner import limpar_dados_visual

    while True:
        print("\nSubmenu - Visualizar Dados:")
        print("1. Exibir resumo dos dados")
        print("2. Exibir estatísticas por coluna específica")
        print("3. Voltar ao menu principal")

        escolha = input("Escolha uma opção (1, 2, 3): ")

        if escolha == "1":
            print("\nResumo dos Dados:")
            limpar_dados_visual(df_raw)

        elif escolha == "2":
            print("\nPreview dos dados limpos:")
            print(df_cleaned.head())

            coluna_usuario = input("\nDigite o nome da coluna que deseja visualizar estatísticas: ")
            if validar_coluna(df_cleaned, coluna_usuario):
                print(f"\nEstatísticas da coluna '{coluna_usuario}':")
                print(f"Média: {calcular_media(df_cleaned, coluna_usuario):.2f}")
                print(f"Mediana: {calcular_mediana(df_cleaned, coluna_usuario):.2f}")
                print(f"Moda: {calcular_moda(df_cleaned, coluna_usuario)}")
                print(f"Desvio Padrão: {calcular_desvio_padrao(df_cleaned, coluna_usuario):.2f}")
            else:
                print("Erro: A coluna escolhida não é válida ou não é numérica.")

        elif escolha == "3":
            print("\nVoltando ao menu principal...")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    while True:
        nome_usuario = input("Digite seu nome: ")
        if validar_nome_usuario(nome_usuario):
            registrar_acao(nome_usuario, "Iniciou o sistema")
            break
        else:
            print("Nome inválido. Certifique-se de que tem ao menos 3 caracteres e contém apenas letras.")

    df_raw = carregar_dados_usuario()
    if df_raw is not None:
        df_cleaned, total_attendance = limpar_dados(df_raw)
        registrar_acao(nome_usuario, "Carregou e limpou os dados")

        print("\nBem-vindo ao sistema de análise de dados!\n")

        while True:
            escolha = exibir_menu()
            registrar_acao(nome_usuario, f"Escolheu a opção {escolha} no menu")

            if escolha == "1":
                print("Opção 1: Escolhendo uma coluna para análise")
                exibir_submenu(df_cleaned, df_raw)
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
