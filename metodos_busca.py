from copy import deepcopy
import heapq
from itertools import count

gabarito = [[1,2,3],[4,5,6],[7,8,0]]

def serialize(matrix):
    return ''.join(str(num) for row in matrix for num in row)


def busca_largura(puzzle_inicial):
    initial_state = deepcopy(puzzle_inicial)
    visited = set()
    queue = [(initial_state, [])]  # (estado atual, caminho)
    explored_nodes = []

    max_queue_size = 1  # custo de memória (máximo tamanho da fronteira)
    num_visited_nodes = 0  # nós efetivamente visitados (com filhos gerados)
    total_nodes_generated = 1  # inclui o nó inicial

    while queue:
        # Atualiza o custo de memória
        max_queue_size = max(max_queue_size, len(queue))

        current_puzzle, path = queue.pop(0)
        serialized = serialize(current_puzzle.getNumbers())

        #if serialized in visited:
        #    continue

        # Marca como visitado e conta o nó
        visited.add(serialized)
        explored_nodes.append(current_puzzle)
        num_visited_nodes += 1

        # Verifica se é solução
        if current_puzzle.is_solved():
            return path + [current_puzzle], explored_nodes, visited, max_queue_size, num_visited_nodes, total_nodes_generated

        # Gera os filhos (movimentos possíveis)
        white_i, white_j = current_puzzle.getWhiteSpace()
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        for dx, dy in directions:
            ni, nj = white_i + dx, white_j + dy
            if 0 <= ni < 3 and 0 <= nj < 3:
                num_to_move = current_puzzle.getNumbers()[ni][nj]
                if current_puzzle.canMove(num_to_move):
                    new_puzzle = deepcopy(current_puzzle)
                    new_puzzle.move(num_to_move)
                    total_nodes_generated += 1  # Incrementa sempre que um novo nó é gerado
                    serialized_new = serialize(new_puzzle.getNumbers())
                    if serialized_new not in visited:
                        queue.append((new_puzzle, path + [current_puzzle]))

    return None, explored_nodes, visited, max_queue_size, num_visited_nodes, total_nodes_generated



# Busca em profundidade
# FUNÇÃO NÃO UTILIZADA
def busca_profundidade(puzzle):
    initial_state = deepcopy(puzzle)
    visited = set()
    stack = [(initial_state, [])]  # (estado atual, caminho até aqui)
    explored_nodes = []

    max_stack_size = 1  # custo de memória (máximo tamanho da fronteira)
    num_visited_nodes = 0  # nós efetivamente visitados (com filhos gerados)

    while stack:
        # Atualiza o custo de memória
        max_stack_size = max(max_stack_size, len(stack))

        current_puzzle, path = stack.pop()  # Agora usando pilha (LIFO)
        serialized = serialize(current_puzzle.getNumbers())

        visited.add(serialized)
        explored_nodes.append(current_puzzle)
        num_visited_nodes += 1

        # Verifica se é a solução
        if current_puzzle.is_solved():
            profundidade_solucao = len(path)
            return path + [current_puzzle], explored_nodes, visited, max_stack_size, num_visited_nodes, profundidade_solucao

        # Gera os filhos (movimentos possíveis)
        white_i, white_j = current_puzzle.getWhiteSpace()
        directions = [(-1,0), (1,0), (0,-1), (0,1)]  # cima, baixo, esquerda, direita

        for dx, dy in directions:
            ni, nj = white_i + dx, white_j + dy
            if 0 <= ni < 3 and 0 <= nj < 3:
                num_to_move = current_puzzle.getNumbers()[ni][nj]
                if current_puzzle.canMove(num_to_move):
                    new_puzzle = deepcopy(current_puzzle)
                    new_puzzle.move(num_to_move)
                    serialized_new = serialize(new_puzzle.getNumbers())
                    # NÃO checamos se já visitamos o estado
                    stack.append((new_puzzle, path + [current_puzzle]))

    return None, explored_nodes, visited, max_stack_size, num_visited_nodes, 0  # profundidade 0 se falhar


