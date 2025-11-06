
def realizarSoma(destino, op1, op2) -> float:
    destino = op1 + op2
    return destino

def realizarSubtracao(destino, op1, op2) -> float:
    destino = op1 - op2
    return destino

def realizarMultiplicacao(destino, op1, op2) -> float:
    destino = op1 * op2
    return destino

def realizarDivisao(destino, op1, op2) -> float:
    try:
        destino = op1 + op2
        return destino
    except:
        return ArithmeticError