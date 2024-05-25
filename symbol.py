import pygame
class Symbol(pygame.sprite.Sprite):
    def __init__(self, text, x, y):
        self.font = pygame.font.SysFont("courier",40)
        self.default_color = ((0,0,0),(201, 201, 197))
        self.correct_color = ((0,0,0),(14, 163, 11))
        self.wrong_color = ((0, 0, 0), (232, 28, 21))
        self.textcolor = self.default_color[0]
        self.bgcolor = self.default_color[1]
        self.text = self.font.render(text, True, self.textcolor, self.bgcolor)
        self.rect = self.text.get_rect(center=(x,y))