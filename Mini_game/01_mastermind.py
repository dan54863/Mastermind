# -*- coding: utf-8 -*-
from termcolor import colored, cprint
from engine import make_num as start, check_num as check
from AI import ai_step
# Правила:
# Компьютер загадывает четырехзначное число, все цифры которого различны
# (первая цифра числа отлична от нуля). Игроку необходимо разгадать задуманное число.
# Игрок вводит четырехзначное число c неповторяющимися цифрами,
# компьютер сообщают о количестве «быков» и «коров» в названном числе
# «бык» — цифра есть в записи задуманного числа и стоит в той же позиции,
#       что и в задуманном числе
# «корова» — цифра есть в записи задуманного числа, но не стоит в той же позиции,
#       что и в задуманном числе
#
# Например, если задумано число 3275 и названо число 1234,
# получаем в названном числе одного «быка» и одну «корову».
# Очевидно, что число отгадано в том случае, если имеем 4 «быка».
#
# Формат ответа компьютера
# > быки - 1, коровы - 1

cls = lambda: print('\n'*3)

while True:

    cprint("Выберите режим игры ", color="red")
    cprint("1 - Игра ИИ, 2 - Игра для Человека ", color="red")
    type_g = input()
    cls()
    if int(type_g) == 1:
        cprint("Сейчас загадаем число", color="red")
        cprint("Игра начинается!", color="red")
        game_num = start()
        cprint("Число ИИ", color="yellow")
        number = 1000
        step = 1
        fun_v = 0
        trying = 0
        while not check(game_num, number):
            step = step + 1
            number, trying = ai_step(fun_v, game_num, number, trying)
            fun_v = fun_v + 1
        print("\nИИ прошел игру за ", step*trying, "ходов!\n")
        cprint("Желаете сыграть еще? (1 - Да , 2 - Нет)", color="green")
        game = input()
        if int(game) == 1:
            True
        else:
            cprint("Хорошего дня!", color="white")
            break
    else:
        while True:
            cprint("Сейчас загадаем число", color="green")
            cprint("Игра начинается!", color="red")
            game_num = start()
            cprint("Введите Ваше число!", color="yellow")
            number = input()
            step = 1
            while not check(game_num, number):
                step = step + 1
                cprint("Введите Ваше число!", color="yellow")
                number = input()
            print("\nВерно, Вы прошли игру за ", step, "ходов!\n")
            cprint("Желаете сыграть еще? (1 - Да , 2 - Нет)", color="green")
            game = input()
            if int(game) == 1:
                True
            else:
                cprint("Хорошего дня!", color="white")
                break
        break

