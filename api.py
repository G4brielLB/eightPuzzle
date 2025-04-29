from puzzle_8 import Puzzle_8
from metodos_busca import busca_largura, busca_profundidade, busca_profundidade_limitada, busca_profundidade_visitado, busca_gulosa, busca_a_star
import numpy as np

def conversorCaminho(estados):
    caminho = []
    
    for i, estado in enumerate(estados):
        if(i == 0):
            continue
        
        ultimo_estado = estados[i - 1].numbers
        estado_atual = np.array(estado.numbers)
        zero = np.where(estado_atual == 0) # encontra o zero no estado atual
        zero_index = np.concatenate((zero[0], zero[1]), axis=0).tolist()
        numero_movido = ultimo_estado[zero_index[0]][zero_index[1]] # obtem o número que trocou de lugar com o zero
        caminho.append(numero_movido)
        
    return caminho

def buscaGulosa(numbers):
    puzzle = Puzzle_8()
    puzzle.setNumbers(numbers)
    
    caminho_bfs, _, _, custo_espaco, custo_tempo, _ = busca_gulosa(puzzle)

    caminho = conversorCaminho(caminho_bfs[-30:])
    
    total_moves = len(caminho_bfs)
    
    primeiro_estado = caminho_bfs[0].numbers
    
    if(len(caminho) >= 29):
        primeiro_estado = caminho_bfs[-30].numbers
    
    return caminho, custo_espaco, custo_tempo, primeiro_estado, total_moves

def aStar(numbers):
    puzzle = Puzzle_8()
    puzzle.setNumbers(numbers)
    
    caminho_a_star, _, _, custo_espaco, custo_tempo, _ = busca_a_star(puzzle)

    caminho = conversorCaminho(caminho_a_star[-30:])
    
    total_moves = len(caminho_a_star)
    
    primeiro_estado = caminho_a_star[0].numbers
    
    if(len(caminho) >= 29):
        primeiro_estado = caminho_a_star[-30].numbers
    
    return caminho, custo_espaco, custo_tempo, primeiro_estado, total_moves

def buscaLargura(numbers):
    puzzle = Puzzle_8()
    puzzle.setNumbers(numbers)
    
    caminho_l, _, _, custo_espaco, custo_tempo = busca_largura(puzzle)

    caminho = conversorCaminho(caminho_l[-30:])
    
    total_moves = len(caminho_l)
    
    primeiro_estado = caminho_l[0].numbers
    
    if(len(caminho) >= 29):
        primeiro_estado = caminho_l[-30].numbers
    
    return caminho, custo_espaco, custo_tempo, primeiro_estado, total_moves

def buscaProfundidade(numbers):
    puzzle = Puzzle_8()
    puzzle.setNumbers(numbers)
    
    caminho_profundidade, _, _, custo_espaco, custo_tempo, profundidade = busca_profundidade(puzzle)

    caminho = conversorCaminho(caminho_profundidade[-30:])
    
    total_moves = len(caminho_profundidade)
    
    primeiro_estado = caminho_profundidade[0].numbers
    
    if(len(caminho) >= 29):
        primeiro_estado = caminho_profundidade[-30].numbers
    
    return caminho, custo_espaco, custo_tempo, primeiro_estado, total_moves, profundidade

def buscaProfundidadeLimitada(numbers):
    puzzle = Puzzle_8()
    puzzle.setNumbers(numbers)
    
    caminho_pl, _, _, custo_espaco, custo_tempo, profundidade_max  = busca_profundidade_limitada(puzzle, 150)

    caminho = conversorCaminho(caminho_pl[-30:])
    
    total_moves = len(caminho_pl)
    
    primeiro_estado = caminho_pl[0].numbers
    
    if(len(caminho) >= 29):
        primeiro_estado = caminho_pl[-30].numbers
        
    return caminho, custo_espaco, custo_tempo, primeiro_estado, total_moves, profundidade_max

def buscaProfundidadeVisitado(numbers):
    puzzle = Puzzle_8()
    puzzle.setNumbers(numbers)
    
    caminho_pv, _, _, custo_espaco, custo_tempo, profundidade = busca_profundidade_visitado(puzzle)

    caminho = conversorCaminho(caminho_pv[-30:])
    
    total_moves = len(caminho_pv)
    
    primeiro_estado = caminho_pv[0].numbers
    
    if(len(caminho) >= 29):
        primeiro_estado = caminho_pv[-30].numbers
    
    return caminho, custo_espaco, custo_tempo, primeiro_estado, total_moves, profundidade
