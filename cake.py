import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 300)  # скорость речи
engine.setProperty('volume', 1)  # громкость (0-1)

menu = {'наполеон': [['масло', 'мука', 'сахар'], 7, 1000],
        'медовик': [['мука', 'масло', 'сахар'], 4, 1025],
        'киевский': [['сахар', 'мука', 'масло'], 5, 985]}

a = '''Если вы хотите посмотреть описание, введите 1
    Посмотреть цену - введите 2
    Посмотреть количество - введите 3
    Посмотреть всю информацию - введите 4
    Если выхотите приобрести торт, введите 5
    Для выхода из программы введите 0'''

engine.say('Добрый день!')
engine.runAndWait()

print(a)
engine.say(a)
engine.runAndWait()

s = []
for key in menu.keys():
    s.append(key)

while True:
    products = 'В наличии есть: '
    for i in s:
        products += i + ' '

    engine.say(products)
    engine.runAndWait()

    print('Какой торт вас интересует? ')
    engine.say('Какой торт вас интересует? ')
    engine.runAndWait()

    dish = input().lower()
    if dish == '0':
        print('Всего доброго!')
        engine.say('Всего доброго!')
        engine.runAndWait()
        break

    query = int(input('Введите ваш запрос: '))
    if query == 0:
        print('Всего доброго!')
        engine.say('Всего доброго!')
        engine.runAndWait()
        break

    for key, value in menu.items():
        if dish == key:
            if query == 1:
                text = f'{key.capitalize()} состоит из:', *value[0]
                print(text)
                engine.say(text)
                engine.runAndWait()

            elif query == 2:
                text = f'{key.capitalize()} стоит {value[1]} рублей.'
                print(text)
                engine.say(text)
                engine.runAndWait()

            elif query == 3:
                text = f'Торта {key.capitalize()} осталось {value[2]} грамм'
                print(text)
                engine.say(text)
                engine.runAndWait()

            elif query == 4:
                print(f'{key.capitalize()} состоит из:', *value[0])
                print(f'{key.capitalize()} стоит {value[1]} рублей')
                print(f'{key.capitalize()} осталось {value[2]} грамм')
                text = f'{key.capitalize()} состоит из:', *value[0]
                engine.say(text)
                engine.say(f'{key.capitalize()} стоит {value[1]} рублей')
                engine.say(f'Торта {key.capitalize()} осталось {value[2]}')
                engine.runAndWait()

            elif query == 5:
                engine.say('Какое количество торта вы желаете приобрести? ')
                engine.runAndWait()
                weight = int(input('Какое количество торта вы желаете приобрести? '))

                if weight <= value[2]:
                    value[2] -= weight
                    price = value[1] * weight / 100
                    print(f'К оплате {price}')
                    print(f'Осталось {value[2]} грамм данного товара')
                    engine.say(f'К оплате {price}')
                    engine.say(f'Осталось {value[2]} грамм данного товара')
                    engine.runAndWait()

                elif value[2] == 0:
                    print('К сожалению данного торта не осталось')
                    engine.say('К сожалению данного торта не осталось')
                    engine.runAndWait()

                else:
                    print(f'К сожалению данного торта осталось всего {value[2]} грамм')
                    engine.say(f'К сожалению данного торта осталось всего {value[2]} грамм')
                    engine.say('Хотите приобрести весь оставшийся?')
                    engine.runAndWait()
                    question = input('Хотите приобрести весь оставшийся? (Да/Нет):   ').lower()

                    if question == 'да':
                        weight = value[2]
                        value[2] = 0
                        price = value[1] * weight / 100
                        print(f'К оплате {price} рублей')
                        print(f'Осталось {value[2]} грамм данного товара')
                        engine.say(f'К оплате {price} рублей')
                        engine.say(f'Осталось {value[2]} грамм данного товара')
                        engine.runAndWait()
                        s.remove(dish)


            elif query == 0:
                print('Всего доброго!')
                engine.say('Всего доброго!')
                engine.runAndWait()
                break

            else:
                print('Неверный запрос, повторите попытку...')
                engine.say('Неверный запрос, повторите попытку.')
                engine.runAndWait()
    print()
