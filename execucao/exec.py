from arquitetura_de_computadores_trabalho2_UFABC.execucao.opcAbstrata import IMPL_COMANDOS_INTERNOS
from arquitetura_de_computadores_trabalho2_UFABC.execucao.opcAritmetica import opcAritmetica
from arquitetura_de_computadores_trabalho2_UFABC.execucao.opcLogica import opcLogica
from arquitetura_de_computadores_trabalho2_UFABC.execucao.opcEscrita import opcEscrita
from arquitetura_de_computadores_trabalho2_UFABC.execucao.opcLeitura import opcLeitura
from arquitetura_de_computadores_trabalho2_UFABC.execucao.jump import jump
from arquitetura_de_computadores_trabalho2_UFABC.execucao.tag import tag
from arquitetura_de_computadores_trabalho2_UFABC.execucao.rep import rep


# Padrão de Projeto Strategy
class Exec:
        def __init__(self, comando, operandos, pc, index):
            self.pc = pc
            self. comando = comando
            self.operandos = operandos
            self.index = index
            self.opc = None
            self.next = None
            # Operações do Sistema
            if comando in ['add', 'sub', 'mul', 'div']:
                self.opc = opcAritmetica(pc, comando, *operandos)
            elif comando in ['mq', 'meq', 'eq']:
                self.opc = opcLogica(pc, comando, *operandos)
            elif comando == 'es':
                self.opc = opcEscrita(pc, comando, *operandos)
            elif comando == 'le':
                self.opc = opcLeitura(pc, comando, *operandos)
            elif comando == 'jump':
                self.opc = jump(pc, comando, *operandos)
            elif comando == 'rep':
                self.opc = rep(pc, comando, *operandos)
            elif comando in ['FIM', 'ELSE', 'DESVIO', 'LOOP', 'END_LOOP']:
                self.opc = tag(comando)

        def processar(self):
            self.opc.processar()
        
        def definirProximo(self, posicao):
            ex = self
           
            if ex.comando not in ['FIM', 'DESVIO', 'jump', 'rep']:
                ex.next = self.pc.execucao[posicao + 1]
            elif ex.comando == 'jump':
                ex.opc.definirPosicoesTags() 
                ex.next = [self.pc.execucao[posicao + 1], self.pc.execucao[ex.opc.posicaoF]]
                self.pc.execucao[ex.opc.posicaoV].next = self.pc.execucao[ex.opc.posicaoFim]
            elif ex.comando == 'rep':
                ex.opc.definirPosicoesTags()
                # print("NUMERO: ", ex.opc.posicaoVerdadeira)
                ex.next = [self.pc.execucao[ex.opc.posicaoVerdadeira], self.pc.execucao[posicao + 1]]
            self = ex
                
        





    
