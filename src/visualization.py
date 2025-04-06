import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def grafico_dispersao(df):
    """
    Produz um gráfico de dispersão para "Sleep_Hours_per_Night" x "Final_Score".
    
    Args:
        df (pd.DataFrame): DataFrame contendo os dados limpos.
    """
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x="Sleep_Hours_per_Night", y="Final_Score", color="blue", alpha=0.6)
    plt.title("Gráfico de Dispersão: Horas de Sono x Nota Final", fontsize=14)
    plt.xlabel("Horas de Sono por Noite", fontsize=12)
    plt.ylabel("Nota Final", fontsize=12)
    plt.grid(True, alpha=0.4)
    plt.show()

def grafico_barras_idade_x_midterm(df):
    """
    Produz um gráfico de barras relacionando Idade (Age) e a média das notas intermediárias (Midterm_Score).
    
    Args:
        df (pd.DataFrame): DataFrame contendo os dados limpos.
    """
    # Agrupa os dados pela idade e calcula a média das notas intermediárias
    medias_por_idade = df.groupby("Age")["Midterm_Score"].mean()

    # Configura e cria o gráfico de barras
    plt.figure(figsize=(10, 6))
    sns.barplot(x=medias_por_idade.index, y=medias_por_idade.values, palette="Blues_d")
    plt.title("Gráfico de Barras: Idade x Média das Notas Intermediárias", fontsize=14)
    plt.xlabel("Idade", fontsize=12)
    plt.ylabel("Média das Notas Intermediárias", fontsize=12)
    plt.xticks(rotation=45)  # Rotaciona os rótulos no eixo X, se necessário
    plt.grid(axis="y", alpha=0.4)
    plt.show()

def grafico_pizza_idades(df):
    """
    Produz um gráfico de pizza para as idades agrupadas em faixas etárias.
    
    Args:
        df (pd.DataFrame): DataFrame contendo os dados limpos.
    """
    # Define faixas etárias
    faixas = ["Até 17", "18 a 21", "21 a 24", "25 ou mais"]
    df["Faixa_Etaria"] = pd.cut(df["Age"], bins=[0, 17, 21, 24, float("inf")], labels=faixas)

    # Conta a quantidade de estudantes por faixa etária
    proporcoes = df["Faixa_Etaria"].value_counts()

    # Gera o gráfico de pizza
    plt.figure(figsize=(8, 8))
    plt.pie(proporcoes, labels=proporcoes.index, autopct="%1.1f%%", startangle=90, colors=["#FF9999", "#66B3FF", "#99FF99", "#FFCC99"])
    plt.title("Distribuição das Idades Agrupadas", fontsize=14)
    plt.show()
