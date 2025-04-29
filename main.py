from puzzle_8 import Puzzle_8
from metodos_busca import busca_largura, busca_profundidade, busca_profundidade_limitada, busca_profundidade_visitado, busca_gulosa, busca_a_star

teste_1 = [
        [1, 2, 0],
        [4, 6, 3], 
        [7, 5, 8]
        ]

teste_2 = [
    [0, 2, 3],
    [1, 5, 6],
    [4, 7, 8]
]

teste_3 = [
    [6, 1, 5],
    [2, 0, 3],
    [4, 7, 8]
]

teste_4 = [
    [8, 7, 3],
    [5, 6, 0],
    [4, 2, 1]
]


puzzle = Puzzle_8()
puzzle.setNumbers(teste_1)

print("="*70)
print("BUSCA EM LARGURA (1)")
print("="*70)
caminho_bfs, explorados_bfs, visitados_bfs, custo_espaco, custo_tempo, total_nos_gerados = busca_largura(puzzle)
if caminho_bfs is None:
    print("Não foi possível encontrar uma solução.")
else:
    print(f"Caminho encontrado em {len(caminho_bfs)-1} passos:")
    # for i, estado in enumerate(caminho_bfs):
    #     print(f"Passo {i}:")
    #     print(estado)

    print(f"Custo de espaço (tamanho máximo fronteira de estado): {custo_espaco}")
    print(f"Custo de tempo (nós visitados): {custo_tempo}")
    print(f"Total de nós gerados: {total_nos_gerados}")

puzzle.reset()
puzzle.setNumbers(teste_1)

print("="*70)
print("BUSCA EM PROFUNDIDADE (1)")
print("="*70)
caminho_dfs, explorados_dfs, visitados_dfs, custo_espaco, custo_tempo, profundidade_max, total_nos_gerados = busca_profundidade_visitado(puzzle)
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
    print(f"Total de nós gerados: {total_nos_gerados}")

puzzle.reset()
puzzle.setNumbers(teste_1)


print("="*70)
print("BUSCA GULOSA (1)")
print("="*70)
caminho_bfs, explorados_bfs, visitados_bfs, custo_espaco, custo_tempo, profundidade_maxima, total_nos_gerados = busca_gulosa(puzzle)
if caminho_bfs is None:
    print("Não foi possível encontrar uma solução.")
else:
    print(f"Caminho encontrado em {len(caminho_bfs)-1} passos:")
    # for i, estado in enumerate(caminho_bfs):
    #     print(f"Passo {i}:")
    #     print(estado)

    print(f"Custo de espaço (tamanho máximo fronteira de estado): {custo_espaco}")
    print(f"Custo de tempo (nós visitados): {custo_tempo}")
    print(f"Profundidade máxima: {profundidade_maxima}")
    print(f"Total de nós gerados: {total_nos_gerados}")

puzzle.reset()
puzzle.setNumbers(teste_1)

print("="*70)
print("BUSCA A* (1)")
print("="*70)
caminho_a_star, explorados_a_star, visitados_a_star, custo_espaco, custo_tempo, profundidade_maxima, total_nos_gerados = busca_a_star(puzzle)
if caminho_a_star is None:
    print("Não foi possível encontrar uma solução.")
else:
    print(f"Caminho encontrado em {len(caminho_a_star)-1} passos:")
    # for i, estado in enumerate(caminho_a_star):
    #     print(f"Passo {i}:")
    #     print(estado)

    print(f"Custo de espaço (tamanho máximo fronteira de estado): {custo_espaco}")
    print(f"Custo de tempo (nós visitados): {custo_tempo}")
    print(f"Profundidade máxima: {profundidade_maxima}")
    print(f"Total de nós gerados: {total_nos_gerados}")

puzzle.reset()
puzzle.setNumbers(teste_2)

print("="*70)
print("BUSCA EM LARGURA (2)")
print("="*70)
caminho_bfs, explorados_bfs, visitados_bfs, custo_espaco, custo_tempo, total_nos_gerados = busca_largura(puzzle)
if caminho_bfs is None:
    print("Não foi possível encontrar uma solução.")
else:
    print(f"Caminho encontrado em {len(caminho_bfs)-1} passos:")
    # for i, estado in enumerate(caminho_bfs):
    #     print(f"Passo {i}:")
    #     print(estado)

    print(f"Custo de espaço (tamanho máximo fronteira de estado): {custo_espaco}")
    print(f"Custo de tempo (nós visitados): {custo_tempo}")
    print(f"Total de nós gerados: {total_nos_gerados}")

