from arquitetura_de_computadores_trabalho2_UFABC.execucao.opcAbstrata import IMPL_COMANDOS_INTERNOS
from arquitetura_de_computadores_trabalho2_UFABC.execucao.utils import verificarValor, validarNumerico

class jump(IMPL_COMANDOS_INTERNOS):
    def __init__(self, pc, comando, condicao=None, tag_verdade=None, tag_falsa=None):
        self.pc = pc
        self.comando = comando
        self.condicao = condicao
        self.tag_verdade = tag_verdade
        self.tag_falsa = tag_falsa
        
    def processar(self):
       print(self.comando, "  ", self.condicao, '  '  , self.tag_verdade, '   ' , self.tag_falsa)