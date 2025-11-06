from arquitetura_de_computadores_trabalho2_UFABC.meuPC import PC

# start
pc = PC()
mp = pc.mp
for i in range(7):
    mp[0][i] = 26.0

linha, coluna = pc.definirPosicaoMP(mp)
print('---- ANTES -----')
print(mp)
print('###########')

pc.escrita(linha, coluna, mp, 50.0)
conteudo = pc.leitura(linha, coluna, mp)
print(linha, ' - ' , coluna , ' ---> ', conteudo )
print(mp)

# for i in pc.instrucoes['instrucoes']:
#     comando = i['comando']
#     operandos = i['campos_que_exige']
#     explicacao = i['explicacao']
#     print(comando, ' - ', operandos, '  - ', explicacao)

# alg = PC.ALGORITMO

# for comando in alg[0]:
#     print(comando)

# destino = 0
# operando1 = 50
# operando2 = 50

# testeSum = pc.OPERACOES_ARITMETICAS('add', destino, operando1, operando2)
# testeSub = pc.OPERACOES_ARITMETICAS('sub', destino, operando1, operando2)
# testeMul = pc.OPERACOES_ARITMETICAS('mul', destino, operando1, operando2)
# testeDiv = pc.OPERACOES_ARITMETICAS('div', destino, operando1, operando2)
# testeMaior = pc.OPERACOES_LOGICAS('mq', destino, operando1, operando2)
# testeMenor = pc.OPERACOES_LOGICAS('meq', destino, operando1, operando2)
# testeIgual = pc.OPERACOES_LOGICAS('eq', destino, operando1, operando2)

# print(testeSum)
# print(testeSub)
# print(testeMul)
# print(testeDiv)
# print(testeMaior)
# print(testeMenor)
# print(testeIgual)



# print(pc.registradores)



