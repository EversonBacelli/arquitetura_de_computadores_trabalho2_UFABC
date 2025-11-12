

def verificarValor(operando, pc):
    if isinstance(operando, str):
            resp = validarNumerico(operando)
            if resp:
                return float(operando)
           
            numeroRegistrador = pc.obterEnderecoRegistrador(operando)
            operando = pc.ler(numeroRegistrador)
            return operando
    return operando


def validarNumerico(valor):
    try:
        # 1. Remove espaços e quebras de linha antes de tentar a conversão
        float(valor.strip()) 
        return True
    except ValueError:
        return False