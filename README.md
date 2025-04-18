# eightPuzzle
 Utilização de diferentes métodos de busca para resolução do jogo dos 8

"""
Este código implementa e testa diferentes métodos de busca para resolver o problema do puzzle 8. 
Os métodos de busca avaliados incluem:

1. Busca em largura.
2. Busca em profundidade e suas variações.
3. Busca gulosa.
4. Busca A* utilizando o algoritmo de Manhattan.

A estrutura do código está organizada da seguinte forma:
- A classe que representa o tabuleiro do puzzle 8 está definida no arquivo `puzzle_8.py`.
- As funções que implementam os métodos de busca estão localizadas no arquivo `metodos_busca.py`.
- O arquivo `main.py` realiza os testes utilizando diferentes configurações de tabuleiros.

Os testes realizados avaliam os seguintes parâmetros:
- Tamanho da solução encontrada.
- Custo de memória, medido pelo tamanho máximo da fronteira de estados.
- Custo de tempo, medido pelo número de nós visitados.
- Profundidade máxima da árvore de busca explorada.
"""