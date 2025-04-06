import pandas as pd

def validar_coluna(df, coluna_usuario):
    """
    Valida se a coluna informada pelo usuário existe e se é numérica.
    
    Args:
        df (pd.DataFrame): DataFrame contendo os dados.
        coluna_usuario (str): Nome da coluna fornecida pelo usuário.
    
    Returns:
        bool: True se a coluna for válida, False caso contrário.
    """
    # Obtém lista de colunas disponíveis no DataFrame
    colunas_disponiveis = df.columns.tolist()

    # Verifica se a coluna existe
    if coluna_usuario not in colunas_disponiveis:
        print(f"Erro: A coluna '{coluna_usuario}' não existe no dataset.")
        print(f"Colunas disponíveis: {colunas_disponiveis}")
        return False

    # Verifica se a coluna é numérica
    colunas_numericas = df.select_dtypes(include=["number"]).columns.tolist()
    if coluna_usuario not in colunas_numericas:
        print(f"Erro: A coluna '{coluna_usuario}' não contém valores numéricos.")
        print(f"Colunas numéricas disponíveis: {colunas_numericas}")
        return False

    return True  # Se passar nas verificações, retorna True


