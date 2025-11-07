from abc import ABC, abstractmethod    

# IMPORTAR RECURSOS
from arquitetura_de_computadores_trabalho2_UFABC.instrucoes.carregarInstrucoes import buscarInstrucoes
from arquitetura_de_computadores_trabalho2_UFABC.memoriaPrincipal.mp import carregarMemoriaPrincipal, selecionarPosicaoMP
from arquitetura_de_computadores_trabalho2_UFABC.memoriaPrincipal.mp import lerEmMP, escreverEmMP
from arquitetura_de_computadores_trabalho2_UFABC.registradores.rg import carregarRegistradores
from arquitetura_de_computadores_trabalho2_UFABC.programas.carregarProgramas import carregarPrograma
from arquitetura_de_computadores_trabalho2_UFABC.operacoes_ula.opcAritmeticas import operacoesAritmeticas
from arquitetura_de_computadores_trabalho2_UFABC.operacoes_ula.opcLogicas import operacoesLogicas
from arquitetura_de_computadores_trabalho2_UFABC.programas.preExec import preProcessamento

class PC:
    ALGORITMO = []
    def __init__(self):
        # CONJUNTO DE INSTRUCOES ISA
        self.instrucoes = buscarInstrucoes()
        
        # RECURSOS DE MEMORIA
        self.mp = carregarMemoriaPrincipal()         # memória principal
        self.definirPosicaoMP = selecionarPosicaoMP
        self.leitura = lerEmMP
        self.escrita = escreverEmMP
        
        self.registradores = carregarRegistradores() # registradores
        # SOFTWARE COMO PROGRAMA
        programa = carregarPrograma()
        PC.ALGORITMO.append(programa)
        
        # ULA
        self.OPERACOES_ARITMETICAS = operacoesAritmeticas.calc
        self.OPERACOES_LOGICAS = operacoesLogicas.comparar
        self.PILHA_EXECUCAO = []
        
    def exec(self):
        alg = preProcessamento(PC.ALGORITMO[0])
        e = Exec('add', [2, 3])
        e.processar()
        e2 = Exec('mq', [5, 3])
        e2.processar()
        # print(alg)
        


class Exec:
    def __init__(self, comando, operandos):
        if comando in ['add', 'sub', 'mul', 'div']:
            opc = opcAritmetica()
            self.executar = opc.processar(comando, *operandos)
        elif comando in ['mq', 'meq', 'eq']:
            opc = opcLogica()
            self.executar = opc.processar(comando, *operandos)
           
    def processar(self):
        resultado = self.executar
        print(resultado)
    
# IMPLEMENTAÇÃO DO PROCESSAMENTO DOS COMANDOS
class IMPL_COMANDOS_INTERNOS(ABC):
    @abstractmethod
    def processar(self, comando, operando1, operando2):
        pass
        
class opcAritmetica(IMPL_COMANDOS_INTERNOS):
    def __init__(self):
        self.OPERACOES_ARITMETICAS = operacoesAritmeticas.calc
    def processar(self, comando, operando1, operando2):
        destino = self.OPERACOES_ARITMETICAS(comando, operando1, operando2)
        return destino
    
class opcLogica(IMPL_COMANDOS_INTERNOS):
    def __init__(self):
        self.OPERACOES_LOGICAS = operacoesLogicas.comparar

    def processar(self, comando, operando1, operando2):
        destino = self.OPERACOES_LOGICAS(comando, operando1, operando2)
        return destino