from decimal import Decimal
from datetime import datetime


def compare_triplets(a_case, b_case):
    aVal = 0
    bVal = 0
    for i in range(len(a_case)):
        if a_case[i] > b_case[i]:
            aVal += 1
        elif a_case[i] < b_case[i]:
            bVal += 1
    res = [aVal, bVal]
    return res


def diagonal_difference(arr):
    left_bank = [arr[i][i] for i in range(0, len(arr[0]))]
    right_bank = [arr[i][(len(arr[0]) - 1) - i] for i in range(0, len(arr[0]))]
    return abs(sum(left_bank) - sum(right_bank))


def plus_minus(arr):
    s = len(arr)
    plus = 0
    minus = 0
    zero = 0
    for number in arr:
        if number < 0:
            minus += 1
        elif number == 0:
            zero += 1
        else:
            plus += 1
    ratio_plus = Decimal(plus)/Decimal(s)
    ratio_minus = minus/s
    ratio_zero = zero/s
    print(format(ratio_minus, '.6f'))
    print(format(ratio_zero, '.6f'))
    print(format(ratio_plus, '.6f'))


def staircase(n):
    stairway = []
    c = n
    d = 0
    for i in range(n):
        stairway.append(' ' * d + '#' * c)
        c -= 1
        d = n - c
    return stairway


def mini_max_sum(arr):
    minor = arr.copy()
    major = arr.copy()
    minor.remove(max(minor))
    major.remove(min(major))
    v_max = sum(major)
    v_min = sum(minor)
    print(f'{v_min} {v_max}')


def birthday_cake_candles(candles):
    # tallest = [x for x in candles if x == max(candles)]
    return candles.count(max(candles))


def time_conversion(s):
    if s[-2:] == "AM":
        if s[:2] == '12':
            n_time = str('00' + s[2:8])
        else:
            n_time = s[:-2]
    else:
        if s[:2] == '12':
            n_time = s[:-2]
        else:
            n_time = str(int(s[:2]) + 12) + s[2:8]
    return n_time


def cavity_map(grid):
    grid_size = len(grid)
    output = [[0] * grid_size for _ in range(grid_size)]

    for ind in range(grid_size):
        for jnd in range(grid_size):
            if (0 < ind < grid_size - 1 and 0 < jnd < grid_size - 1 and
                    grid[ind][jnd] > grid[ind + 1][jnd] and
                    grid[ind][jnd] > grid[ind - 1][jnd] and
                    grid[ind][jnd] > grid[ind][jnd + 1] and
                    grid[ind][jnd] > grid[ind][jnd - 1]):
                output[ind][jnd] = 'X'
            else:
                output[ind][jnd] = grid[ind][jnd]

    return ["".join(x) for x in output]


if __name__ == '__main__':
    grid = ['1112', '1912', '1892', '1234']
    n_grid = cavity_map(grid)
    print(n_grid)
