

def preProcessamento(ALGORITMO):
    alg = ALGORITMO
    comandos = []
    comandos_func = []
    # Remover Comentário
    alg = removerComentarios(alg)   
    alg, func = removerFuncoes(alg)
    
    # Separar comandos e operandos
    for linha in alg[2:]:
        if linha.find('|') != -1:
            comando, operandos = linha.split('|', 1)
            comando = comando.strip()
            operandos = operandos.strip()
            operandos = operandos.split(';')
            for i in range(len(operandos)):
                operandos[i] = operandos[i].strip()
            comandos.append((comando, operandos))
    
    for linha in func:
        if linha.find('|') != -1:
            comando, operandos = linha.split('|', 1)
            comando = comando.strip()
            operandos = operandos.strip()
            operandos = operandos.split(';')
            for i in range(len(operandos)):
                operandos[i] = operandos[i].strip()
            comandos_func.append((comando, operandos))
        elif linha != '***': 
            comandos_func.append(linha)
        
    return comandos, comandos_func

def removerComentarios(alg):
    comentarios = []
    for i in range(len(alg)):
        padrao = '--'
        linha = alg[i]
        if padrao in linha:
            comentarios.append(i)

    comentarios = sorted(comentarios, reverse=True)
    
    for i in range(len(comentarios)):
        alg.pop(comentarios[i])
        
    return alg

def removerFuncoes(alg):
    # trechoFuncao = []
    inicioFunc = None
    for i in range(len(alg)):
        padrao = '***'
        
        linha = alg[i]
        if padrao in linha:
            inicioFunc = i

    novoAlg = alg[:inicioFunc]
    func = alg[inicioFunc:]
            
    return novoAlg, func