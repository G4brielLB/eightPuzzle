from puzzle_8 import Puzzle_8
from metodos_busca import busca_largura, busca_profundidade, busca_profundidade_limitada, busca_profundidade_visitado

teste = [
        [1, 5, 2],
        [4, 0, 3], 
        [7, 8, 6]
        ]

teste_2 = [
    [8, 7, 3],
    [5, 6, 0],
    [4, 2, 1]
]

teste_3 = [
    [1, 2, 3],
    [4, 6, 0],
    [7, 5, 8]
]


puzzle = Puzzle_8()
puzzle.setNumbers(teste)

print("="*50)
print("BUSCA EM LARGURA (1)")
print("="*50)
caminho_bfs, explorados_bfs, visitados_bfs, custo_espaco, custo_tempo = busca_largura(puzzle)
if caminho_bfs is None:
    print("Não foi possível encontrar uma solução.")
else:
    print(f"Caminho encontrado em {len(caminho_bfs)-1} passos:")
    for i, estado in enumerate(caminho_bfs):
        print(f"Passo {i}:")
        print(estado)

    print(f"Custo de espaço (tamanho máximo fronteira de estado): {custo_espaco}")
    print(f"Custo de tempo (nós visitados): {custo_tempo}")


puzzle.reset()
puzzle.setNumbers(teste_2)


print("="*50)
print("BUSCA EM LARGURA (2)")
print("="*50)
caminho_bfs, explorados_bfs, visitados_bfs, custo_espaco, custo_tempo = busca_largura(puzzle)
if caminho_bfs is None:
    print("Não foi possível encontrar uma solução.")
else:
    print(f"Caminho encontrado em {len(caminho_bfs)-1} passos:")
    # for i, estado in enumerate(caminho_bfs):
    #     print(f"Passo {i}:")
    #     print(estado)

    print(f"Custo de espaço (tamanho máximo fronteira de estado): {custo_espaco}")
    print(f"Custo de tempo (nós visitados): {custo_tempo}")


puzzle.reset()
puzzle.setNumbers(teste_3)

print("="*50)
print("BUSCA EM LARGURA (3)")
print("="*50)
caminho_bfs, explorados_bfs, visitados_bfs, custo_espaco, custo_tempo = busca_largura(puzzle)
if caminho_bfs is None:
    print("Não foi possível encontrar uma solução.")
else:
    print(f"Caminho encontrado em {len(caminho_bfs)-1} passos:")
    for i, estado in enumerate(caminho_bfs):
        print(f"Passo {i}:")
        print(estado)

    print(f"Custo de espaço (tamanho máximo fronteira de estado): {custo_espaco}")
    print(f"Custo de tempo (nós visitados): {custo_tempo}")

"""
puzzle.reset()
puzzle.setNumbers(teste_3)
print("="*50)
print("BUSCA EM PROFUNDIDADE (1)")
print("="*50)
caminho_dfs, explorados_dfs, visitados_dfs, custo_espaco, custo_tempo, profundidade_max = busca_profundidade(puzzle)
if caminho_dfs is None:
    print("Não foi possível encontrar uma solução.")
else:
    print(f"Caminho encontrado em {len(caminho_dfs)-1} passos:")
    for i, estado in enumerate(caminho_dfs):
        print(f"Passo {i}:")
        print(estado)

    print(f"Custo de espaço (tamanho máximo fronteira de estado): {custo_espaco}")
    print(f"Custo de tempo (nós visitados): {custo_tempo}")
    print(f"Profundidade máxima: {profundidade_max}")

    print("="*50)
"""

puzzle.reset()
puzzle.setNumbers(teste)
print("="*50)
print("BUSCA EM PROFUNDIDADE LIMITADA (1)")
print("="*50)
caminho_dfs, explorados_dfs, visitados_dfs, custo_espaco, custo_tempo, profundidade_max = busca_profundidade_limitada(puzzle, 150)
if caminho_dfs is None:
    print("Não foi possível encontrar uma solução.")
else:
    print(f"Caminho encontrado em {len(caminho_dfs)-1} passos:")
    # for i, estado in enumerate(caminho_dfs):
    #     print(f"Passo {i}:")
    #     print(estado)

    print(f"Custo de espaço (tamanho máximo fronteira de estado): {custo_espaco}")
    print(f"Custo de tempo (nós visitados): {custo_tempo}")
    print(f"Profundidade máxima: {profundidade_max}")



