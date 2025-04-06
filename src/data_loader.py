import pandas as pd
import os

def carregar_dados():
    """
    Carrega o arquivo JSON com dados do dataset de alunos.
    Retorna um DataFrame do Pandas, garantindo que o arquivo está na pasta 'data'.
    
    Returns:
        pd.DataFrame | None: Retorna o DataFrame se os dados forem carregados corretamente, ou None em caso de erro.
    """
    # Define o caminho do arquivo relativo à pasta 'data'
    file_path = os.path.join(os.getcwd(), "data", "Students_Grading_Dataset.json")

    # Verifica se o arquivo existe
    if not os.path.exists(file_path):
        print(f"Erro: O arquivo '{file_path}' não foi encontrado. Certifique-se de que está na pasta 'data'.")
        return None

    try:
        # Carrega os dados do JSON
        df = pd.read_json(file_path)

        # Verifica se o arquivo não está vazio
        if df.empty:
            print("Erro: O arquivo JSON está vazio. Certifique-se de que contém dados antes de prosseguir.")
            return None

        print("Dados carregados com sucesso!")
        return df

    except ValueError:
        print("Erro: O arquivo JSON não pôde ser lido. Verifique se está formatado corretamente.")
        return None
    except Exception as e:
        print(f"Erro inesperado ao carregar os dados: {e}")
        return None

# Exemplo de uso
if __name__ == "__main__":
    dados = carregar_dados()
