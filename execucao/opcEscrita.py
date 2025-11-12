from arquitetura_de_computadores_trabalho2_UFABC.execucao.opcAbstrata import IMPL_COMANDOS_INTERNOS
from arquitetura_de_computadores_trabalho2_UFABC.execucao.utils import verificarValor, validarNumerico


class opcEscrita(IMPL_COMANDOS_INTERNOS):
    def __init__(self, pc, comando, destino, operando1):
        self.pc = pc
        self.comando = comando
        self.destino = destino
        self.operando1 = operando1
        
    def processar(self):
        valor = verificarValor(self.operando1, self.pc)
        posicao = self.pc.escrever(valor, self.destino)
        return posicao