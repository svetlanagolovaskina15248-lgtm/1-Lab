
spot = '\x1b[48;5;0m  \x1b[0m' #фон = черный квадрат
empty = '  ' #пробелы в фоне

pattern = [ [1, 0, 1], [0, 1, 0], [1, 0, 1]] #вложенный список, описывающий узор (1 - черный, 0 - пробел)

for row in pattern:
    line = '' #пустая строка в которую добавляем значения pattern
    for cell in row:
        if cell == 1:
            line += spot
        else:
            line += empty
    print(line)