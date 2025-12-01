from arquitetura_de_computadores_trabalho2_UFABC.execucao.opcAbstrata import IMPL_COMANDOS_INTERNOS
from arquitetura_de_computadores_trabalho2_UFABC.execucao.utils import verificarValor, validarNumerico

class opcLeitura(IMPL_COMANDOS_INTERNOS):
    def __init__(self, pc, endereco):
        self.pc = pc
        self.endereco = endereco
    def processar(self):
        valor = self.pc.ler(self.endereco)
        return float(valor)