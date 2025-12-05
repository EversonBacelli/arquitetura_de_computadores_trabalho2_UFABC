from arquitetura_de_computadores_trabalho2_UFABC.meuPC import PC
import time
import tracemalloc


##
#        "[0] - Teste Leitura, Escrita e Operações Aritméticas "
#        "[1] - Teste Operações Lógicas"
#        "[2] - Teste de Salto Condicional"
#        "[3] - Teste de Laço de Repetição"
#        "[4] - Raiz"
#        "[5] - Logaritmo "
#        "[6] - Cosseno "
#        "[7] - Seno"    
    
# start
start_time = time.perf_counter()
tracemalloc.start()

pc = PC()
pc.exec(5)

snapshot = tracemalloc.take_snapshot()
memoria_atual, pico_memoria = tracemalloc.get_traced_memory()


end_time = time.perf_counter()
tempo_decorrido = end_time - start_time
print(f"Tempo de execução: {tempo_decorrido:.4f} segundos")
print(f"Uso de memória atual: {memoria_atual / 1048576:.2f} MB")
print(f"Pico de uso de memória: {pico_memoria / 1048576:.2f} MB")

tracemalloc.stop()