import sys

Computer_steps = set()
Human_steps = set()


def loss_check(step, gamer):
    def gen_horizontal(step):
        horizontal = {i for i in range(step - 4, step + 5) if i // 10 == step // 10}
        return horizontal

    def gen_vert(step):
        vertical = {i for i in range(step - 4 * 10, step + 5 * 10, 10) if 0 <= i < 100}
        return vertical

    def gen_diagonal1(step):
        diagonal_tl_br = [i for i in range(step - 4 * 11, step + 5 * 11, 11) if 0 <= i < 100]
        if step % 10 == 0:
            start = diagonal_tl_br.index(step)
            diagonal_tl_br = diagonal_tl_br[start:]
        for i in diagonal_tl_br:
            if i % 10 == 9:
                stop = diagonal_tl_br.index(i)
                diagonal_tl_br = diagonal_tl_br[:stop + 1]
        if len(diagonal_tl_br) < 5:
            diagonal_tl_br = set()
            return diagonal_tl_br
        return set(diagonal_tl_br)

    def gen_diagonal2(step):
        diagonal_rt_bl = [i for i in range(step - 4 * 9, step + 5 * 9, 9) if 0 <= i < 100]
        start = 0
        for i in diagonal_rt_bl:
            if i % 10 == 9:
                start = diagonal_rt_bl.index(i)
            elif i % 10 == 0 and start < diagonal_rt_bl.index(i):
                stop = diagonal_rt_bl.index(i)
                diagonal_rt_bl = diagonal_rt_bl[:stop + 1]
                break
        diagonal_rt_bl = diagonal_rt_bl[start:]
        if len(diagonal_rt_bl) < 5:
            return set()

        return set(diagonal_rt_bl)

    def game_over(steps, line, looser):
        # print(looser, ' steps - ', steps)
        # print('Looser line - ', line)
        # print(steps & line)
        if len(steps & line) == 5:
            print('Game over ', looser)
            sys.exit()

    if gamer == 'computer':
        Computer_steps.add(step)

        horizontel = gen_horizontal(step)
        vertical = gen_vert(step)
        diagonal1 = gen_diagonal1(step)
        diagonal2 = gen_diagonal2(step)

        # print(horizontel, vertical, diagonal2, diagonal1)

        game_over(Computer_steps, horizontel, gamer)
        game_over(Computer_steps, vertical, gamer)
        game_over(Computer_steps, diagonal2, gamer)
        game_over(Computer_steps, diagonal1, gamer)

        # print('Функция loss_check computer', Computer_steps)
    else:
        Human_steps.add(step)
        horizontel = gen_horizontal(step)
        vertical = gen_vert(step)
        diagonal1 = gen_diagonal1(step)
        diagonal2 = gen_diagonal2(step)
        # print(horizontel, vertical, diagonal2, diagonal1)

        game_over(Human_steps, horizontel, gamer)
        game_over(Human_steps, vertical, gamer)
        game_over(Human_steps, diagonal2, gamer)
        game_over(Human_steps, diagonal1, gamer)


def human_step(game_table):
    try:
        step = int(input('Введи номер элемента - ', ))
        if step not in range(0, 100):
            raise ValueError
    except ValueError:
        print('Введите число от 0 до 99')
        human_step(game_table)

    valid_step(step, game_table, gamer='human')
    # print(*game_table, sep='\n')
    print('_' * 75)
    return game_table


def computer_step(game_table):
    print('Теперь ходит компьютер')
    import random
    step = random.randint(0, 100)
    print('Компьютер выбрал номер - ', step)
    valid_step(step, game_table, gamer='computer')
    # print(*game_table, sep='\n')
    print('_' * 75)
    return game_table


def valid_step(step, game_table, gamer):
    # x_step = ''
    # y_step = ''
    if step < 10:
        if game_table[0][step] in ('X', 'O'):
            print('Этот номер уже занят, попробуй другой')
            if gamer == 'computer':
                computer_step(game_table)
            else:
                human_step(game_table)
        else:
            # x_step = 0
            # y_step = step
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
            # x_step = coordinat_step[0]
            # y_step = coordinat_step[1]
            if gamer == 'computer':
                game_table[coordinat_step[0]][coordinat_step[1]] = 'O '
            else:
                game_table[coordinat_step[0]][coordinat_step[1]] = 'X '
    loss_check(step, gamer)
    return game_table


def draw_table(game_table):
    for number_line in range(len(game_table)):
        if number_line == 0:
            print(*game_table[number_line], sep='  | ', end='  |\n')
        else:
            print(*game_table[number_line], sep=' | ', end=' |\n')


def start_game():
    list_game_numbers = [str(x) for x in range(100)]
    game_table = []
    i = 0
    for j in range(10):
        game_table.append(list_game_numbers[i:i + 10])
        i += 10
    # print(*game_table, sep='\n')
    while True:
        draw_table(game_table)
        game_table = human_step(game_table)
        game_table = computer_step(game_table)


start_game()
