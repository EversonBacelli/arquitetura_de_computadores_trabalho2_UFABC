from arquitetura_de_computadores_trabalho2_UFABC.execucao.opcAbstrata import IMPL_COMANDOS_INTERNOS
from arquitetura_de_computadores_trabalho2_UFABC.execucao.utils import verificarValor, validarNumerico

class rep(IMPL_COMANDOS_INTERNOS):
    def __init__(self, pc, comando, condicao=None, tag_verdade=None, tag_falsa=None):
        self.pc = pc
        self.comando = comando
        self.condicao = condicao
        self.resultadoOpcLogica = None
        self.tag_verdade = tag_verdade
        self.tag_falsa = tag_falsa
        self.posicaoVerdadeira = 0
        self.posicaoFalsa = 0
        # print(self.tag_verdade, '  ' , self.tag_falsa)
    def processar(self):
        print('', end='')
        
    
    def definirPosicoesTags(self, escopo):
        ex = None
        if escopo == 'main':
            ex = self.pc.execucao
        else:
            ex = self.pc.exec_func
        
        
        for i in range(len(ex) - 1):
            if ex[i].comando == self.tag_verdade:
                self.posicaoVerdadeira = i
            elif ex[i].comando == self.tag_falsa:
                self.posicaoFalsa = i
        # print(self.tag_verdade, ' --  ', self.posicaoVerdadeira)
        # print(self.tag_falsa, ' --  ', self.posicaoFalsa)   
    
    def atualizarCondicao(self):   
        self.resultadoOpcLogica = verificarValor(self.condicao, self.pc)
        