puzzle.reset()
puzzle.setNumbers(teste_2)

print("="*70)
print("BUSCA EM PROFUNDIDADE (2)")
print("="*70)
caminho_dfs, explorados_dfs, visitados_dfs, custo_espaco, custo_tempo, profundidade_max, total_nos_gerados = busca_profundidade_visitado(puzzle)
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
    print(f"Total de nós gerados: {total_nos_gerados}")

puzzle.reset()
puzzle.setNumbers(teste_2)

print("="*70)
print("BUSCA GULOSA (2)")
print("="*70)
caminho_bfs, explorados_bfs, visitados_bfs, custo_espaco, custo_tempo, profundidade_maxima, total_nos_gerados = busca_gulosa(puzzle)
if caminho_bfs is None:
    print("Não foi possível encontrar uma solução.")
else:
    print(f"Caminho encontrado em {len(caminho_bfs)-1} passos:")
    # for i, estado in enumerate(caminho_bfs):
    #     print(f"Passo {i}:")
    #     print(estado)

    print(f"Custo de espaço (tamanho máximo fronteira de estado): {custo_espaco}")
    print(f"Custo de tempo (nós visitados): {custo_tempo}")
    print(f"Profundidade máxima: {profundidade_maxima}")
    print(f"Total de nós gerados: {total_nos_gerados}")

puzzle.reset()
puzzle.setNumbers(teste_2)

print("="*70)
print("BUSCA A* (2)")
print("="*70)
caminho_a_star, explorados_a_star, visitados_a_star, custo_espaco, custo_tempo, profundidade_maxima, total_nos_gerados = busca_a_star(puzzle)
if caminho_a_star is None:
    print("Não foi possível encontrar uma solução.")
else:
    print(f"Caminho encontrado em {len(caminho_a_star)-1} passos:")
    # for i, estado in enumerate(caminho_a_star):
    #     print(f"Passo {i}:")
    #     print(estado)

    print(f"Custo de espaço (tamanho máximo fronteira de estado): {custo_espaco}")
    print(f"Custo de tempo (nós visitados): {custo_tempo}")
    print(f"Profundidade máxima: {profundidade_maxima}")
    print(f"Total de nós gerados: {total_nos_gerados}")

puzzle.reset()
puzzle.setNumbers(teste_3)

print("="*70)
print("BUSCA EM LARGURA (3)")
print("="*70)
caminho_bfs, explorados_bfs, visitados_bfs, custo_espaco, custo_tempo, total_nos_gerados = busca_largura(puzzle)
if caminho_bfs is None:
    print("Não foi possível encontrar uma solução.")
else:
    print(f"Caminho encontrado em {len(caminho_bfs)-1} passos:")
    print(f"Custo de espaço (tamanho máximo fronteira de estado): {custo_espaco}")
    print(f"Custo de tempo (nós visitados): {custo_tempo}")
    print(f"Total de nós gerados: {total_nos_gerados}")

puzzle.reset()
puzzle.setNumbers(teste_3)

print("="*70)
print("BUSCA EM PROFUNDIDADE (3)")
print("="*70)
caminho_dfs, explorados_dfs, _, custo_espaco, custo_tempo, profundidade_max, total_nos_gerados = busca_profundidade_visitado(puzzle)
if caminho_dfs is None:
    print("Não foi possível encontrar uma solução.")
else:
    print(f"Caminho encontrado em {len(caminho_dfs)-1} passos:")
    print(f"Custo de espaço (tamanho máximo fronteira de estado): {custo_espaco}")
    print(f"Custo de tempo (nós visitados): {custo_tempo}")
    print(f"Profundidade máxima: {profundidade_max}")
    print(f"Total de nós gerados: {total_nos_gerados}")

puzzle.reset()
puzzle.setNumbers(teste_3)

print("="*70)
print("BUSCA GULOSA (3)")
print("="*70)
caminho_bfs, explorados_bfs, visitados_bfs, custo_espaco, custo_tempo, profundidade_maxima, total_nos_gerados = busca_gulosa(puzzle)
if caminho_bfs is None:
    print("Não foi possível encontrar uma solução.")
