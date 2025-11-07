

def preProcessamento(ALGORITMO):
    alg = ALGORITMO

    comandos = []

    for linha in alg[2:]:
        comando, operandos = linha.split('|', 1)
        comando = comando.strip()
        operandos = operandos.strip()
        operandos = operandos.split(';')
        for i in range(len(operandos)):
            operandos[i] = operandos[i].strip()
        comandos.append((comando, operandos))
    
    return comandos