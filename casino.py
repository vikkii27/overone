# Напишите программу, которая генерирует случайное число от 1 до 10. Игроку дается 3 попытки, чтобы угадать это число.
# Если вы совершили ошибку, программа подскажет какое значение надо взять (больше или меньше).
import random

a = random.randrange(0,10,1)
for i in range(0, 4):
    if i == 3:
        print('Вы проиграли:(')
    else:
        print('Попытка №', i+1)
        b = int(input())
        if b > a:
            print('Много')
        if b < a:
            print ('Мало')
        if b == a:
            print('Вы победили!')
            break