
def ai_step(fun_v, game_num, answer, trying):
    if fun_v == 0:
        while ch_for_ai(game_num, answer, fun_v):
            answer = answer + 1000
            trying = trying + 1
    if fun_v == 1:
        while ch_for_ai(game_num, answer, fun_v):
            answer = answer + 100
            trying = trying + 1
    if fun_v == 2:
        while ch_for_ai(game_num, answer, fun_v):
            answer = answer + 10
            trying = trying + 1
    if fun_v == 3:
        while ch_for_ai(game_num, answer, fun_v):
            answer = answer + 1
            trying = trying + 1
    print("Ваше число", answer)
    return answer, trying


def ch_for_ai(game_num, answer, fun_v):
    dictionary = {"Быки": 0}
    number_ingame = list(str(game_num))
    player_num = list(str(answer))
    for fun_v in range(fun_v+1):
        # сравниваем элементы первого списка
        # с элементами второго списка
        if number_ingame[fun_v] == player_num[fun_v]:
            dictionary["Быки"] += 1

    if dictionary["Быки"] == fun_v+1:
        return False
    else:
        return True
