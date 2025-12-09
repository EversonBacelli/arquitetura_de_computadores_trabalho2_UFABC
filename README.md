# Arquitetura de Computadores — Trabalho 2 (UFABC)

Este repositório contém a implementação de uma **Instruction Set Architecture (ISA)** minimalista desenvolvida como parte do **Trabalho 2 da disciplina Arquitetura de Computadores**, no **Programa de Mestrado em Ciência da Computação da UFABC**.  
O objetivo é demonstrar como, mesmo com um conjunto reduzido de instruções e recursos limitados, é possível **executar cálculos numéricos complexos** como seno, cosseno, raiz e logaritmo.

## 🎯 Objetivos do Projeto

- Criar uma **ISA minimalista** com apenas 12 instruções.
- Simular uma CPU com:
  - 8 registradores  
  - 64 posições de memória  
  - Dados exclusivamente em ponto flutuante
- Implementar calculadoras numéricas usando apenas operações básicas (add, sub, mul, div).
- Explorar o funcionamento interno de CPUs:  
  parsing → decodificação → vinculação → execução.
- Mensurar:
  - precisão,
  - tempo de processamento,
  - consumo e pico de memória.

## 🧩 Recursos Implementados

### ✔ Conjunto de Instruções (ISA)
- **Aritméticas:** `add`, `sub`, `mul`, `div`
- **Lógicas:** `mq`, `meq`, `eq`
- **Controle de fluxo:** `cond`, `rep`, `jump`
- **Entrada e saída:** `es`
- **Tags:** para desvios e estruturação do fluxo

### ✔ Estruturas Suportadas
- Condicionais  
- Laços de repetição  
- Saltos e sub-rotinas  
- Controle de fluxo com tags  
- Encadeamento dinâmico de instruções

## 🔢 Algoritmos Numéricos Implementados

| Algoritmo | Método Utilizado | Observações |
|----------|------------------|-------------|
| **Raiz** | Bisseção + Newton-Raphson | Alta precisão, 100% de acerto nos testes |
| **Logaritmo** | Mudança de base + Regra do Trapézio (n=1000) | Preciso, mas com maior uso de memória |
| **Cosseno** | Série de Maclaurin | Altamente eficiente e preciso |
| **Seno** | Série de Maclaurin | Menor precisão (60% dentro do erro limite) |

## 📂 Estrutura Recomendada do Repositório

```
/
├── src/                  
├── algorithms/           
├── tests/                
├── docs/                 
└── README.md
```

## ▶ Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/EversonBacelli/arquitetura_de_computadores_trabalho2_UFABC.git
cd arquitetura_de_computadores_trabalho2_UFABC
```

2. Execute o interpretador da ISA:

```bash
python index.py
```

3. Para rodar um algoritmo numérico:

```bash
python index.py --program algorithms/logaritmo.txt
```

## 📄 Documentação

O repositório acompanha um relatório completo contendo:

- Arquitetura geral da CPU  
- Detalhamento da ISA  
- Fluxo de decodificação  
- Fluxo de execução  
- Métodos matemáticos  
- Testes de precisão  
- Análises de tempo e memória  
- Considerações finais  

## 👤 Autor

**Everson Willian Pereira Bacelli**  
Programa de Pós-Graduação em Ciência da Computação  
Universidade Federal do ABC (UFABC)

## 📜 Licença

Este projeto pode ser utilizado livremente para fins acadêmicos.

## 🚀 Melhorias Futuras

- Ampliar a ISA  
- Suporte a valores maiores  
- Pipeline de instruções  
- Verificador de erros  
- Benchmarks  
- Visualização gráfica
