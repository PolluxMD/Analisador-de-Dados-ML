import pandas as pd

def validar_coluna(df, coluna):
    """
    Valida se a coluna existe no DataFrame e se é numérica.

    Args:
        df (pd.DataFrame): O DataFrame que contém os dados.
        coluna (str): Nome da coluna a ser validada.

    Returns:
        bool: Retorna True se a coluna for válida (existe e é numérica), caso contrário False.
    """
    if coluna not in df.columns:
        print(f"Erro: A coluna '{coluna}' não foi encontrada no dataset.")
        return False

    if not pd.api.types.is_numeric_dtype(df[coluna]):
        print(f"Erro: A coluna '{coluna}' não é numérica. Escolha uma coluna com valores numéricos.")
        return False

    return True


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

