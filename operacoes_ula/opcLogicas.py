from arquitetura_de_computadores_trabalho2_UFABC.operacoes_ula.implOpcLogica import definirSeEmaior, definirSeEmenor, definirSeEigual


class operacoesLogicas:
    def comparar(opc, destino, operando1, operando2):
        if opc == 'mq':   # maior que
            resp = definirSeEmaior(destino, operando1, operando2)
            return resp
        elif opc == 'meq':
            resp = definirSeEmenor(destino, operando1, operando2)
            return resp
        elif opc == 'eq':
            resp = definirSeEigual(destino, operando1, operando2)
            return resp
        else:
            return Exception