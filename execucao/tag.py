
from arquitetura_de_computadores_trabalho2_UFABC.execucao.opcAbstrata import IMPL_COMANDOS_INTERNOS


class tag(IMPL_COMANDOS_INTERNOS):
    def __init__(self, nomeTag):
        self.nome = nomeTag
       
        
    def processar(self):
       print(self.nome)