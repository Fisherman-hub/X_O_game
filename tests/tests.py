def generation(step):
    horizontal = {i for i in range(step - 4, step + 5) if i // 10 == step // 10}
    return horizontal


def gen_vert(step):
    vertical = {i for i in range(step - 4 * 10, step + 5 * 10, 10) if 0 <= i < 100}
    return vertical


def gen_diagonal1(step):
    print('step - ', step)
    diagonal_tl_br = [i for i in range(step - 4 * 11, step + 5 * 11, 11) if 0 <= i < 100]
    print('diagonal create - ', diagonal_tl_br)
    if step % 10 == 0:
        start = diagonal_tl_br.index(step)
        diagonal_tl_br = diagonal_tl_br[start:]
        print('diagonal_correct - ', diagonal_tl_br)
    for i in diagonal_tl_br:
        if i % 10 == 9:
            stop = diagonal_tl_br.index(i)
            diagonal_tl_br = diagonal_tl_br[:stop + 1]
    if len(diagonal_tl_br) < 5:
        diagonal_tl_br = set()
        print('Длина меньше 5 элементов', diagonal_tl_br)
        return diagonal_tl_br
    print('step number - ', step)
    print('diagonal_tl_br - ', diagonal_tl_br)
    print('_' * 60)
    return set(diagonal_tl_br)


def gen_diagonal2(step):
    print('_' * 80)
    diagonal_rt_bl = [i for i in range(step - 4 * 9, step + 5 * 9, 9) if 0 <= i < 100]
    print('step - ', step)
    print('Диагональ создана', diagonal_rt_bl)
    print('_' * 80)
    start = 0
    for i in diagonal_rt_bl:
        if i % 10 == 9:
            start = diagonal_rt_bl.index(i)
        elif i % 10 == 0 and start < diagonal_rt_bl.index(i):
            stop = diagonal_rt_bl.index(i)
            diagonal_rt_bl = diagonal_rt_bl[:stop + 1]
            break
    diagonal_rt_bl = diagonal_rt_bl[start:]
    print('Диагональ после цикла - ', diagonal_rt_bl)
    if len(diagonal_rt_bl) < 5:
        return set()

    return set(diagonal_rt_bl)


'''['0',  '1',  '2',  '3',  '4',  '5',  '6',  '7',  '8',  '9']
   ['10', '11', '12', '13', '14', '15', '16', '17', '18', '19']
   ['20', '21', '22', '23', '24', '25', '26', '27', '28', '29']
   ['30', '31', '32', '33', '34', '35', '36', '37', '38', '39']
   ['40', '41', '42', '43', '44', '45', '46', '47', '48', '49']
   ['50', '51', '52', '53', '54', '55', '56', '57', '58', '59']
   ['60', '61', '62', '63', '64', '65', '66', '67', '68', '69']
   ['70', '71', '72', '73', '74', '75', '76', '77', '78', '79']
   ['80', '81', '82', '83', '84', '85', '86', '87', '88', '89']
   ['90', '91', '92', '93', '94', '95', '96', '97', '98', '99']'''

assert gen_diagonal2(55) == {55, 46, 37, 28, 19, 64, 73, 82, 91}
assert gen_diagonal2(99) == set()
assert gen_diagonal2(70) == {70, 61, 52, 43, 34}

assert gen_diagonal1(27) == {27, 16, 5, 38, 49}
assert gen_diagonal1(99) == {99, 88, 77, 66, 55}
assert gen_diagonal1(55) == {11, 22, 33, 44, 55, 66, 77, 88, 99}
assert gen_diagonal1(2) == {2, 13, 24, 35, 46}
assert gen_diagonal1(40) == {40, 51, 62, 73, 84}
assert gen_diagonal1(90) == set()

assert gen_diagonal1(0) == {0, 11, 22, 33, 44}
assert gen_diagonal1(99) == {99, 88, 77, 66, 55}
assert gen_diagonal1(55) == {11, 22, 33, 44, 55, 88, 77, 66, 99}

print(gen_diagonal2(66))
assert gen_diagonal2(66) == {75, 84, 93, 57, 48, 39, 66}

assert gen_vert(0) == {0, 10, 20, 30, 40}
assert gen_vert(55) == {15, 25, 35, 45, 55, 65, 75, 85, 95}
assert gen_vert(99) == {99, 89, 79, 69, 59}

assert generation(50) == {50, 51, 52, 53, 54}
assert generation(72) == {70, 71, 72, 73, 74, 75, 76}
assert generation(99) == {99, 98, 97, 96, 95}
assert generation(0) == {0, 1, 2, 3, 4}
