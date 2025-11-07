from arquitetura_de_computadores_trabalho2_UFABC.operacoes_ula.implOpcAritmeticas import realizarSoma, realizarSubtracao, realizarMultiplicacao, realizarDivisao


class operacoesAritmeticas:
    def calc(opc, operando1, operando2):
        if opc == 'add':
            resp = realizarSoma(operando1, operando2)
            return resp
        elif opc == 'sub':
            resp = realizarSubtracao(operando1, operando2)
            return resp
        elif opc == 'div':
            resp = realizarDivisao(operando1, operando2)
            return resp
        elif opc == 'mul':
            resp = realizarMultiplicacao(operando1, operando2)
            return resp
        else:
            return Exception