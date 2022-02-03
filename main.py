
def loss_check(game_table, step):
    print('Проверил')





def human_step(game_table):
    try:
        step = int(input('Введи номер элемента - ', ))
    except ValueError:
        print('Введите число от 0 до 99')
        human_step(game_table)
    valid_step(step, game_table, gamer='human')
    print(*game_table, sep='\n')
    print('_' * 75)
    return game_table


def computer_step(game_table):
    print('Теперь ходит компьютер')
    import random
    step = random.randint(0, 100)
    print('Компьютер выбрал номер - ', step)
    valid_step(step, game_table, gamer='computer')
    print(*game_table, sep='\n')
    print('_'*75)
    return game_table


def valid_step(step, game_table, gamer):
    if step < 10:
        if game_table[0][step] in ('X', 'O'):
            print('Этот номер уже занят, попробуй другой')
            if gamer == 'computer':
                computer_step(game_table)
            else:
                human_step(game_table)
        else:
            if gamer == 'computer':
                game_table[0][step] = 'O'
            else:
                game_table[0][step] = 'X'
    else:
        coordinat_step = [int(x) for x in str(step)]
        if game_table[coordinat_step[0]][coordinat_step[1]] in ('X', 'O'):
            print('Этот номер уже занят, попробуй другой')
            if gamer == 'computer':
                computer_step(game_table)
            else:
                human_step(game_table)
        else:
            if gamer == 'computer':
                game_table[coordinat_step[0]][coordinat_step[1]] = 'O'
            else:
                game_table[coordinat_step[0]][coordinat_step[1]] = 'X'
    loss_check(game_table, step)
    return game_table


def start_game():
    list_game_numbers = [str(x) for x in range(100)]
    game_table = []
    i = 0
    for j in range(10):
        game_table.append(list_game_numbers[i:i + 10])
        i += 10
    print(*game_table, sep='\n')
    while True:
        game_table = human_step(game_table)

        game_table = computer_step(game_table)


start_game()
