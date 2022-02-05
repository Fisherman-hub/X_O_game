Computer_steps = []
Human_steps = []


def loss_check(step, gamer):

    if gamer == 'computer':
        Computer_steps.append(step)
        print('Функция loss_check computer', Computer_steps)
    else:
        Human_steps.append(step)
        sorted(Human_steps)
        print('Функция loss_check human', Human_steps)
        print('Длина human_step - ', len(Human_steps))
        count = 1
        if len(Human_steps) > 4:
            print ('Зашел в проверку на победу')
            for i in range(len(Human_steps)-1):
                print('Зашел в цикл')
                print('count - ', count)
                if Human_steps[i+1]-Human_steps[i] == 1:
                    print('Зашел в if')
                    count += 1
                else:
                    print('Зашел в else')
                    count = 0
            if count == 5:
                print('Человечишко ты проиграл')








    '''Реализация в зависимости от положения. Можем, ли мы двигаться вверх, вниз,
    подиагонали вверх, подиагонали вниз'''
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
    x_step = ''
    y_step = ''
    if step < 10:
        if game_table[0][step] in ('X', 'O'):
            print('Этот номер уже занят, попробуй другой')
            if gamer == 'computer':
                computer_step(game_table)
            else:
                human_step(game_table)
        else:
            x_step = 0
            y_step = step
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
            x_step = coordinat_step[0]
            y_step = coordinat_step[1]
            if gamer == 'computer':
                game_table[coordinat_step[0]][coordinat_step[1]] = 'O'
            else:
                game_table[coordinat_step[0]][coordinat_step[1]] = 'X'
    loss_check(step, gamer)
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


