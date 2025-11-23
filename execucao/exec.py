from arquitetura_de_computadores_trabalho2_UFABC.execucao.opcAbstrata import IMPL_COMANDOS_INTERNOS
from arquitetura_de_computadores_trabalho2_UFABC.execucao.opcAritmetica import opcAritmetica
from arquitetura_de_computadores_trabalho2_UFABC.execucao.opcLogica import opcLogica
from arquitetura_de_computadores_trabalho2_UFABC.execucao.opcEscrita import opcEscrita
from arquitetura_de_computadores_trabalho2_UFABC.execucao.opcLeitura import opcLeitura
from arquitetura_de_computadores_trabalho2_UFABC.execucao.cond import cond
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
            elif comando == 'cond':
                self.opc = cond(pc, comando, *operandos)
            elif comando == 'rep':
                self.opc = rep(pc, comando, *operandos)
            else:
                self.opc = tag(comando)

        def processar(self):
            self.opc.processar()
        
        def definirProximo(self, posicao):
            ex = self
           
            if ex.comando not in ['cond', 'rep'] and ex.comando not in tag.LISTA_DE_TAGS:
                ex.next = self.pc.execucao[posicao + 1]
            elif ex.comando == 'cond':
                ex.opc.definirPosicoesTags() 
                ex.next = [self.pc.execucao[posicao + 1], self.pc.execucao[ex.opc.posicaoF]]
                self.pc.execucao[ex.opc.posicaoV].next = self.pc.execucao[ex.opc.posicaoFim]
                self.pc.execucao[ex.opc.posicaoF].next = self.pc.execucao[ex.opc.posicaoF + 1]
                # print(self.pc.execucao[ex.opc.posicaoFim].comando)
                
                if ex.opc.posicaoFim + 1 < len(self.pc.execucao):
                    self.pc.execucao[ex.opc.posicaoFim].next = self.pc.execucao[ex.opc.posicaoFim + 1]
                # print(len(self.pc.execucao), ' --------- ')
            elif ex.comando == 'rep':
                ex.opc.definirPosicoesTags()
                # print(ex.opc.tag_verdade,'   posicaoVerdade: ', ex.opc.posicaoVerdadeira)
                # print(ex.opc.tag_falsa, '  posicaoFalsa: ', ex.opc.posicaoFalsa)
                ex.next = [self.pc.execucao[ex.opc.posicaoVerdadeira], self.pc.execucao[ex.opc.posicaoFalsa]]
                # print('NEXT: ', ex.next[0].comando)
                # print('NEXT: ', ex.next[1].comando)
                
                self.pc.execucao[ex.opc.posicaoVerdadeira].next = self.pc.execucao[ex.opc.posicaoVerdadeira + 1]
                # print(self.pc.execucao[ex.opc.posicaoVerdadeira].next.comando)
                self.pc.execucao[posicao + 1].next = self.pc.execucao[posicao + 2]
                # print(self.pc.execucao[posicao + 1].next.comando)
                # print('--------')
            self = ex
                
        





    
