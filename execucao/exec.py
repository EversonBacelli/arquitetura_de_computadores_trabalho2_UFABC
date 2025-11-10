from abc import ABC, abstractmethod    

# Padrão de Projeto Strategy
class Exec:
        def __init__(self, comando, operandos, pc):
            self. comando = comando
            self.operandos = operandos
            if comando in ['add', 'sub', 'mul', 'div']:
                opc = opcAritmetica(pc)
                self.executar = opc.processar(comando, *operandos)
            elif comando in ['mq', 'meq', 'eq']:
                opc = opcLogica(pc)
                self.executar = opc.processar(comando, *operandos)
            elif comando == 'es':
                opc = opcEscrita(pc)
                self.executar = opc.processar(comando, *operandos)
            elif comando == 'le':
                opc = opcLeitura(pc)
                self.executar = opc.processar(comando, *operandos)
            
        def processar(self):
            resultado = self.executar
            # print(resultado)
        
# IMPLEMENTAÇÃO DO PROCESSAMENTO DOS COMANDOS
class IMPL_COMANDOS_INTERNOS(ABC):
    @abstractmethod
    def processar(self, comando, operando1, operando2):
            pass
            
class opcAritmetica(IMPL_COMANDOS_INTERNOS):
    def __init__(self, pc):
        self.OPERACOES_ARITMETICAS = pc.OPERACOES_ARITMETICAS
        self.pc = pc
    def processar(self, comando, destino ,operando1, operando2):
        operando1 = verificarValor(operando1, self.pc)
        operando2 = verificarValor(operando2, self.pc)

        
        
        resp = self.OPERACOES_ARITMETICAS(comando, float(operando1), float(operando2))
        retorno = self.pc.escrever(resp, destino)
        return retorno
        
class opcLogica(IMPL_COMANDOS_INTERNOS):
    def __init__(self, pc):
        self.OPERACOES_LOGICAS = pc.OPERACOES_LOGICAS
        self.pc = pc
    def processar(self, comando, destino ,operando1, operando2):
        resp = self.OPERACOES_LOGICAS(comando, operando1, operando2)
        retorno = self.pc.escrever(resp, destino)
        return retorno

class opcEscrita(IMPL_COMANDOS_INTERNOS):
    def __init__(self, pc):
        self.pc = pc
    def processar(self, comando, endereco, valor):
        valor = verificarValor(valor, self.pc)
        posicao = self.pc.escrever(valor, endereco)
        return posicao

class opcLeitura(IMPL_COMANDOS_INTERNOS):
    def __init__(self, pc):
        self.pc = pc
    def processar(self, endereco):
        valor = self.pc.ler(endereco)
        return valor
    
def verificarValor(operando, pc):
    
    
    if isinstance(operando, str):
            resp = validarNumerico(operando)
            if resp:
                return float(operando)
           
            numeroRegistrador = pc.obterEnderecoRegistrador(operando)
            operando = pc.ler(numeroRegistrador)
            return operando
    return operando


def validarNumerico(valor):
    try:
        # 1. Remove espaços e quebras de linha antes de tentar a conversão
        float(valor.strip()) 
        return True
    except ValueError:
        return False