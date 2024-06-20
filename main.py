import pygame, pygame_widgets

from game import Game

from symbol import Symbol

from pygame_widgets.button import ButtonArray, Button

from matirx import Matrix
from tkinter import messagebox

pygame.init()

W,H = 600,800

sym_w = 30
sym_h = 60

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Wordle 2.0")



textList = []

for i in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
    textList.append(i)


def game_init():
    global curr_game, matrix, texts_, word, s, level, wordpos
    curr_game = Game()
    matrix = Matrix()
    texts_ = tuple(textList)
    word = ''  # наше слово
    #    0           1       2           3       4
    s = [[' ', ''], [' ', ''], [' ', ''], [' ', ''], [' ', '']]  # буквы вводимого слова в матрицу
    level = 0  # попытка или позиция в матрице
    wordpos = 0  # буква в строке


game_init()


def click_sym_button(ss):
    global level
    global wordpos
    global word
    if (wordpos<=4):
        s[wordpos][0] = ss
        matrix.text_matrix[level] = s
        word+=ss
        wordpos+=1

click_ = (
lambda : click_sym_button('а'),
lambda : click_sym_button('б'),
lambda : click_sym_button('в'),
lambda : click_sym_button('г'),
lambda : click_sym_button('д'),
lambda : click_sym_button('е'),
lambda : click_sym_button('ё'),
lambda : click_sym_button('ж'),
lambda : click_sym_button('з'),
lambda : click_sym_button('и'),
lambda : click_sym_button('й'),
lambda : click_sym_button('к'),
lambda : click_sym_button('л'),
lambda : click_sym_button('м'),
lambda : click_sym_button('н'),
lambda : click_sym_button('о'),
lambda : click_sym_button('п'),
lambda : click_sym_button('р'),
lambda : click_sym_button('с'),
lambda : click_sym_button('т'),
lambda : click_sym_button('у'),
lambda : click_sym_button('ф'),
lambda : click_sym_button('х'),
lambda : click_sym_button('ц'),
lambda : click_sym_button('ч'),
lambda : click_sym_button('ш'),
lambda : click_sym_button('щ'),
lambda : click_sym_button('ъ'),
lambda : click_sym_button('ы'),
lambda : click_sym_button('ь'),
lambda : click_sym_button('э'),
lambda : click_sym_button('ю'),
lambda : click_sym_button('я'),
)


btnArray = ButtonArray(sc,50, 500, 400, 200,
                       (11,3),
                       texts=texts_,
                       onClicks=click_
                       )

def bksp_click():
    global level
    global wordpos
    global word
    global s
    if wordpos>0:
        wordpos-=1
        s[wordpos][0] = ' '
        matrix.text_matrix[level]=s
        word = word[0: len(word)-1]


bksp = Button(sc,50,710, 180, 50,
              text="<<<<<",
              onClick=bksp_click
              )

def check_submit():
    global level
    global wordpos
    global word
    global s
    if (wordpos>4):
        test = curr_game.check(word)
        matrix.text_matrix[level] = test
        level=level+1
        wordpos=0
        s=[[' ',''],[' ',''],[' ',''],[' ',''],[' ','']]
        word = ""
        if curr_game.win=="user":
            bksp.hide()
            checkButton.hide()
            messagebox.showinfo(title="Ура! Победа!", message="Игра окончена! Вы победили!")
            newButton.show()
        elif level>5:
            bksp.hide()
            checkButton.hide()
            messagebox.showinfo(title="Поражение", message="Вы проиграли! Количество попыток исчерпано! Загаданное слово: "+curr_game.quest)
            newButton.show()





checkButton = Button(sc,270,710, 180, 50,
              text="Hа проверку",
              onClick=check_submit
              )

def new_click():
    bksp.show()
    checkButton.show()
    game_init()
    newButton.hide()

newButton = Button(sc,270,710, 180, 50,
              text="Новая игра", onClick=new_click
              )
newButton.hide()


sym = None
    #Symbol(curr_game.quest, W/2, H/2)


while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
           quit()


    sc.fill((0,0,0))
    pos_w=0
    pos_h =0

    for i in range(matrix.level):
        for j in range(5):
            sym = Symbol(matrix.text_matrix[i][j][0], W / 3 + pos_w, H /6 + pos_h,matrix.text_matrix[i][j][1] )
            sc.blit(sym.text, sym.rect)
            pos_w += sym_w
        pos_h += sym_h
        pos_w =0

    pressed = pygame.key.get_pressed()

    if (pressed[pygame.K_SPACE]):
        print(curr_game.quest)
        word = 'кобра'
        s = curr_game.check(word)
        matrix.text_matrix[0] = s




    pygame_widgets.update(events)
    pygame.display.update()


