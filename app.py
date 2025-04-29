import pygame
import time
import threading
from puzzle_8_operator import Puzzle_8_Operator

screen_width = 1000
screen_height = 600

pygame.init()
pygame.display.set_caption('Jogo dos 8')
image_icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(image_icon)
window = pygame.display.set_mode((screen_width,screen_height))
font = pygame.font.SysFont('Tohama',40, True,False)
evenflow = pygame.mixer.Sound("./images/evenflow.mp3")
evenflow.set_volume(0.1)

running = True

puzzle_8_op = Puzzle_8_Operator()
puzzle_8_op.setCanvas(window)
# puzzle_8_op.setNumbers([[1,4,2],[5,0,7],[3,8,6]])

while(running):
    pygame.draw.rect(window, (255,255,255), pygame.Rect(0,0,screen_width, screen_height))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            puzzle_8_op.handleText(event.unicode)
            
            if event.key == pygame.K_s:
                threading.Thread(target=puzzle_8_op.shuffle, args=(20,)).start()
            if event.key == pygame.K_r:
                puzzle_8_op.reset()
            if event.key == pygame.K_e:
                puzzle_8_op.handleEditMode()
            if event.key == pygame.K_g:
                threading.Thread(target=puzzle_8_op.buscaGulosa,).start()
            if event.key == pygame.K_a:
                threading.Thread(target=puzzle_8_op.aStar,).start()
            if event.key == pygame.K_l:
                threading.Thread(target=puzzle_8_op.buscaLargura,).start()
            if event.key == pygame.K_p:
                threading.Thread(target=puzzle_8_op.buscaProfundidade,).start()
            if event.key == pygame.K_m:
                threading.Thread(target=puzzle_8_op.buscaProfundidadeLimitada,).start()
            if event.key == pygame.K_k:
                threading.Thread(target=puzzle_8_op.buscaProfundidadeVisitado,).start()
            if event.key == pygame.K_z:
                puzzle_8_op.zeroMoves()
            if event.key == pygame.K_x:
                evenflow.play()
                
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            puzzle_8_op.handleClick(pos[0],pos[1])
    
    puzzle_8_op.update()
    puzzle_8_op.render()
    
    pygame.display.update()
    time.sleep(0.04)
