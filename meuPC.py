import re, ast


# IMPORTAR RECURSOS
from arquitetura_de_computadores_trabalho2_UFABC.instrucoes.carregarInstrucoes import buscarInstrucoes
from arquitetura_de_computadores_trabalho2_UFABC.memoriaPrincipal.mp import carregarMemoriaPrincipal, selecionarPosicaoMP
from arquitetura_de_computadores_trabalho2_UFABC.memoriaPrincipal.mp import lerEmMP, escreverEmMP
from arquitetura_de_computadores_trabalho2_UFABC.registradores.rg import carregarRegistradores
from arquitetura_de_computadores_trabalho2_UFABC.programas.carregarProgramas import carregarPrograma
from arquitetura_de_computadores_trabalho2_UFABC.operacoes_ula.opcAritmeticas import operacoesAritmeticas
from arquitetura_de_computadores_trabalho2_UFABC.operacoes_ula.opcLogicas import operacoesLogicas
from arquitetura_de_computadores_trabalho2_UFABC.programas.preExec import preProcessamento
from arquitetura_de_computadores_trabalho2_UFABC.execucao.exec import Exec

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
        execucao = []
        alg = preProcessamento(PC.ALGORITMO[0])
        for comando, operandos in alg:
            e = Exec(comando, operandos, self)
            execucao.append(e)

        for tarefa in execucao:
            tarefa.processar()    
        
        print(self.mp)
        print(self.registradores)


    def escrever(self, valor, destino):
        primeiraLetra = destino[0]
        
        # Escrita em posição definida pelo usuário na MP
        if primeiraLetra == 'r':
            numeroRegistrador = self.obterEnderecoRegistrador(destino)
            self.registradores[numeroRegistrador] = valor
            return numeroRegistrador
        else: 
            endMP = ast.literal_eval(destino)
            linha, coluna = endMP
            self.mp = self.escrita(linha, coluna, self.mp, valor)
            return (linha, coluna)
        # Escrita em um registrador
        
           
        
    def ler(self, endereco):
        if isinstance(endereco, tuple):
            valor = self.leitura(endereco)
            return valor
        valor = self.registradores[endereco]
        return valor
    
    def obterEnderecoRegistrador(self, end):
        padrao = r'\[(\d+)\]'
        match = re.search(padrao, end)
        numeroRegistrador = int(match.group(1))
        return numeroRegistrador