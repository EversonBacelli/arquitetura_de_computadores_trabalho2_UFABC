
def realizarSoma(op1, op2) -> float:
    resultado = op1 + op2
    return resultado

def realizarSubtracao(op1, op2) -> float:
    resultado = op1 - op2
    return resultado

def realizarMultiplicacao(op1, op2) -> float:
    resultado = op1 * op2
    return resultado

def realizarDivisao(op1, op2) -> float:
    try:
        resultado = op1 / op2
        return resultado
    except:
        return ArithmeticError