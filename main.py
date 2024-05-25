import pygame
from game import Game
from symbol import Symbol

from matirx import Matrix

pygame.init()

W,H = 600,800

sym_w = 30
sym_h = 60

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Wordle 2.0")

matrix = Matrix()

curr_game = Game()
sym = None
    #Symbol(curr_game.quest, W/2, H/2)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           quit()


    sc.fill((0,0,0))
    pos_w=0
    pos_h =0
    '''
    for i in curr_game.quest:
        sym = Symbol(i, W/3+pos_w, H/2+pos_h)
        sc.blit(sym.text, sym.rect)
        pos += sym_w
   '''
    for i in range(matrix.level):
        for j in range(5):
            sym = Symbol(matrix.text_matrix[i][j][0], W / 3 + pos_w, H /5 + pos_h)
            sc.blit(sym.text, sym.rect)
            pos_w += sym_w
        pos_h += sym_h
        pos_w =0



    pygame.display.update()


