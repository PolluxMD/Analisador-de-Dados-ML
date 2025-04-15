import pandas as pd

def limpar_dados(df):
    """
    Limpa os dados fornecidos, removendo registros e ajustando valores nulos.

    Args:
        df (pd.DataFrame): DataFrame com os dados carregados.

    Returns:
        tuple: Uma tupla contendo:
            - pd.DataFrame: DataFrame limpo.
            - float: Somatório dos valores da coluna "Attendance (%)".

    Raises:
        KeyError: Se alguma das colunas necessárias não for encontrada.
        ValueError: Se a coluna "Attendance (%)" contiver valores inválidos.
    """
    if df.empty:
        raise ValueError("O DataFrame fornecido está vazio.")

    required_columns = ["Parent_Education_Level", "Attendance (%)"]
    for col in required_columns:
        if col not in df.columns:
            raise KeyError(f"A coluna obrigatória '{col}' não foi encontrada.")

    df_cleaned = df.dropna(subset=["Parent_Education_Level"]).copy()

    if not pd.api.types.is_numeric_dtype(df_cleaned["Attendance (%)"]):
        raise ValueError("A coluna 'Attendance (%)' contém valores não numéricos.")

    median_attendance = df_cleaned["Attendance (%)"].median()
    df_cleaned["Attendance (%)"] = df_cleaned["Attendance (%)"].fillna(median_attendance)

    total_attendance = df_cleaned["Attendance (%)"].sum()

    return df_cleaned, total_attendance


def limpar_dados_visual(df):
    """
    Limpa os dados com exibição passo a passo do processo.

    Args:
        df (pd.DataFrame): DataFrame bruto com os dados.

    Returns:
        pd.DataFrame: DataFrame limpo.
    """
    try:
        print("\n### Etapa 1 - Dados Brutos ###")
        print(df.head())
        print("Valores nulos por coluna:")
        print(df.isnull().sum())
        print(f"Soma inicial de 'Attendance (%)': {df['Attendance (%)'].sum()}")

        df_cleaned, total_attendance = limpar_dados(df)

        print("\n### Etapa 2 - Após Remoção de Registros com 'Parent_Education_Level' Vazio ###")
        print(f"Registros restantes: {len(df_cleaned)}")
        print("Valores nulos restantes:")
        print(df_cleaned.isnull().sum())

        print("\n### Etapa 3 - Após Preenchimento de 'Attendance (%)' com a Mediana ###")
        print(f"Soma final de 'Attendance (%)': {total_attendance}")
        print("Primeiros registros limpos:")
        print(df_cleaned.head())

        return df_cleaned

    except (KeyError, ValueError) as e:
        print(f"Erro durante a limpeza: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

    return None
