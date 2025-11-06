# IMPORTAR RECURSOS
from arquitetura_de_computadores_trabalho2_UFABC.instrucoes.carregarInstrucoes import buscarInstrucoes
from arquitetura_de_computadores_trabalho2_UFABC.memoriaPrincipal.mp import carregarMemoriaPrincipal
from arquitetura_de_computadores_trabalho2_UFABC.registradores.rg import carregarRegistradores
from arquitetura_de_computadores_trabalho2_UFABC.programas.carregarProgramas import carregarPrograma
from arquitetura_de_computadores_trabalho2_UFABC.operacoes_ula.opcAritmeticas import operacoesAritmeticas
from arquitetura_de_computadores_trabalho2_UFABC.operacoes_ula.opcLogicas import operacoesLogicas

class PC:
    ALGORITMO = []
    def __init__(self):
        # CONJUNTO DE INSTRUCOES ISA
        self.instrucoes = buscarInstrucoes()
        
        # RECURSOS DE MEMORIA
        self.mp = carregarMemoriaPrincipal()         # memória principal
        self.registradores = carregarRegistradores() # registradores
        # SOFTWARE COMO PROGRAMA
        programa = carregarPrograma()
        PC.ALGORITMO.append(programa)
        # ULA
        self.OPERACOES_ARITMETICAS = operacoesAritmeticas.calc
        self.OPERACOES_LOGICAS = operacoesLogicas.comparar
        self.PILHA_EXECUCAO = []
        
    # def exec(self):
        
    def controlarMP(self, comando):
        return self.mp
    
    def controlarRegistradores(self, opc):
        return self.registradores
    
    def realizarOperacoesAritmeticas(opc):
        if opc == 'add':    
            print('add')