import pygame
import time
from puzzle_8 import Puzzle_8
from api import buscaGulosa, aStar, buscaProfundidade, buscaProfundidadeVisitado, buscaProfundidadeLimitada, buscaLargura

class Puzzle_8_Operator:
    
    def __init__(self):
        self.canvas = None
        self.x = 280
        self.y = 150
        
        self.blocks = []
        self.puzzle_8 = Puzzle_8()
        self.updateNumbers()

        self.editing_block = None
        self.edit_mode = False
        self.isShuffling = False
        self.shuffle_stack = []
        self.moves = 0
        self.moving = False
        
        self.font = pygame.font.SysFont('rubik', 30)
        
        self.memory_label = ""
        self.time_label = ""
        self.search_label = ""
        self.depth_label = ""
        
        self.animation = []
        self.background_animation = []
        self.animation_frame = 0
        self.background_animation_frame = 0
        self.loadConfettiAnimation()
        self.loadBackgroundAnimation()
        
    def loadConfettiAnimation(self):
        try:
            for number in range(10):
                image = pygame.image.load("./images/confetti/confetti-28.png")
                self.animation.append(image)
                self.animation_frame += 1
            for number in range(59):
                image = pygame.image.load("./images/confetti/confetti-"+str((number+29) % 59)+".png")
                self.animation.append(image)
                self.animation_frame += 1
        except Exception as e:
            print("erro no carregamento da animacao do confete:",e)
        
    def loadBackgroundAnimation(self):
        try:
            for number in range(31):
                formated_number = f"{number:03}"
                image = pygame.image.load("./images/background/sunset-loop_"+formated_number+".jpg")
                self.background_animation.append(image)
        except Exception as e:
            print("erro no carregamento da animacao:",e)
        
    def setCanvas(self, new_canvas):
        self.canvas = new_canvas
        
    def handleEditMode(self):
        self.edit_mode = not self.edit_mode
        
    def win(self):
        if(self.animation_frame >= len(self.animation)):
            self.animation_frame = 0
        
    def shuffle(self, moves):
        self.isShuffling = True
        self.shuffle_stack.append(1)
        
        for _ in range(moves):
            num_to_move = self.puzzle_8.shuffle()
            if(num_to_move != 0):
                self.moveBlock(num_to_move)
            time.sleep(0.3)
        
        self.shuffle_stack.pop()
        if(len(self.shuffle_stack) == 0):
            self.isShuffling = False
        
    def moveSequence(self, sequence):
        if self.moving:
            return
        
        self.moving = True
        
        for num in sequence:
            if(self.puzzle_8.canMove(num)):
                self.moveBlock(num)
            time.sleep(0.3)
        
        self.moving = False
        
    def reset(self):
        self.puzzle_8.reset()
        # self.puzzle_8.setNumbers([[1,2,3],[4,5,6],[7,8,0]])
        self.updateNumbers()
        self.moves = 0
        self.memory_label = self.time_label = ""
        self.search_label = ""
        self.depth_label = ""
        
    def updateNumbers(self):
        self.blocks.clear()
        puzzle_numbers = self.puzzle_8.getNumbers()
        puzzle_white_space = self.puzzle_8.getWhiteSpace()
        square_size = 80
        
        for row in range(len(puzzle_numbers)):
            for line in range(len(puzzle_numbers[row])):
                if(line == puzzle_white_space[0] and row == puzzle_white_space[1]):
                    continue
                self.blocks.append(Block(self.x + row * square_size, self.y + line * square_size, puzzle_numbers[line][row]))
        
    def setNumbers(self, new_matrix):
        self.puzzle_8.setNumbers(new_matrix)
        self.updateNumbers()
        
    def handleClick(self, x, y):
        if(self.isShuffling):
            return
        
        for block in self.blocks:
            block_rect = block.getRect()
            if(x >= block_rect[0] and y >= block_rect[1] and x < block_rect[2] and y < block_rect[3]):
                if(self.edit_mode):
                    self.editing_block = block
                else:
                    if(self.puzzle_8.canMove(block.getNum())):
                        self.moveBlock(block.getNum())
        
    def handleText(self, text):
        if(self.edit_mode == True):
            try:
                num = int(text)
                self.puzzle_8.switchNums(self.editing_block.getNum(), num)
                self.updateNumbers()
            except Exception as e:
                print(e)
                print("rapaz... (som do ratinho)")
                
    def buscaProfundidade(self):
        profundidade_move_sequence, tempo, memoria, primeiro_estado, total_moves, profundidade = buscaProfundidade(self.puzzle_8.getNumbers())
        
        if(len(profundidade_move_sequence) == 0):
            return
        
        self.search_label = "Busca em Profundidade"
                    
        self.setNumbers(primeiro_estado)
        self.updateNumbers()
        
        if(len(profundidade_move_sequence) == 29):
            self.moves = total_moves - 29
            
        self.showInfo(tempo, memoria, profundidade)   
        self.moveSequence(profundidade_move_sequence)
        
    def buscaProfundidadeLimitada(self):
        limitada_move_sequence, tempo, memoria, primeiro_estado, total_moves, profundidade_max = buscaProfundidadeLimitada(self.puzzle_8.getNumbers())
        
        if(len(limitada_move_sequence) == 0):
            return
        
        self.search_label = "Profundidade Limitada"
                    
        self.setNumbers(primeiro_estado)
        self.updateNumbers()
        
        if(len(limitada_move_sequence) == 29):
            self.moves = total_moves - 29
            
        self.showInfo(tempo, memoria, profundidade_max)
        self.moveSequence(limitada_move_sequence)
        
    def zeroMoves(self):
        if self.moving:
            return
        self.moves = 0
        
    def buscaProfundidadeVisitado(self):
        visitado_move_sequence, tempo, memoria, primeiro_estado, total_moves, profundidade = buscaProfundidadeVisitado(self.puzzle_8.getNumbers())
        
        if(len(visitado_move_sequence) == 0):
            return
        
        self.search_label = "Profundidade Visitados"
                    
        self.setNumbers(primeiro_estado)
        self.updateNumbers()
        
        if(len(visitado_move_sequence) == 29):
            self.moves = total_moves - 29
            
        self.showInfo(tempo, memoria, profundidade)
        self.moveSequence(visitado_move_sequence)
        
    def buscaGulosa(self):
        gulosa_move_sequence, tempo, memoria, primeiro_estado, total_moves = buscaGulosa(self.puzzle_8.getNumbers())
        
        if(len(gulosa_move_sequence) == 0):
            return
        
        self.search_label = "Busca Gulosa ≥¬≤"
                    
        self.setNumbers(primeiro_estado)
        self.updateNumbers()
        
        if(len(gulosa_move_sequence) == 29):
            self.moves = total_moves - 29
            
        self.showInfo(tempo, memoria, "")
        self.moveSequence(gulosa_move_sequence)
        
    def aStar(self):
        a_star_move_sequence, tempo, memoria, primeiro_estado, total_moves = aStar(self.puzzle_8.getNumbers())
        
        if(len(a_star_move_sequence) == 0):
            return
                    
        self.search_label = "A star *"
        
        self.setNumbers(primeiro_estado)
        self.updateNumbers()
        
        if(len(a_star_move_sequence) == 29):
            self.moves = total_moves - 29
        
        self.showInfo(tempo, memoria, "")     
        self.moveSequence(a_star_move_sequence)
        
    def buscaLargura(self):
        busca_largura_move_sequence, tempo, memoria, primeiro_estado, total_moves = buscaLargura(self.puzzle_8.getNumbers())
        
        if(len(busca_largura_move_sequence) == 0):
            return
        
        self.search_label = "Busca em Largura"
        
        if(len(busca_largura_move_sequence) == 29):
            self.moves = total_moves - 29
                    
        self.setNumbers(primeiro_estado)
        self.updateNumbers()
        
        if(len(busca_largura_move_sequence) == 29):
            self.moves = total_moves - 29
            
        self.showInfo(tempo, memoria, "")    
        self.moveSequence(busca_largura_move_sequence)
        
    def showInfo(self, memory, time, profundidade):
        self.time_label = "Custo de tempo: " + str(time)
        self.memory_label = "Custo de espaço: " + str(memory)
        if(profundidade != ""):
            self.depth_label = "Profundidade máxima: " + str(profundidade)
        else:
            self.depth_label = ""
        
    def moveBlock(self, block_num):
        block = self.getBlock(block_num)
        
        new_pos = self.puzzle_8.getWhiteSpace().copy()
        self.puzzle_8.move(block.getNum())
        block.moveTo(self.x + new_pos[1] * block.getSquareSize(), self.y + new_pos[0] * block.getSquareSize())
        
        if not self.isShuffling:
            self.moves += 1
            
            if(self.puzzle_8.hasWon()):
                self.win()
        
    def getBlock(self, num):
        for block in self.blocks:
            if(block.getNum() == num):
                return block
        raise Exception("bloco não encontrado")
        
    def update(self):
        for block in self.blocks:
            block.update()
        
    def render(self):
        self.canvas.blit(self.background_animation[self.background_animation_frame], (-10,0))
        self.background_animation_frame = (self.background_animation_frame + 1) % len(self.background_animation)
        
        moves_label = self.font.render("movimentos: " + str(self.moves), False, (252, 186, 3))
        self.canvas.blit(moves_label, (50,50))

        time_label = self.font.render(self.time_label, False, (252, 200, 3))
        self.canvas.blit(time_label, (50,505))
        
        memory_label = self.font.render(self.memory_label, False, (252, 200, 3))
        self.canvas.blit(memory_label, (50,535))
        
        depth_label = self.font.render(self.depth_label, False, (252, 200, 3))
        self.canvas.blit(depth_label, (50,565))

        search_label = self.font.render(self.search_label, False, (252, 200, 3))
        self.canvas.blit(search_label, (50,100))
        
        self.canvas.blit(self.font.render("Busca Gulosa: G", False, (252, 200, 3)), (580,50))
        self.canvas.blit(self.font.render("A*: A", False, (252, 200, 3)), (580,80))
        self.canvas.blit(self.font.render("Busca em Largura: L", False, (252, 200, 3)), (580,110))
        self.canvas.blit(self.font.render("Busca em Profundidade: P", False, (252, 200, 3)), (580,140))
        self.canvas.blit(self.font.render("Profundidade Limitada: M", False, (252, 200, 3)), (580,170))
        self.canvas.blit(self.font.render("Profundidade Visitados: K", False, (252, 200, 3)), (580,200))
        self.canvas.blit(self.font.render("Resetar: R", False, (252, 200, 3)), (580,230))
        self.canvas.blit(self.font.render("Embaralhar: S", False, (252, 200, 3)), (580,260))
        self.canvas.blit(self.font.render("Edit mode: E", False, (252, 200, 3)), (580,290))
        
        if(self.edit_mode):
            edit_label = self.font.render("edit mode", False, (252, 50, 3))
            self.canvas.blit(edit_label, (600,50))
        
        for block in self.blocks:
            block.render(self.canvas)
                
        if(self.animation_frame < len(self.animation)):
            self.canvas.blit(self.animation[self.animation_frame], (144,88))
            self.animation_frame += 1
            
