from abc import ABC, abstractmethod    


# IMPLEMENTAÇÃO DO PROCESSAMENTO DOS COMANDOS
class IMPL_COMANDOS_INTERNOS(ABC):
    @abstractmethod
    def processar(self, comando, operando1, operando2):
            pass