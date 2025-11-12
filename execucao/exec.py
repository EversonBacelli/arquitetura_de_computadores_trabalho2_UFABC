from arquitetura_de_computadores_trabalho2_UFABC.execucao.opcAbstrata import IMPL_COMANDOS_INTERNOS
from arquitetura_de_computadores_trabalho2_UFABC.execucao.opcAritmetica import opcAritmetica
from arquitetura_de_computadores_trabalho2_UFABC.execucao.opcLogica import opcLogica
from arquitetura_de_computadores_trabalho2_UFABC.execucao.opcEscrita import opcEscrita
from arquitetura_de_computadores_trabalho2_UFABC.execucao.opcLeitura import opcLeitura


# Padrão de Projeto Strategy
class Exec:
        def __init__(self, comando, operandos, pc):
            self. comando = comando
            self.operandos = operandos
            self.opc = None
            if comando in ['add', 'sub', 'mul', 'div']:
                self.opc = opcAritmetica(pc, comando, *operandos)
            elif comando in ['mq', 'meq', 'eq']:
                self.opc = opcLogica(pc, comando, *operandos)
            elif comando == 'es':
                self.opc = opcEscrita(pc, comando, *operandos)
            elif comando == 'le':
                self.opc = opcLeitura(pc, comando, *operandos)
            
        def processar(self):
            self.opc.processar()
        

            

        





    
