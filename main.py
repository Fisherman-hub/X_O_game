import sys

computer_steps = set()
human_steps = set()

CROSS = f'\033[31mX\033[37m'
ZERO = f'\033[34mO\033[37m'

def loss_check(step, gamer):

    def gen_horizontal(step):
        """Функция получает проигрышную горизонтальную комбинацию в зависимости от номера шага."""

        horizontal = {i for i in range(step - 4, step + 5) if i // 10 == step // 10}
        return horizontal

    def gen_vert(step):
        """Функция получает проигрышную вертикальную комбинацию в зависимости от номера шага."""
        vertical = {i for i in range(step - 4 * 10, step + 5 * 10, 10) if 0 <= i < 100}
        return vertical

    def gen_diagonal1(step):
        """Функция получает проигрышную диагональную комбинацию (от верхнего левого угла к правому
        нижнему в зависимости от номера шага."""
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
        """Функция получает проигрышную диагональную комбинацию (от верхнего правого угла к левому
               нижнему в зависимости от номера шага."""
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
        if len(steps & line) == 5:
            print('Игра закончена. Проиграл - ', looser)
            sys.exit()

    moves = {'computer': computer_steps, 'human': human_steps}

    if gamer == 'computer':
        computer_steps.add(step)
        for combination in (gen_vert(step), gen_horizontal(step), gen_diagonal1(step), gen_diagonal2(step)):
            game_over(moves[gamer], combination, gamer)

    else:
        human_steps.add(step)
        for combination in (gen_vert(step), gen_horizontal(step), gen_diagonal1(step), gen_diagonal2(step)):
            game_over(moves[gamer], combination, gamer)

def human_step(game_table):
    try:
        step = int(input('Введи номер элемента - ', ))
        if step not in range(0, 100):
            raise ValueError
    except ValueError:
        print('Введите число от 0 до 99')
        human_step(game_table)

    valid_step(step, game_table, gamer='human')
    print('_' * 75)
    return game_table


def computer_step(game_table):
    print('Теперь ходит компьютер')
    import random
    step = random.randint(0, 100)
    print('Компьютер выбрал номер - ', step)
    valid_step(step, game_table, gamer='computer')
    print('_' * 75)
    return game_table


def valid_step(step, game_table, gamer):
    if step < 10:
        if game_table[0][step] in (CROSS, ZERO):
            print('Этот номер уже занят, попробуй другой')
            if gamer == 'computer':
                computer_step(game_table)
            else:
                human_step(game_table)
        else:
            if gamer == 'computer':
                game_table[0][step] = ZERO
            else:
                game_table[0][step] = CROSS
    else:
        coordinat_step = [int(x) for x in str(step)]
        if game_table[coordinat_step[0]][coordinat_step[1]] in (f'{CROSS} ', f'{ZERO} '):
            print('Этот номер уже занят, попробуй другой')
            if gamer == 'computer':
                computer_step(game_table)
            else:
                human_step(game_table)
        else:
            if gamer == 'computer':
                # f'{} присваивается переменной, чтобы таблица не плыла при игре
                game_table[coordinat_step[0]][coordinat_step[1]] = f'{ZERO} '
            else:
                game_table[coordinat_step[0]][coordinat_step[1]] = f'{CROSS} '
    loss_check(step, gamer)
    return game_table


def draw_table(game_table):
    for number_line in range(len(game_table)):
        if number_line == 0:
            print('\033[37m_' * 50)
            print(*game_table[number_line], sep='  | ', end='  |\n')
            print("\033[37m"'_'*50)
        else:
            print(*game_table[number_line], sep=' | ', end=' |\n')
            print('\033[37m_' * 50)


def start_game():
    print(
'''Добро пожаловать в игру обратные крестики-нолики!
Здесь тебе предстоить как можно дольше продержаться не 
собрав 5 в ряд по ветикали, горизонтали, диагонали.
Играть предстоит против компьютера. Желаю тебе удачи''', end='\n'*3)
    list_game_numbers = [str(x) for x in range(100)]
    game_table = []
    i = 0
    for j in range(10):
        game_table.append(list_game_numbers[i:i + 10])
        i += 10
    while True:
        draw_table(game_table)
        game_table = human_step(game_table)
        game_table = computer_step(game_table)


start_game()
