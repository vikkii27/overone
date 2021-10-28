def calc(a, b, c):
    global res
    if c == '+':
        res = a + b
    elif c == '-':
        res = a - b
    elif c == '/':
        res = a / b
    elif c == '*':
        res = a * b
    else:
        print('Вы ввели неверный символ!')
    return res

a = int(input('Число 1: '))
b = int(input('Число 2: '))
c = input('Введите математический оператор: ')

print(calc(a, b, c))

