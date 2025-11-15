import os

def carregarPrograma():
    caminho_relativo = "arquitetura_de_computadores_trabalho2_UFABC/programas/laco_repeticao.txt"
    caminho_absoluto = os.path.abspath(caminho_relativo)
    
    # Inicializa a lista que armazenará o conteúdo
    linhas_do_programa = []

    # Verifica se o arquivo realmente existe antes de ler
    if os.path.exists(caminho_absoluto):
        try:
            with open(caminho_absoluto, "r", encoding="utf-8") as arquivo:
                # Modificação: Ler cada linha do arquivo
                for linha in arquivo:
                    # Remove espaços em branco do início e fim, incluindo quebras de linha (\n)
                    linha_limpa = linha.strip() 
                    
                    # Opcional: Ignorar linhas vazias (se houver)
                    if linha_limpa:
                        linhas_do_programa.append(linha_limpa)
            
            # Retorna a lista de linhas lidas
            return linhas_do_programa
            
        except Exception as e:
            print(f"Erro ao ler o arquivo: {e}")
            return None
    else:
        print(f"\nArquivo não encontrado nesse caminho: {caminho_absoluto}")
        return None