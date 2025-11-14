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
        # self.instrucoes = buscarInstrucoes()
        self.execucao = []
        
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
        
        alg, tags = preProcessamento(PC.ALGORITMO[0])
        
        for i in range(len(alg)):
            comando, operandos = alg[i]
            e = Exec(comando, operandos, self, i)
            self.execucao.append(e)
        
        # Vincular Nós, 
        for i in range(len(self.execucao) -1 ):
            self.execucao[i].definirProximo(i)
            # if self.execucao[i].comando not in ['jump', 'FIM']:
            #     print(self.execucao[i].comando, '  NEXT: ', self.execucao[i].next.comando)
            # elif self.execucao[i].comando != 'FIM':
            #     print(self.execucao[i].comando, '  NEXT: ', self.execucao[i].next[0].comando)
            #     print(self.execucao[i].comando, '  NEXT: ', self.execucao[i].next[1].comando)
            
        
        # print(self.execucao[0].comando, '  ', self.execucao[0].next.comando )
        # print(self.execucao[1].comando, '  ', self.execucao[1].next.comando)
        # print(self.execucao[2].comando,'  ', self.execucao[2].next.comando)
        # print(self.execucao[3].comando,'  ', self.execucao[3].next)
        # print(self.execucao[4].comando,'  ', self.execucao[4].next.comando)
        # print(self.execucao[5].comando,'  ', self.execucao[5].next.comando)
        # print(self.execucao[6].comando,'  ', self.execucao[6].next.comando)
        # print(self.execucao[7].comando,'  ', self.execucao[7].next.comando)
        # print(self.execucao[8].comando,'  ', self.execucao[8].next.comando)
        # print(self.execucao[9].comando,'  ', self.execucao[9].next.comando)
        # print(self.execucao[10].comando,'  ', self.execucao[10].next)
        
        
        
        atual = self.execucao[0]
        ultimoComando = self.execucao[-1]
        
        while atual != ultimoComando :
            
            if atual.comando == 'jump':
                atual.processar() 
                atual.opc.atualizarCondicao()
                
                if atual.opc.condicao == 1:
                    atual = atual.next[0]
                else: 
                    atual = atual.next[1]
            else:
                atual.processar()
                atual = atual.next



        
        
        
        
        # for tarefa in self.execucao:
        #     if tarefa.comando is not 'jump':
        #         print(tarefa.comando, '  ' , tarefa.next.comando)
        #     else:
        #         print(tarefa.comando, '  ' , tarefa.next)
        #     tarefa.processar()    
        
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