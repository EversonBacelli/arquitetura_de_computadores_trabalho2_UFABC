from arquitetura_de_computadores_trabalho2_UFABC.execucao.opcAbstrata import IMPL_COMANDOS_INTERNOS
from arquitetura_de_computadores_trabalho2_UFABC.execucao.utils import verificarValor, validarNumerico

class cond(IMPL_COMANDOS_INTERNOS):
    def __init__(self, pc, comando, condicao=None, tag_verdade=None, tag_fim=None, tag_falsa=None):
        self.pc = pc
        self.comando = comando
        self.condicao = condicao
        self.resultadoOpcLogica = None
        self.tag_verdade = tag_verdade
        self.tag_fim = tag_fim
        self.tag_falsa = tag_falsa
        self.posicaoV = 0
        self.posicaoF = 0
        self.posicaoFim = 0
        
    def processar(self):
        print('', end='')
        
    
    def definirPosicoesTags(self, escopo):
        ex = None
        valor = 0
        # print('---------- ',escopo )
        
        if escopo == 'main':
            ex = self.pc.execucao
        else:
            ex = self.pc.exec_func


        for i in range(len(ex) - 1):
            if ex[i].comando == self.tag_verdade:
                self.posicaoV = i
            elif ex[i].comando == self.tag_falsa:
                self.posicaoF = i
            elif ex[i].comando == self.tag_fim:
                self.posicaoFim = i
    
    def atualizarCondicao(self):
        self.resultadoOpcLogica = verificarValor(self.condicao, self.pc)
        