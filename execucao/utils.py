import ast
from typing import Tuple

def verificarValor(operando, pc):
    if isinstance(operando, str):
            resp = validarNumerico(operando)
            if resp:
                return float(operando)
            operando = operando.strip()
            if len(operando) != 5:
                numeroRegistrador = pc.obterEnderecoRegistrador(operando)
                operando = pc.ler(numeroRegistrador)
                return operando
            else:
                tupla: Tuple[int, int] = ast.literal_eval(operando)
                linha, coluna = tupla
                operando = pc.leitura(linha, coluna, pc.mp)
                return operando
    return operando


def validarNumerico(valor):
    try:
        # 1. Remove espaços e quebras de linha antes de tentar a conversão
        float(valor.strip()) 
        return True
    except ValueError:
        return False