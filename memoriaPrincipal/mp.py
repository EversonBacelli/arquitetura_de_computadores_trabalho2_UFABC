import numpy as np

def carregarMemoriaPrincipal():
    mp = np.full((8, 8), np.nan, dtype=float)
    return mp

def selecionarPosicaoMP(mp):
    tentativas = 0
    
    for i in range(len(mp)):
        for j in range(len(mp[0])):
            if np.isnan(mp[i][j]):
                return i, j
    
    # 2. Obtenha as dimensões (shape)
    num_linhas, num_colunas = mp.shape

    # 3. Gere índices aleatórios
    # O np.random.randint(low, high) é exclusivo no 'high'.
    indice_linha_aleatorio = np.random.randint(0, num_linhas)
    indice_coluna_aleatorio = np.random.randint(0, num_colunas)
    return indice_linha_aleatorio, indice_linha_aleatorio

def lerEmMP(linha, coluna, mp):
    try:
        conteudo = mp[linha][coluna]
        return conteudo
    except: 
        return Exception

def escreverEmMP(linha, coluna, mp, conteudo):
    try:
        mp[linha][coluna] = conteudo
    except:
        return Exception
    
