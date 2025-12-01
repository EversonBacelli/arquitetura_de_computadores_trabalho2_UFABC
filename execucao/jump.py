from arquitetura_de_computadores_trabalho2_UFABC.execucao.opcAbstrata import IMPL_COMANDOS_INTERNOS
from arquitetura_de_computadores_trabalho2_UFABC.execucao.utils import verificarValor, validarNumerico

class jump(IMPL_COMANDOS_INTERNOS):
    def __init__(self, pc, comando, tag_link=None, tag_retorno=None):
        self.pc = pc
        self.comando = comando
        self.tag_link= tag_link
        self.tag_retorno = tag_retorno
        self.link = None
        self.retorno = None
        self.next = None
        # print(self.tag_link, '-----', self.tag_retorno)
    def processar(self):
        print('', end='')
        
    
    def definirPosicoesTags(self):
        # principal
        ex = self.pc.execucao
        # funcoes
        ex_func = self.pc.exec_func
        
        # print(self.tag_link) 
        for i in range(len(ex_func)):
            # print(ex_func[i].comando)
            if ex_func[i].comando == self.tag_link:
                self.link = i
                # print('Retorno ', i)
            if ex_func[i].comando == self.tag_retorno:
                self.retorno = i
        
        # print(self.link, ' --  ', self.retorno)
           
    
    
        