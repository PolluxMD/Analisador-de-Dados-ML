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

def calcular_media(df, coluna):
    """
    Calcula a média dos valores na coluna especificada.
    
    Args:
        df (pd.DataFrame): DataFrame contendo os dados.
        coluna (str): Nome da coluna que será analisada.
    
    Returns:
        float: Média dos valores na coluna.
    """
    return df[coluna].mean()

def calcular_mediana(df, coluna):
    """
    Calcula a mediana dos valores na coluna especificada.
    
    Args:
        df (pd.DataFrame): DataFrame contendo os dados.
        coluna (str): Nome da coluna que será analisada.
    
    Returns:
        float: Mediana dos valores na coluna.
    """
    return df[coluna].median()

def calcular_moda(df, coluna):
    """
    Calcula a moda dos valores na coluna especificada.
    
    Args:
        df (pd.DataFrame): DataFrame contendo os dados.
        coluna (str): Nome da coluna que será analisada.
    
    Returns:
        float: Moda dos valores na coluna.
    """
    moda = df[coluna].mode()
    return moda[0] if not moda.empty else None

def calcular_desvio_padrao(df, coluna):
    """
    Calcula o desvio padrão dos valores na coluna especificada.
    
    Args:
        df (pd.DataFrame): DataFrame contendo os dados.
        coluna (str): Nome da coluna que será analisada.
    
    Returns:
        float: Desvio padrão dos valores na coluna.
    """
    return df[coluna].std()

