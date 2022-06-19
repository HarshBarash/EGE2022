#Одна куча
#Петя, Ваня, Петя, Ваня -> #Четный овтет - Ваня | #Нечётный - петя
#19 - ищем минимальный summ с значением winner = 2
#20 - ищем 2 минимальные summ с значением winner = 3
#20 - ищем минимальную summ с значением winner = 4

# def f(current_player, summ1, final_player):
#     if summ1 >= 34 and summ1 <= 83: return current_player % 2 == final_player % 2
#     if current_player == final_player: return 0
#     games = [f(current_player + 1, summ1 + 2, final_player),
#              f(current_player + 1, summ1 * 3, final_player)]
    #19
    # return any(games)

    #20
    # return any(games) if (current_player + 1) % 2 == final_player % 2 else all(games)

# for summ in range(1, 83 + 1):
#     for games in range(1, 4 + 1):
#         if f(0, summ, games):
#             print('summ = ', summ, ' winner = ', games)


#-----------------------------------------------------------------------------
# две кучи

def f(current_player, summ1, summ2, final_player):
    if summ1 + summ2 >= 74: return current_player % 2 == final_player % 2
    if current_player == final_player: return 0
    games = [f(current_player + 1, summ1 + 1, summ2, final_player),
             f(current_player + 1, summ1 * 2, summ2, final_player),
             f(current_player + 1, summ1, summ2 + 1, final_player),
             f(current_player + 1, summ1, summ2 * 2, final_player), ]
    # 19
    # return any(games)

    # 20
    return any(games) if (current_player + 1) % 2 == final_player % 2 else all(games)

for summ in range(1, 61 + 1):
    for games in range(1, 4 + 1):
        if f(0, 12, summ, games):
            print('summ = ', summ, ' winner = ', games)