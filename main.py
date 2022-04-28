from decimal import Decimal


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


if __name__ == '__main__':
    arr = [1, 3, 5, 7, 9]
    mini_max_sum(arr)
