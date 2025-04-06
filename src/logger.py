from datetime import datetime

def validar_nome_usuario(nome):
    """
    Valida o nome do usuário.
    Requisitos:
    - Deve conter apenas caracteres alfabéticos.
    - Deve ter no mínimo 3 caracteres.
    
    Args:
        nome (str): Nome fornecido pelo usuário.
    
    Returns:
        bool: True se o nome for válido, False caso contrário.
    """
    if nome.isalpha() and len(nome) >= 3:
        return True
    return False

def registrar_acao(nome_usuario, descricao):
    """
    Registra uma ação do usuário em um arquivo de log.
    
    Args:
        nome_usuario (str): Nome do usuário.
        descricao (str): Descrição da ação realizada.
    """
    with open("log.txt", "a") as log_file:
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{data_hora}] {nome_usuario}: {descricao}\n")