class Block():
    
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.square_size = 80
        self.num = num
        self.future_x = x
        self.future_y = y
        self.speed = 7

        font = pygame.font.SysFont('rubik', 30)
        
        self.image = pygame.image.load("./images/wood_block.bmp")
        
        self.label = font.render(str(num), False, (59, 31, 7))
        
    def getNum(self):
        return self.num
        
    def getRect(self):
        return [self.x, self.y, self.x + self.square_size, self.y + self.square_size]
        
    def moveTo(self, new_x, new_y):
        self.future_x = new_x
        self.future_y = new_y
        
    def update(self):
        diff_x = abs(self.future_x - self.x)
        diff_y = abs(self.future_y - self.y)
        
        if(diff_x > self.speed):
            if(self.x > self.future_x):
                self.x -= self.speed
            elif(self.x < self.future_x):
                self.x += self.speed
        else:
            if(self.x > self.future_x):
                self.x -= diff_x
            elif(self.x < self.future_x):
                self.x += diff_x
        if(diff_y > self.speed):
            if(self.y > self.future_y):
                self.y -= self.speed
            elif(self.y < self.future_y):
                self.y += self.speed
        else:
            if(self.y > self.future_y):
                self.y -= diff_y
            elif(self.y < self.future_y):
                self.y += diff_y
        
    def render(self, canvas):
        canvas.blit(self.image, pygame.Rect(self.x, self.y, self.square_size, self.square_size))
        centered_rect = self.label.get_rect(center=(self.x + self.square_size/2,self.y + self.square_size/2))
        canvas.blit(self.label, centered_rect)
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getSquareSize(self):
        return self.square_size
        
