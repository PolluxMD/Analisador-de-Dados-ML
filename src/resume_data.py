def gerar_resumo_dados(df):
    """
    Gera um resumo estatístico do DataFrame carregado.

    Args:
        df (pd.DataFrame): DataFrame contendo os dados limpos.

    Returns:
        dict: Resumo estatístico contendo:
            - Quantidade de registros.
            - Quantidade de homens e mulheres.
            - Quantidade de registros sem dados sobre a educação dos pais.
    """
    resumo = {}

    # Quantidade de registros totais
    resumo["Quantidade de Registros"] = len(df)

    # Quantidade de homens e mulheres
    if "Gender" in df.columns:
        resumo["Homens"] = df["Gender"].value_counts().get("Male", 0)
        resumo["Mulheres"] = df["Gender"].value_counts().get("Female", 0)
    else:
        resumo["Homens"] = resumo["Mulheres"] = "Coluna 'Gender' não encontrada"

    # Quantidade de registros sem dados sobre a educação dos pais
    if "Parent_Education_Level" in df.columns:
        resumo["Sem Dados sobre Educação dos Pais"] = df["Parent_Education_Level"].isna().sum()
    else:
        resumo["Sem Dados sobre Educação dos Pais"] = "Coluna 'Parent_Education_Level' não encontrada"

    return resumo