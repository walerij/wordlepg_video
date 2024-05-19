import pygame

pygame.init()

W,H = 600,600

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Wordle 2.0")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           quit()


    sc.fill((0,0,0))
    pygame.display.update()


