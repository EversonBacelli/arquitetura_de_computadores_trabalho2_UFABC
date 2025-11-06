import os
import json

def buscarInstrucoes():
    caminho_relativo = "arquitetura_de_computadores_trabalho2_UFABC/instrucoes/instrucoes.txt"
    caminho_absoluto = os.path.abspath(caminho_relativo)

    # Verifica se o arquivo realmente existe antes de ler
    if os.path.exists(caminho_absoluto):
        with open(caminho_absoluto, "r", encoding="utf-8") as arquivo:
            conteudo = json.load(arquivo)  # Corrigido: passar objeto de arquivo
            
            return conteudo
    else:
        print("\nArquivo não encontrado nesse caminho.")
        return None
