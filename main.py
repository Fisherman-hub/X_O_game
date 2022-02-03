


def make_table():
    pass

def update_table():
    pass


def human_step(game_table):
    while True:
        step_number = input('Введи номер элемента - ', )
        try:
            if int(step_number) < 10:
                game_table[0][int(a)] = 'X'
            elif int(step_number) > 99:
                print('Введите число от 0 до 99')
            else:
                step_number = tuple(step_number)
                print(step_number)
                game_table[int(step_number[0])][int(step_number[1])] = 'X'
        except ValueError:
            print('А где же число?')
            continue
        print(*game_table, sep='\n')
        computer_step(game_table)


def computer_step(game_table):
    print('Теперь ходит компьютер')
    import random
    step = random.randint(0, 100)
    print('Компьютер выбрал номер - ', step)
    if step < 10:
        if game_table[0][step] == 'X':
            computer_step(game_table)
        else:
            game_table[0][step] = 'O'
    else:
        coordinat_step = [int(x) for x in str(step)]

        if game_table[coordinat_step[0]][coordinat_step[1]] == 'X':
            computer_step(game_table)
        else:
            game_table[coordinat_step[0]][coordinat_step[1]] = 'O'
    print(*game_table, sep='\n')
    human_step(game_table)


def start_game():
    list_game_numbers = [str(x) for x in range(100)]
    game_table = []
    i = 0
    for j in range(10):
        game_table.append(list_game_numbers[i:i + 10])
        i += 10
    print(*game_table, sep='\n')
    human_step(game_table)


start_game()


# list_game_numbers = [str(x) for x in range(100)]
# game_table = []
# i = 0
# for j in range(10):
#     game_table.append(list_game_numbers[i:i+10])
#     i += 10
#
# print(*game_table, sep='\n')
#
# while True:
#
#     '''Разбить чило на элементы, использоваить int(input()) '''
#
#
#     a = input('Введи номер элемента - ', )
#
#     print (a)
#     try:
#         if int(a)<10:
#             game_table[0][int(a)] ='X'
#         elif int(a)>99:
#             print('Введите число от 0 до 99')
#         else:
#             a = tuple(a)
#             print(a)
#             game_table[int(a[0])][int(a[1])] = 'X'
#     except ValueError:
#         print('А где же число?')
#         continue
#
#     print(*game_table, sep='\n')


# if __name__ == "__main__":
#
