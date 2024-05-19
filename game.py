import random
class Game:
    def __init__(self):
        with open("words.txt","r") as f:
            self.worklist = f.read().splitlines()
        self.quest = self.worklist[random.randint(0,len(self.worklist)-1)]
        self.win =""
        #user - победил игрок
        #comp - победил комп
        

   
    #green - зеленый
    #red - красный
    # пустой параметр - белый
    
    #проверка слова
    def check(self, word):
        result = []
        if (word == self.quest):
            for i in word:
                result.append([i, 'green'])
            self.win = "user"    
            return result 

        elif word != self.quest:
            pos =0
            for i in word:
                find = self.quest.find(i) 
                # -1 - не найдена - ""
                # find != pos  - "red"
                # find == pos - "green"

                if find== -1:
                    result.append([i,''])
                elif find==pos:
                    result.append([i,'green'])
                elif find!=pos:
                    result.append([i,'red']) 
                pos+=1
            return result    





        
