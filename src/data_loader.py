import pandas as pd

def carregar_dados():
    """
    Carrega o arquivo JSON com dados do dataset de alunos.
    Retorna um DataFrame do Pandas.
    """
    file_path = r"C:\Users\erica\OneDrive\Semestre 5 2k25 - Análise e Desenvolvimento de Sistemas\MachineLeaning\Analisador_De_Dados\Analisador-de-Dados-ML\data\Students_Grading_Dataset.json"
    
    try:
        df = pd.read_json(file_path)
        print("Dados carregados com sucesso!")
        print(df.head())  # Visualiza as 5 primeiras linhas do DataFrame
        return df
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado no caminho: {file_path}")
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")

# Exemplo de uso
if __name__ == "__main__":
    dados = carregar_dados()