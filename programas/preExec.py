

def preProcessamento(ALGORITMO):
    alg = ALGORITMO
   
    comandos = []
    tags = alg[1]
    
    _, elements = tags.split('|', 1)
    elements = elements.strip()
    elements = elements.split(';')
    
    
    for linha in alg[3:]:
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
    
    return comandos, elements