RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END = '\u001b[0m'


height = 6 #количество строк = циков (ширина)
length = 5 #количество пробелов (длина)


for i in range (height):
        print(f'{BLUE}{"  " * length}',f'{WHITE}{"  " * length} ',f'{RED}{"  " * length }{END}') 
        #строка начинающаяся с кода цвета, затем два пробела length раз 



