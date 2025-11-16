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
        # print('INICIADA REP, valor inicial da condicao: ', self.condicao)
    def processar(self):
        # ex = self.pc.execucao
        condicao = verificarValor(self.condicao, self.pc)
        
        if condicao == 0.0:
            print('Menor') 
        else:
            print('Maior')
        
    
    def definirPosicoesTags(self):
        ex = self.pc.execucao
        print('DEFINIR_POSICAO')
        
        
        for i in range(len(ex)):
            if ex[i].comando == self.tag_verdade:
                print('VERDADE')
                self.posicaoVerdadeira = i
                #print(ex[i].comando, ' posicao: ', i)
            elif ex[i].comando == self.tag_falsa:
                self.posicaoFalsa = i
        # print(self.tag_verdade, ' --  ', self.posicaoVerdadeira)
        # print(self.tag_falsa, ' --  ', self.posicaoFalsa)   
    
    def atualizarCondicao(self):
        print(self.resultadoOpcLogica)
        self.resultadoOpcLogica = verificarValor(self.condicao, self.pc)
        print("Condição atualizada ", self.resultadoOpcLogica)
        