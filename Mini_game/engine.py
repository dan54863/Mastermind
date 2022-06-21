import random

# Составить отдельный модуль mastermind_engine, реализующий функциональность игры.
# В этом модуле нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.
num = 0
def make_num():
    global num
    num = 0
    while not check_genetator(num):
        num = random.randint(1000, 9999)
    return(num)


def check_genetator(num):
    try:
        number_list = list(str(num))
        if len(set(number_list)) == 4:
            return True
        else:
            return False
    except:
        return False


def check_num(num, player_n):
    dictionary = {"Быки": 0, "Коровы": 0}
    diff = []
    number_ingame = list(str(num))
    player_num = list(str(player_n))
    for i in range(len(number_ingame)):
        # сравниваем элементы первого списка
        # с элементами второго списка
        if number_ingame[i] == player_num[i]:

            # элемент из первого, если он меньше
            dictionary["Быки"] += 1
            diff.append(number_ingame[i])

    number_ingame = set(number_ingame)
    player_num = set(player_num)
    a = len((number_ingame & player_num) - set(diff))
    dictionary["Коровы"] += a
    if dictionary["Быки"] == 4:
        return True
    else:
        print(dictionary)
        return False


