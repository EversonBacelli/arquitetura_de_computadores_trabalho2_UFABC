from arquitetura_de_computadores_trabalho2_UFABC.operacoes_ula.implOpcAritmeticas import realizarSoma, realizarSubtracao, realizarMultiplicacao, realizarDivisao


class operacoesAritmeticas:
    def calc(opc, destino, operando1, operando2):
        if opc == 'add':
            resp = realizarSoma(destino, operando1, operando2)
            return resp
        elif opc == 'sub':
            resp = realizarSubtracao(destino, operando1, operando2)
            return resp
        elif opc == 'div':
            resp = realizarDivisao(destino, operando1, operando2)
            return resp
        elif opc == 'mul':
            resp = realizarMultiplicacao(destino, operando1, operando2)
            return resp
        else:
            return Exception