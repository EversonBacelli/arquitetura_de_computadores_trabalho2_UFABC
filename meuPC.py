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
        
        alg = preProcessamento(PC.ALGORITMO[0])
        
        for i in range(len(alg)):
            comando, operandos = alg[i]
            e = Exec(comando, operandos, self, i)
            self.execucao.append(e)
        
        # Vincular Nós, 
        for i in range(len(self.execucao) -1 ):
            self.execucao[i].definirProximo(i)
            
        # print(self.execucao[0].comando, '  ', self.execucao[0].next.comando )
        # print(self.execucao[1].comando, '  ', self.execucao[1].next.comando)
        # print(self.execucao[2].comando,'  ', self.execucao[2].next.comando)
        # print(self.execucao[3].comando,'  ', self.execucao[3].next.comando)
        # print(self.execucao[4].comando,'  ', self.execucao[4].next.comando)
        # print(self.execucao[5].comando,'  ', self.execucao[5].operandos)
        # print(self.execucao[6].comando,'  ', self.execucao[6].next.comando)
        # print(self.execucao[7].comando,'  ', self.execucao[7].next[0].comando, ' ', self.execucao[7].next[1].comando)
        # print(self.execucao[8].comando,'  ', self.execucao[8].next.comando)
        # print(self.execucao[9].comando,'  ', self.execucao[9].next)
        # print(self.execucao[10].comando,'  ', self.execucao[10].next)
        
        # # Condição de parada do process
        self.execucao.append(None)
        
        atual = self.execucao[0]
        ultimoComando = self.execucao[-1]
        
        while atual != ultimoComando :
            atual.processar() 
            if atual.comando == 'cond' or atual.comando == 'rep':
                atual.opc.atualizarCondicao()
                
                if atual.opc.resultadoOpcLogica == 1.0:
                    atual = atual.next[0]
                else: 
                    atual = atual.next[1]
            else:
                atual = atual.next
            if atual != None:
                print(atual.comando, ' ', atual.operandos,'  ',self.registradores)
        
        print(PC.ALGORITMO[0][0])
        print('-------')
        print('MEMÓRIA PRINCIPAL: ')
        print(self.mp)
        print('---------')
        print('REGISTRADORES: ')
        print(self.registradores)


    def escrever(self, valor, destino):
        novaString = destino[0:3]
        
        # Escrita em posição definida pelo usuário na MP
        if novaString == 'reg':
            numeroRegistrador = self.obterEnderecoRegistrador(destino)
            self.registradores[numeroRegistrador] = valor
            return numeroRegistrador
        else:
            print(destino) 
            endMP = ast.literal_eval(destino)
            linha, coluna = endMP
            self.mp = self.escrita(linha, coluna, self.mp, valor)
            print(self.mp[linha][coluna], 'linha: ', linha , ' coluna: ', coluna)
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