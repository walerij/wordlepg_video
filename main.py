import pygame
from game import Game
from symbol import Symbol

pygame.init()

W,H = 600,600

sym_w = 50
sym_h = 50

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Wordle 2.0")

curr_game = Game()
sym = None
    #Symbol(curr_game.quest, W/2, H/2)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           quit()


    sc.fill((0,0,0))
    pos=0
    for i in curr_game.quest:
        sym = Symbol(i, W/3+pos, H/2)
        sc.blit(sym.text, sym.rect)
        pos += sym_w

    pygame.display.update()


