import os
import pandas as pd

def carregar_dados_usuario():
    """
    Permite que o usuário carregue um arquivo CSV ou JSON na pasta 'data' do projeto ou forneça um caminho manual.
    Agora com tratamento aprimorado para entradas inválidas.
    
    Returns:
        pd.DataFrame | None: Retorna um DataFrame com os dados carregados, ou None caso o arquivo seja inválido.
    """
    data_path = os.path.join(os.getcwd(), "data")  # Define o caminho absoluto da pasta 'data'
    
    # Verifica se há arquivos disponíveis na pasta 'data'
    arquivos_disponiveis = [f for f in os.listdir(data_path) if f.endswith(".csv") or f.endswith(".json")]

    caminho = None
    
    if arquivos_disponiveis:
        print("\nArquivos disponíveis na pasta 'data':")
        for idx, arquivo in enumerate(arquivos_disponiveis, start=1):
            print(f"{idx}. {arquivo}")

        escolha = input("Escolha um arquivo (digite o número correspondente) ou pressione ENTER para fornecer outro caminho: ")

        if escolha.isdigit() and 1 <= int(escolha) <= len(arquivos_disponiveis):
            arquivo_escolhido = arquivos_disponiveis[int(escolha) - 1]
            caminho = os.path.join(data_path, arquivo_escolhido)
        elif escolha.strip():  # Se o usuário digitou algo diferente de vazio
            caminho = escolha.strip()

    # Caso não tenha arquivos na pasta `data` ou o usuário queira fornecer outro caminho
    if caminho is None:
        caminho = input("Informe o caminho completo do arquivo CSV ou JSON: ").strip()

    # **Verificação adicional para evitar entradas inválidas**
    if not caminho or caminho.lower() == "c://null":
        print("Erro: Caminho do arquivo inválido! Certifique-se de inserir um caminho correto.")
        return None

    if not os.path.exists(caminho):
        print("Erro: O arquivo não foi encontrado! Verifique o caminho e tente novamente.")
        return None

    try:
        if caminho.endswith(".csv"):
            df = pd.read_csv(caminho)
            print(f"Arquivo CSV '{os.path.basename(caminho)}' carregado com sucesso!")
            return df
        elif caminho.endswith(".json"):
            df = pd.read_json(caminho)
            print(f"Arquivo JSON '{os.path.basename(caminho)}' carregado com sucesso!")
            return df
        else:
            print("Erro: O arquivo informado não é CSV ou JSON. Tente novamente.")
    except Exception as e:
        print(f"Erro ao carregar o arquivo: {e}")
        print("Certifique-se de que o caminho e o formato do arquivo estão corretos.")

    return None