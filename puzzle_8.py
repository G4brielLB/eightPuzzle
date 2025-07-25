import random

class Puzzle_8:
    
    def __init__(self):
        self.numbers = [[1,2,3],[4,5,6],[7,8,0]]
        self.white_space = [2,2]
        self.last_num_moved = 0

    def getNumbers(self):
        return self.numbers
    
    def getWhiteSpace(self):
        return self.white_space
    
    def setNumbers(self, new_matrix):
        self.numbers = new_matrix.copy()
        for i in range(len(self.numbers)):
            for j in range(len(self.numbers[i])):
                if(self.numbers[i][j] == 0):
                    self.white_space = [i,j]
    
    def reset(self):
        self.numbers = [[1,2,3],[4,5,6],[7,8,0]]
        self.white_space = [2,2]
        self.last_num_moved = 0
    
    def switchNums(self, num1, num2):
        try:
            pos_1 = self.getPos(num1)
            pos_2 = self.getPos(num2)
            
            new_matrix = self.numbers.copy()
            new_matrix[pos_1[0]][pos_1[1]] = num2
            new_matrix[pos_2[0]][pos_2[1]] = num1
            
            self.setNumbers(new_matrix)
        except Exception as e:
            raise e
    
    def hasWon(self):
        if(self.numbers == [[1,2,3],[4,5,6],[7,8,0]]):
            return True
        return False
    
    def canMove(self, num):
        try:
            num_pos = self.getPos(num)
            if(num_pos[0] == self.white_space[0] and num_pos[1] == self.white_space[1]):
                return False
            if(abs(num_pos[0] - self.white_space[0]) > 1 or abs(num_pos[1] - self.white_space[1]) > 1):
                return False
            if(num_pos[0] == self.white_space[0] or num_pos[1] == self.white_space[1]):
                return True
            return False
        except Exception as e:
            print("erro aqui ó:")
            print(e)
        
    def move(self, num):
        try:
            num_pos = self.getPos(num)
            if(num_pos[1] == self.white_space[1]):
                temp = num_pos[0]
                num_pos[0] = self.white_space[0]
                self.white_space[0] = temp
            elif(num_pos[0] == self.white_space[0]):
                temp = num_pos[1]
                num_pos[1] = self.white_space[1]
                self.white_space[1] = temp
            self.numbers[num_pos[0]][num_pos[1]] = num
            self.numbers[self.white_space[0]][self.white_space[1]] = 0
            self.last_num_moved = num
        except Exception as e:
            print("erro aqui ó:")
            print(e)
        
    def shuffle(self):
        possible_moves = []
        
        for i in range(len(self.numbers)):
            for j in range(len(self.numbers[i])):
                num = self.numbers[i][j]
                if(self.canMove(num) and num != self.last_num_moved):
                    possible_moves.append(num)
        
        if(len(possible_moves) > 0):
            num_to_move = random.choice(possible_moves)
            return num_to_move
        
        return 0
    
    def is_solved(self):
        gabarito = [[1,2,3],[4,5,6],[7,8,0]]
        
        for i in range(len(self.numbers)):
            for j in range(len(self.numbers[i])):
                if(self.numbers[i][j] != gabarito[i][j]):
                    return False
        return True
        
    def getPos(self, num):
        for i in range(len(self.numbers)):
            for j in range(len(self.numbers[i])):
                if(self.numbers[i][j] == num):
                    return [i,j]
        raise Exception("número não encontrado")