# FUNÇÃO NÃO UTILIZADA
def busca_profundidade_limitada(puzzle_inicial, limite):
    initial_state = deepcopy(puzzle_inicial)
    stack = [(initial_state, [], 0, set())]  # (estado atual, caminho, profundidade, visitados no caminho)
    max_stack_size = 1
    num_visited_nodes = 0
    explored_nodes = []

    while stack:
        max_stack_size = max(max_stack_size, len(stack))

        current_puzzle, path, profundidade, visited = stack.pop()
        serialized = serialize(current_puzzle.getNumbers())

        if serialized in visited:
            continue  # já passei por esse estado nesse caminho

        visited.add(serialized)
        explored_nodes.append(current_puzzle)
        num_visited_nodes += 1

        if current_puzzle.is_solved():
            return path + [current_puzzle], explored_nodes, visited, max_stack_size, num_visited_nodes, profundidade

        if profundidade < limite:
            white_i, white_j = current_puzzle.getWhiteSpace()
            directions = [(-1,0), (1,0), (0,-1), (0,1)]

            for dx, dy in directions:
                ni, nj = white_i + dx, white_j + dy
                if 0 <= ni < 3 and 0 <= nj < 3:
                    num_to_move = current_puzzle.getNumbers()[ni][nj]
                    if current_puzzle.canMove(num_to_move):
                        new_puzzle = deepcopy(current_puzzle)
                        new_puzzle.move(num_to_move)
                        # copia do visited para o novo caminho
                        stack.append((new_puzzle, path + [current_puzzle], profundidade + 1, visited.copy()))

    return None, explored_nodes, set(), max_stack_size, num_visited_nodes, 0


# FUNÇÃO BUSCA EM PROFUNDIDADE UTILIZADA
def busca_profundidade_visitado(puzzle):
    initial_state = deepcopy(puzzle)
    visited = set()
    stack = [(initial_state, [])]  # (estado atual, caminho até aqui)
    explored_nodes = []

    max_stack_size = 1  # custo de memória (máximo tamanho da fronteira)
    num_visited_nodes = 0  # nós efetivamente visitados (com filhos gerados)
    total_nodes_generated = 1  # inclui o nó inicial

    while stack:
        # Atualiza o custo de memória
        max_stack_size = max(max_stack_size, len(stack))

        current_puzzle, path = stack.pop()  # Agora usando pilha (LIFO)
        serialized = serialize(current_puzzle.getNumbers())

        # Verifica se já foi visitado
        if serialized in visited:
            continue

        visited.add(serialized)
        explored_nodes.append(current_puzzle)
        num_visited_nodes += 1

        # Verifica se é a solução
        if current_puzzle.is_solved():
            profundidade_solucao = len(path)
            return path + [current_puzzle], explored_nodes, visited, max_stack_size, num_visited_nodes, profundidade_solucao, total_nodes_generated

        # Gera os filhos (movimentos possíveis)
        white_i, white_j = current_puzzle.getWhiteSpace()
        directions = [(-1,0), (1,0), (0,-1), (0,1)]  # cima, baixo, esquerda, direita

        for dx, dy in directions:
            ni, nj = white_i + dx, white_j + dy
            if 0 <= ni < 3 and 0 <= nj < 3:
                num_to_move = current_puzzle.getNumbers()[ni][nj]
                if current_puzzle.canMove(num_to_move):
                    new_puzzle = deepcopy(current_puzzle)
                    new_puzzle.move(num_to_move)
                    total_nodes_generated += 1  # Incrementa sempre que um novo nó é gerado
                    serialized_new = serialize(new_puzzle.getNumbers())
                    if serialized_new not in visited:  # Evita adicionar estados já visitados
                        stack.append((new_puzzle, path + [current_puzzle]))

    return None, explored_nodes, visited, max_stack_size, num_visited_nodes, 0, total_nodes_generated  # profundidade 0 se falhar


# Definindo a heurística de Manhattan
# A função calcula a soma das distâncias de Manhattan de cada número em relação à sua posição correta
def manhattan(puzzle):
    total = 0
    for i in range(3):
        for j in range(3):
            value = puzzle[i][j]
            if value != 0:
                target_x = (value - 1) // 3
                target_y = (value - 1) % 3
                total += abs(i - target_x) + abs(j - target_y)
    return total

