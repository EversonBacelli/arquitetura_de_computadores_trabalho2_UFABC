
from arquitetura_de_computadores_trabalho2_UFABC.execucao.opcAbstrata import IMPL_COMANDOS_INTERNOS


class tag(IMPL_COMANDOS_INTERNOS):
    LISTA_DE_TAGS = []
    def __init__(self, nomeTag):
        self.nome = nomeTag
        tag.LISTA_DE_TAGS.append(self.nome)
        
    def processar(self):
        print('', end='')
    
    def updateDestino(self, posicao):
        self.destino = posicao