
from projeto2_meu_pc.instrucoes.carregarInstrucoes import buscarInstrucoes
from projeto2_meu_pc.memoriaPrincipal.mp import carregarMemoriaPrincipal
from projeto2_meu_pc.registradores.rg import carregarRegistradores

# start
colecao = buscarInstrucoes()

print(colecao)

# for instr in colecao['instrucoes']:
#     print(instr)

mp = carregarMemoriaPrincipal()
registradores = carregarRegistradores()
print("Memória Principal: ")
print(mp)
print("Registradores ",registradores)