from projeto2_meu_pc.instrucoes.carregarInstrucoes import buscarInstrucoes
from projeto2_meu_pc.memoriaPrincipal.mp import carregarMemoriaPrincipal
from projeto2_meu_pc.registradores.rg import carregarRegistradores


class PC:
    def __init__(self):
        self.instrucoes = buscarInstrucoes()
        self.mp = carregarMemoriaPrincipal()
        self.registradores = carregarRegistradores()
    