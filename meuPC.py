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
from pip._vendor.urllib3.packages.six import exec_

class PC:
    ALGORITMO = []
    def __init__(self):
        self.execucao = []
        self.exec_func = []
        # RECURSOS DE MEMORIA
        self.mp = carregarMemoriaPrincipal()         # memória principal
        self.definirPosicaoMP = selecionarPosicaoMP
        self.leitura = lerEmMP
        self.escrita = escreverEmMP
        
        self.registradores = carregarRegistradores() # registradores
        # SOFTWARE COMO PROGRAMA
        programas = carregarPrograma()
        PC.ALGORITMO.append(programas)
        
        # ULA
        self.OPERACOES_ARITMETICAS = operacoesAritmeticas.calc
        self.OPERACOES_LOGICAS = operacoesLogicas.comparar
        self.PILHA_EXECUCAO = []
        
    def exec(self, numeroAlgoritmo):      
        alg, func = preProcessamento(PC.ALGORITMO[0][numeroAlgoritmo])
         
        
        # Converter comandos em operações executáveis       
        for i in range(len(alg)):
            if isinstance(alg[i], str):
                e = Exec(alg[i], None, self, i)    
            else:
                comando, operandos = alg[i]
                e = Exec(comando, operandos, self, i)
            self.execucao.append(e)
        # # Condição de parada do process
        self.execucao.append(None)
        
        
        
        for i in range(len(func)):
            if isinstance(func[i], str):
                link = func[i]
                e = Exec(link, None, self, i)
                self.exec_func.append(e)
            else:
                comando, operandos = func[i]
                e = Exec(comando, operandos, self, i)
                self.exec_func.append(e)
        
        
        
        # # Vincular Nós, 
        for i in range(len(self.execucao) -1 ):
            self.execucao[i].definirProximo(i, 'main')
        
        # for e in self.execucao:
        #     if e is not None:
        #         if isinstance(e.next, list):
        #             print(e.comando, '  ' , e.next[0].comando, ' ', e.next[1].comando )
        #         else:
        #             if e.next != None:
        #                 print(e.comando, '  ', e.next.comando)
        #             else:
        #                 print(e.comando, '  ', e.next)

        for i in range(len(self.exec_func) -1 ):
            self.exec_func[i].definirProximo(i, 'func')
        
        
        
        # # print(len(self.execucao))
        # for exe in self.exec_func:
        #     if exe is not None:
        #         if exe.comando == 'cond' or exe.comando == 'rep':
        #             print(exe.comando, '  ', exe.next[0].comando, '  ', exe.next[1].comando)
        #         elif exe.comando == 'jump':
        #             print(exe.comando, '  ', exe.next.comando, ' ', exe.opc.link_true)
        #         else:
        #             if exe.next is not None:
        #                 print(exe.comando, '  ', exe.next.comando)
        #             else:
        #                 print(exe.comando, '  ', exe.next)

        
        
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
                
            
        
        # print(PC.ALGORITMO[0][0])
        print('-------')
        print('MEMÓRIA PRINCIPAL: ')
        # for linha in self.mp:
        #     for celula in linha:
        #         print(f'{celula:.2f} ', end=' ')
        #     print()
        print(self.mp)
        print('---------')
        print('REGISTRADORES: ')
        print(self.registradores)


    def escrever(self, valor, destino):
        novaString = destino[0:3]
        # print(valor)
        # Escrita em posição definida pelo usuário na MP
        if novaString == 'reg':
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