a = [float(x) for x in open('sequence.txt')]

pos = 0  #счётчик чисел > 0
neg = 0  #счётчик чисел < 0

spot_pos = f'\x1b[48;5;2m  \x1b[0m'  #зелёный квадрат
spot_neg = f'\x1b[48;5;1m  \x1b[0m'  #красный квадрат

#Количество чисел больше и меньше нуля
for x in a:
    if x > 0:
        pos += 1
    elif x < 0:
        neg += 1

for i in range(max(pos, neg), 0, -1): #генерация чисел от max(pos, neg) до 1 включительно с шагом -1
    if i <= pos and i <= neg: #оба столбца достигают этой строки: печатаем оба
        print(spot_pos, spot_neg)
    elif i <= pos:
        print(spot_pos)
    elif i <= neg: #только красный достаточно высок: печатаем пустое место слева и красный столб
        print('  ', spot_neg)

print(f'\n> 0 : {pos} чисел')
print(f'< 0 : {neg} чисел')
