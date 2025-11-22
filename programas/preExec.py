

def preProcessamento(ALGORITMO):
    alg = ALGORITMO
    comandos = []
     
    # Remover Comentário
    alg = removerComentarios(alg)   
 
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
        else:
            linha = linha.strip()
            comandos.append((linha, None))
    return comandos

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