puzzle.reset()
puzzle.setNumbers(teste_2)
print("="*50)
print("BUSCA EM PROFUNDIDADE LIMITADA (2)")
print("="*50)
caminho_dfs, explorados_dfs, visitados_dfs, custo_espaco, custo_tempo, profundidade_max = busca_profundidade_limitada(puzzle, 150)
if caminho_dfs is None:
    print("Não foi possível encontrar uma solução.")
else:
    print(f"Caminho encontrado em {len(caminho_dfs)-1} passos:")
    # for i, estado in enumerate(caminho_dfs):
    #     print(f"Passo {i}:")
    #     print(estado)

    print(f"Custo de espaço (tamanho máximo fronteira de estado): {custo_espaco}")
    print(f"Custo de tempo (nós visitados): {custo_tempo}")
    print(f"Profundidade máxima: {profundidade_max}")



puzzle.reset()
puzzle.setNumbers(teste_3)
print("="*50)
print("BUSCA EM PROFUNDIDADE LIMITADA (3)")
print("="*50)
caminho_dfs, explorados_dfs, visitados_dfs, custo_espaco, custo_tempo, profundidade_max = busca_profundidade_limitada(puzzle, 150)
if caminho_dfs is None:
    print("Não foi possível encontrar uma solução.")
else:
    print(f"Caminho encontrado em {len(caminho_dfs)-1} passos:")
    # for i, estado in enumerate(caminho_dfs):
    #     print(f"Passo {i}:")
    #     print(estado)

    print(f"Custo de espaço (tamanho máximo fronteira de estado): {custo_espaco}")
    print(f"Custo de tempo (nós visitados): {custo_tempo}")
    print(f"Profundidade máxima: {profundidade_max}")





puzzle.reset()
puzzle.setNumbers(teste)
print("="*50)
print("BUSCA EM PROFUNDIDADE VISITADO (1)")
print("="*50)
caminho_dfs, explorados_dfs, visitados_dfs, custo_espaco, custo_tempo, profundidade_max = busca_profundidade_visitado(puzzle)
if caminho_dfs is None:
    print("Não foi possível encontrar uma solução.")
else:
    print(f"Caminho encontrado em {len(caminho_dfs)-1} passos:")
    # for i, estado in enumerate(caminho_dfs):
    #     print(f"Passo {i}:")
    #     print(estado)

    print(f"Custo de espaço (tamanho máximo fronteira de estado): {custo_espaco}")
    print(f"Custo de tempo (nós visitados): {custo_tempo}")
    print(f"Profundidade máxima: {profundidade_max}")


puzzle.reset()
puzzle.setNumbers(teste_2)
print("="*50)
print("BUSCA EM PROFUNDIDADE VISITADO (2)")
print("="*50)   
caminho_dfs, explorados_dfs, visitados_dfs, custo_espaco, custo_tempo, profundidade_max = busca_profundidade_visitado(puzzle)
if caminho_dfs is None:
    print("Não foi possível encontrar uma solução.")
else:
    print(f"Caminho encontrado em {len(caminho_dfs)-1} passos:")
    # for i, estado in enumerate(caminho_dfs):
    #     print(f"Passo {i}:")
    #     print(estado)

    print(f"Custo de espaço (tamanho máximo fronteira de estado): {custo_espaco}")
    print(f"Custo de tempo (nós visitados): {custo_tempo}")
    print(f"Profundidade máxima: {profundidade_max}")


puzzle.reset()
puzzle.setNumbers(teste_3)
print("="*50)
print("BUSCA EM PROFUNDIDADE VISITADO (3)")
print("="*50)
caminho_dfs, explorados_dfs, visitados_dfs, custo_espaco, custo_tempo, profundidade_max = busca_profundidade_visitado(puzzle)
if caminho_dfs is None:
    print("Não foi possível encontrar uma solução.")
else:
    print(f"Caminho encontrado em {len(caminho_dfs)-1} passos:")
    # for i, estado in enumerate(caminho_dfs):
    #     print(f"Passo {i}:")
    #     print(estado)

    print(f"Custo de espaço (tamanho máximo fronteira de estado): {custo_espaco}")
    print(f"Custo de tempo (nós visitados): {custo_tempo}")
    print(f"Profundidade máxima: {profundidade_max}")