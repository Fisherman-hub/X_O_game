

def make_table():
    list_game_numbers = [str(x) for x in range(100)]
    game_table = []
    i = 0
    for j in range(10):
        game_table.append(list_game_numbers[i:i + 10])
        i += 10
    return game_table

def update_table():
    pass

def human_step(make_table):
    while True:
        a = input('Введи номер элемента - ', )
        print(a)
        try:
            if int(a) < 10:
                game_table[0][int(a)] = 'X'
            elif int(a) > 99:
                print('Введите число от 0 до 99')
            else:
                a = tuple(a)
                print(a)
                game_table[int(a[0])][int(a[1])] = 'X'
        except ValueError:
            print('А где же число?')
            continue


def computer_step(update_table):
    import random
    step = random.randint(0, 100)
    if step<10:
        update_table[0][step] = 'O'
    else:
        coordinat_step = [int(x) for x in step]
        update_table[coordinat_step[0]][coordinat_step[1]] = 'O'

    return update_table


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


if __name__ == "__main__":
	print(*make_table(), sep='\n')
