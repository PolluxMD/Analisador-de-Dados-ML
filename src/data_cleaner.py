import pandas as pd

def limpar_dados(df):
    """
    Limpa os dados fornecidos, removendo registros e ajusta valoresnulos 

    - Remove registros onde a coluna "Parents_Education_Level" está vazia.
    - Preenche valores nulos na coluna "Attendance (%)" com a mjediana da própria soluna"
    - Calcula e retornar o somatório dos valores da coluna "Attendance (%)".

    Args:
        df (pd.DataFrame): DataFrame com os dados carregados.

    Returns:
        pd.DataFrame: DataFrame limpo.
        float: Somatório dos valores da coluna "Atendance (%)".
    """

    # Remove registros onde a coluna "Parents_Education"  está vazia

    df_cleaned = df.dropna(subset=["Parent_Education_Level"])
    
    # Um aviso no log está dizendo que o arquivo pode não estar sendo copiado para o original, fiz uma cópia independente

    df_cleaned = df.dropna(subset=["Parent_Education_Level"]).copy()
    
    # Preenche os valores nulos da coluna "Attendance" com a mediana

    median_attendance = df_cleaned["Attendance (%)"].median()
    df_cleaned["Attendance (%)"].fillna(median_attendance, inplace=True)

    # Calcula o somatório da coluna "Attendance"

    total_attendance = df_cleaned["Attendance (%)"].sum()

    return df_cleaned, total_attendance