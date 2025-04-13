import pandas as pd

def limpar_dados(df):
    """
    Limpa os dados fornecidos, removendo registros e ajustando valores nulos.
    
    - Remove registros onde "Parent_Education_Level" está vazia.
    - Preenche valores nulos em "Attendance (%)" com a mediana.
    - Calcula e retorna o somatório dos valores na coluna "Attendance (%)".
    
    Args:
        df (pd.DataFrame): DataFrame com os dados carregados.
    
    Returns:
        pd.DataFrame: DataFrame limpo.
        float: Somatório dos valores da coluna "Attendance (%)".
        float: Média da idade, se disponível.
    """
    try:
        # Verifica se as colunas necessárias existem
        required_columns = ["Parent_Education_Level", "Attendance (%)"]
        for col in required_columns:
            if col not in df.columns:
                raise KeyError(f"Erro: A coluna '{col}' não foi encontrada no DataFrame.")

        # Remove registros onde "Parent_Education_Level" está vazio
        df_cleaned = df.dropna(subset=["Parent_Education_Level"]).copy()

        # Preenche valores nulos na coluna "Attendance (%)" com a mediana
        if not pd.api.types.is_numeric_dtype(df_cleaned["Attendance (%)"]):
            raise ValueError("Erro: A coluna 'Attendance (%)' contém valores não numéricos.")

        median_attendance = df_cleaned["Attendance (%)"].median()
        df_cleaned["Attendance (%)"] = df_cleaned["Attendance (%)"].fillna(median_attendance)

        # Calcula o somatório de "Attendance (%)"
        total_attendance = df_cleaned["Attendance (%)"].sum()

        return df_cleaned, total_attendance

    except KeyError as e:
        print(f"Erro de Coluna: {e}")
    except ValueError as e:
        print(f"Erro de Valores: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

    return None, None, None  # Retorna valores nulos se houver erro