else:
    print(f"Caminho encontrado em {len(caminho_bfs)-1} passos:")
    print(f"Custo de espaço (tamanho máximo fronteira de estado): {custo_espaco}")
    print(f"Custo de tempo (nós visitados): {custo_tempo}")
    print(f"Profundidade máxima: {profundidade_maxima}")
    print(f"Total de nós gerados: {total_nos_gerados}")

puzzle.reset()
puzzle.setNumbers(teste_3)

print("="*70)
print("BUSCA A* (3)")
print("="*70)
caminho_a_star, explorados_a_star, visitados_a_star, custo_espaco, custo_tempo, profundidade_maxima, total_nos_gerados = busca_a_star(puzzle)
if caminho_a_star is None:
    print("Não foi possível encontrar uma solução.")
else:
    print(f"Caminho encontrado em {len(caminho_a_star)-1} passos:")
    print(f"Custo de espaço (tamanho máximo fronteira de estado): {custo_espaco}")
    print(f"Custo de tempo (nós visitados): {custo_tempo}")
    print(f"Profundidade máxima: {profundidade_maxima}")
    print(f"Total de nós gerados: {total_nos_gerados}")

puzzle.reset()
puzzle.setNumbers(teste_1)

puzzle.reset()
puzzle.setNumbers(teste_4)

print("="*70)
print("BUSCA EM LARGURA (4)")
print("="*70)
caminho_bfs, explorados_bfs, visitados_bfs, custo_espaco, custo_tempo, total_nos_gerados = busca_largura(puzzle)
if caminho_bfs is None:
    print("Não foi possível encontrar uma solução.")
else:
    print(f"Caminho encontrado em {len(caminho_bfs)-1} passos:")
    print(f"Custo de espaço (tamanho máximo fronteira de estado): {custo_espaco}")
    print(f"Custo de tempo (nós visitados): {custo_tempo}")
    print(f"Total de nós gerados: {total_nos_gerados}")

puzzle.reset()
puzzle.setNumbers(teste_4)

print("="*70)
print("BUSCA EM PROFUNDIDADE (4)")
print("="*70)
caminho_dfs, explorados_dfs, visitados_dfs, custo_espaco, custo_tempo, profundidade_max, total_nos_gerados = busca_profundidade_visitado(puzzle)
if caminho_dfs is None:
    print("Não foi possível encontrar uma solução.")
else:
    print(f"Caminho encontrado em {len(caminho_dfs)-1} passos:")
    print(f"Custo de espaço (tamanho máximo fronteira de estado): {custo_espaco}")
    print(f"Custo de tempo (nós visitados): {custo_tempo}")
    print(f"Profundidade máxima: {profundidade_max}")
    print(f"Total de nós gerados: {total_nos_gerados}")

puzzle.reset()
puzzle.setNumbers(teste_4)

print("="*70)
print("BUSCA GULOSA (4)")
print("="*70)
caminho_gulosa, explorados_gulosa, visitados_gulosa, custo_espaco, custo_tempo, profundidade_maxima, total_nos_gerados = busca_gulosa(puzzle)
if caminho_gulosa is None:
    print("Não foi possível encontrar uma solução.")
else:
    print(f"Caminho encontrado em {len(caminho_gulosa)-1} passos:")
    print(f"Custo de espaço (tamanho máximo fronteira de estado): {custo_espaco}")
    print(f"Custo de tempo (nós visitados): {custo_tempo}")
    print(f"Profundidade máxima: {profundidade_maxima}")
    print(f"Total de nós gerados: {total_nos_gerados}")

puzzle.reset()
puzzle.setNumbers(teste_4)

print("="*70)
print("BUSCA A* (4)")
print("="*70)
caminho_a_star, explorados_a_star, visitados_a_star, custo_espaco, custo_tempo, profundidade_maxima, total_nos_gerados = busca_a_star(puzzle)
if caminho_a_star is None:
    print("Não foi possível encontrar uma solução.")
else:
    print(f"Caminho encontrado em {len(caminho_a_star)-1} passos:")
    print(f"Custo de espaço (tamanho máximo fronteira de estado): {custo_espaco}")
    print(f"Custo de tempo (nós visitados): {custo_tempo}")
    print(f"Profundidade máxima: {profundidade_maxima}")
    print(f"Total de nós gerados: {total_nos_gerados}")

