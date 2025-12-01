from arquitetura_de_computadores_trabalho2_UFABC.execucao.opcAbstrata import IMPL_COMANDOS_INTERNOS
from arquitetura_de_computadores_trabalho2_UFABC.execucao.opcAritmetica import opcAritmetica
from arquitetura_de_computadores_trabalho2_UFABC.execucao.opcLogica import opcLogica
from arquitetura_de_computadores_trabalho2_UFABC.execucao.opcEscrita import opcEscrita
from arquitetura_de_computadores_trabalho2_UFABC.execucao.opcLeitura import opcLeitura
from arquitetura_de_computadores_trabalho2_UFABC.execucao.cond import cond
from arquitetura_de_computadores_trabalho2_UFABC.execucao.tag import tag
from arquitetura_de_computadores_trabalho2_UFABC.execucao.rep import rep
from arquitetura_de_computadores_trabalho2_UFABC.execucao.jump import jump


# Padrão de Projeto Strategy
class Exec:
        def __init__(self, comando, operandos=None, pc=None, index=None):
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
            
            elif comando == 'cond':
                self.opc = cond(pc, comando, *operandos)
            elif comando == 'rep':
                self.opc = rep(pc, comando, *operandos)
            elif comando == 'jump':
                self.opc = jump(pc, comando, *operandos)
            else:
                self.opc = tag(comando)

        def processar(self):
            self.opc.processar()
        
        def definirProximo(self, posicao, escopo):
            ex = self
            
            if ex.comando not in ['cond', 'rep', 'jump'] and ex.comando not in tag.LISTA_DE_TAGS:
                if escopo == 'main':
                    ex.next = self.pc.execucao[posicao + 1]
                else:
                    ex.next = self.pc.exec_func[posicao + 1]
            elif ex.comando == 'cond':
                ex.opc.definirPosicoesTags() 
                ex.next = [self.pc.execucao[posicao + 1], self.pc.execucao[ex.opc.posicaoF]]
                self.pc.execucao[ex.opc.posicaoV].next = self.pc.execucao[ex.opc.posicaoFim]
                self.pc.execucao[ex.opc.posicaoF].next = self.pc.execucao[ex.opc.posicaoF + 1]
                if ex.opc.posicaoFim + 1 < len(self.pc.execucao):
                    self.pc.execucao[ex.opc.posicaoFim].next = self.pc.execucao[ex.opc.posicaoFim + 1]
               
            elif ex.comando == 'rep':
                ex.opc.definirPosicoesTags()
                ex.next = [self.pc.execucao[ex.opc.posicaoVerdadeira], self.pc.execucao[ex.opc.posicaoFalsa]]
                self.pc.execucao[ex.opc.posicaoVerdadeira].next = self.pc.execucao[ex.opc.posicaoVerdadeira + 1]
                self.pc.execucao[posicao + 1].next = self.pc.execucao[posicao + 2]
               
            elif ex.comando == 'jump':
                ex.opc.definirPosicoesTags()
                # print('-----')
                # print(ex.comando, ' --- ', ex.opc.tag_link, ' ', ex.opc.tag_retorno)
                # print(ex.opc.link, ' ', ex.opc.retorno)
                ex.next = self.pc.exec_func[ex.opc.link]
                self.pc.exec_func[ex.opc.link].next = self.pc.exec_func[ex.opc.link + 1]
                self.pc.exec_func[ex.opc.retorno].next = self.pc.execucao[posicao + 1]





    
