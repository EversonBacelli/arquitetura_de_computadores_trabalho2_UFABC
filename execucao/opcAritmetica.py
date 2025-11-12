from arquitetura_de_computadores_trabalho2_UFABC.execucao.opcAbstrata import IMPL_COMANDOS_INTERNOS
from arquitetura_de_computadores_trabalho2_UFABC.execucao.utils import verificarValor, validarNumerico


class opcAritmetica(IMPL_COMANDOS_INTERNOS):
    def __init__(self, pc, comando, destino, operando1, operando2):
        self.OPERACOES_ARITMETICAS = pc.OPERACOES_ARITMETICAS
        self.pc = pc
        self.comando = comando
        self.destino = destino
        self.operando1 = operando1
        self.operando2 = operando2
    def processar(self):
        operando1 = verificarValor(self.operando1, self.pc)
        operando2 = verificarValor(self.operando2, self.pc)

        resp = self.OPERACOES_ARITMETICAS(self.comando, float(operando1), float(operando2))
        retorno = self.pc.escrever(resp, self.destino)
        return retorno