# Busca heuristica (gulosa)
# A função de busca gulosa utiliza a heurística de Manhattan para priorizar os estados que estão mais próximos da solução.
# Ela utiliza uma fila de prioridade (heap) para armazenar os estados.
def busca_gulosa(puzzle_inicial):
    initial_state = deepcopy(puzzle_inicial)
    visited = set()
    explored_nodes = []

    heap = []
    counter = count()  # para evitar comparação entre objetos
    heuristica = manhattan(initial_state.getNumbers())
    heapq.heappush(heap, (heuristica, next(counter), initial_state, []))  # (heurística, estado, caminho)

    max_heap_size = 1
    num_visited_nodes = 0
    profundidade_maxima = 0
    total_nodes_generated = 1  # inclui o nó inicial

    while heap:
        max_heap_size = max(max_heap_size, len(heap))

        _, _, current_puzzle, path = heapq.heappop(heap)
        serialized = serialize(current_puzzle.getNumbers())

        if serialized in visited:
            continue

        visited.add(serialized)
        explored_nodes.append(current_puzzle)
        num_visited_nodes += 1

        profundidade_maxima = max(profundidade_maxima, len(path))
        
        if current_puzzle.is_solved():
            return path + [current_puzzle], explored_nodes, visited, max_heap_size, num_visited_nodes, profundidade_maxima, total_nodes_generated

        white_i, white_j = current_puzzle.getWhiteSpace()
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        for dx, dy in directions:
            ni, nj = white_i + dx, white_j + dy
            if 0 <= ni < 3 and 0 <= nj < 3:
                num_to_move = current_puzzle.getNumbers()[ni][nj]
                if current_puzzle.canMove(num_to_move):
                    new_puzzle = deepcopy(current_puzzle)
                    new_puzzle.move(num_to_move)
                    total_nodes_generated += 1  # Incrementa sempre que um novo nó é gerado
                    serialized_new = serialize(new_puzzle.getNumbers())
                    if serialized_new not in visited:
                        h = manhattan(new_puzzle.getNumbers())
                        heapq.heappush(heap, (h, next(counter), new_puzzle, path + [current_puzzle]))

    return None, explored_nodes, visited, max_heap_size, num_visited_nodes, profundidade_maxima, total_nodes_generated

def busca_a_star(puzzle_inicial):
    initial_state = deepcopy(puzzle_inicial)
    visited = set()
    explored_nodes = []

    heap = []
    counter = count()
    heuristica = manhattan(initial_state.getNumbers())
    heapq.heappush(heap, (heuristica, next(counter), 0, initial_state, []))  

    max_heap_size = 1
    num_visited_nodes = 0
    profundidade_maxima = 0
    total_nodes_generated = 1  # inclui o nó inicial

    while heap:
        max_heap_size = max(max_heap_size, len(heap))

        _, _, g, current_puzzle, path = heapq.heappop(heap)
        serialized = serialize(current_puzzle.getNumbers())

        if serialized in visited:
            continue

        visited.add(serialized)
        explored_nodes.append(current_puzzle)
        num_visited_nodes += 1

        profundidade_maxima = max(profundidade_maxima, len(path))

        if current_puzzle.is_solved():
            return path + [current_puzzle], explored_nodes, visited, max_heap_size, num_visited_nodes, profundidade_maxima, total_nodes_generated

        white_i, white_j = current_puzzle.getWhiteSpace()
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        for dx, dy in directions:
            ni, nj = white_i + dx, white_j + dy
            if 0 <= ni < 3 and 0 <= nj < 3:
                num_to_move = current_puzzle.getNumbers()[ni][nj]
                if current_puzzle.canMove(num_to_move):
                    new_puzzle = deepcopy(current_puzzle)
                    new_puzzle.move(num_to_move)
                    total_nodes_generated += 1  # Incrementa sempre que um novo nó é gerado
                    serialized_new = serialize(new_puzzle.getNumbers())
                    if serialized_new not in visited:
                        new_g = g + 1  # Custo real aumenta 1 a cada movimento
                        h = manhattan(new_puzzle.getNumbers())
                        f = new_g + h
                        heapq.heappush(heap, (f, next(counter), new_g, new_puzzle, path + [current_puzzle])) # (f = g+h, contador, g, estado, caminho)

    return None, explored_nodes, visited, max_heap_size, num_visited_nodes, profundidade_maxima, total_nodes_generated
