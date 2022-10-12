# Course: CS261 - Data Structures
# Student Name:
# Assignment:
# Description:

import random
import string
from a1_include import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------


def min_max(arr: StaticArray) -> ():
    """
    take a static array and return the minimum and maximum values
    """
    min = arr.get(0)
    max = arr.get(0)
    # iterate the array, checking each value against current min/max
    for i in range(arr.size()):
        if arr.get(i) > max:
            max = arr.get(i)
        if arr.get(i) < min:
            min = arr.get(i)
    return min, max


# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------


def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
    make a new array that copies the original but replaces
    numbers divisible by both 3 and 5 with "fizzbuzz", replaces
    numbers divisible by 3 with "fizz", and numbers divisible
    by 5 with "buzz"
    """
    new_array = StaticArray(arr.size())
    for i in range(arr.size()):
        if arr.get(i) % 3 == 0 and arr.get(i) % 5 == 0:
            new_array.set(i, "fizzbuzz")
        elif arr.get(i) % 3 == 0:
            new_array.set(i, "fizz")
        elif arr.get(i) % 5 == 0:
            new_array.set(i, "buzz")
        else:
            new_array.set(i, arr.get(i))
    return new_array




# ------------------- PROBLEM 3 - REVERSE -----------------------------------


def reverse(arr: StaticArray) -> None:
    """
    reverse the order of the array in place
    """
    size = arr.size()
    for i in range(size//2):
        temp = arr.get(i)
        arr.set(i, arr.get(size-(i+1)))
        arr.set(size-(i+1), temp)


# ------------------- PROBLEM 4 - ROTATE ------------------------------------


def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    take a static array and return a new static array rotated by the
    specified number of steps
    """
    size = arr.size()
    new_arr = StaticArray(size)
    for i in range(size):
        val = arr.get(i)
        pos = i + steps
        # if the position on the new array is outside the range, adjust it
        while pos < 0:
            pos += size
        if pos >= size:
            pos = pos % size
        new_arr.set(pos, val)
    return new_arr




# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------


def sa_range(start: int, end: int) -> StaticArray:
    """
    takes a starting and ending integer and returns a static array counting
    from start to end
    """
    size = abs(end - start) + 1
    arr = StaticArray(size)
    pos = 0
    if end < start:
        end -= 1
        step = -1
    else:
        end += 1
        step = 1
    for i in range(start, end, step):
        arr.set(pos, i)
        pos += 1
    return arr


# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------


def is_sorted(arr: StaticArray) -> int:
    """
    return 1 if arr is strictly ascending, 2 if strictly descending, 0 otherwise
    """
    # per instructions, if there is only one item in the list, treat it
    # as strictly ascending
    if arr.size() == 1:
        return 1

    ascending = True
    descending = True

    # iterate the list, checking consecutive values for ascending or descending
    for i in range(arr.size()-2):
        if arr.get(i) <= arr.get(i+1):
            descending = False
        if arr.get(i) >= arr.get(i+1):
            ascending = False

    if ascending:
        return 1
    elif descending:
        return 2
    else:
        return 0


# ------------------- PROBLEM 7 - SA_SORT -----------------------------------


def sa_sort(arr: StaticArray) -> None:
    """
    use an insertion sort to sort the static array
    """
    for i in range(1, arr.size()):
        val = arr.get(i)
        pos = i - 1

        while pos >= 0 and val < arr.get(pos):
            arr.set(pos+1, arr.get(pos))
            pos -= 1
        arr.set(pos+1, val)




# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------


def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """
    pass


# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------


def count_sort(arr: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """
    pass


# ------------------- PROBLEM 10 - SA_INTERSECTION --------------------------


def sa_intersection(arr1: StaticArray, arr2: StaticArray, arr3: StaticArray) \
        -> StaticArray:
    """
    TODO: Write this implementation
    """
    pass


# ------------------- PROBLEM 11 - SORTED SQUARES ---------------------------


def sorted_squares(arr: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """
    pass


# ------------------- PROBLEM 12 - ADD_NUMBERS ------------------------------


def add_numbers(arr1: StaticArray, arr2: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """
    pass


# ------------------- PROBLEM 13 - BALANCED_STRINGS -------------------------


def balanced_strings(s: str) -> StaticArray:
    """
    TODO: Write this implementation
    """
    pass


# ------------------- PROBLEM 14 - TRANSFORM_STRING -------------------------


def transform_string(source: str, s1: str, s2: str) -> str:
    """
    TODO: Write this implementation
    """
    pass







# BASIC TESTING
if __name__ == "__main__":

    # print('\n# min_max example 1')
    # arr = StaticArray(5)
    # for i, value in enumerate([7, 8, 6, -5, 4]):
    #     arr[i] = value
    # print(min_max(arr))
    #
    #
    # print('\n# min_max example 2')
    # arr = StaticArray(1)
    # arr[0] = 100
    # print(min_max(arr))
    #
    #
    # print('\n# min_max example 3')
    # arr = StaticArray(3)
    # for i, value in enumerate([3, 3, 3]):
    #     arr[i] = value
    # print(min_max(arr))

    #
    # print('\n# fizz_buzz example 1')
    # source = [_ for _ in range(-5, 20, 4)]
    # arr = StaticArray(len(source))
    # for i, value in enumerate(source):
    #     arr[i] = value
    # print(fizz_buzz(arr))
    # print(arr)


    # print('\n# reverse example 1')
    # source = [_ for _ in range(-20, 20, 7)]
    # arr = StaticArray(len(source))
    # for i, value in enumerate(source):
    #     arr.set(i, value)
    # print(arr)
    # reverse(arr)
    # print(arr)
    # reverse(arr)
    # print(arr)
    #
    # print('\n# reverse example 2')
    # source = [_ for _ in range(-20, 20, 6)]
    # arr = StaticArray(len(source))
    # for i, value in enumerate(source):
    #     arr.set(i, value)
    # print(arr)
    # reverse(arr)
    # print(arr)
    # reverse(arr)
    # print(arr)


    # print('\n# rotate example 1')
    # source = [_ for _ in range(-20, 20, 7)]
    # arr = StaticArray(len(source))
    # for i, value in enumerate(source):
    #     arr.set(i, value)
    # print(arr)
    # for steps in [1, 2, 0, -1, -2, 28, -100]:
    #     print(rotate(arr, steps), steps)
    # print(arr)


    # print('\n# sa_range example 1')
    # cases = [
    #     (1, 3), (-1, 2), (0, 0), (0, -3),
    #     (-105, -99), (-99, -105)]
    # for start, end in cases:
    #     print(start, end, sa_range(start, end))


    # print('\n# is_sorted example 1')
    # test_cases = (
    #     [-100, -8, 0, 2, 3, 10, 20, 100],
    #     ['A', 'B', 'Z', 'a', 'z'],
    #     ['Z', 'T', 'K', 'A', '5'],
    #     [1, 3, -10, 20, -30, 0],
    #     [-10, 0, 0, 10, 20, 30],
    #     [100, 90, 0, -90, -200],
    #     ['apple']
    # )
    # for case in test_cases:
    #     arr = StaticArray(len(case))
    #     for i, value in enumerate(case):
    #         arr[i] = value
    #     print('Result:', is_sorted(arr), arr)


    print('\n# sa_sort example 1')
    test_cases = (
        [1, 10, 2, 20, 3, 30, 4, 40, 5],
        ['zebra2', 'apple', 'tomato', 'apple', 'zebra1'],
        [(1, 1), (20, 1), (1, 20), (2, 20)],
        [random.randrange(-30000, 30000) for _ in range(5_000)]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr if len(case) < 50 else 'Started sorting large array')
        sa_sort(arr)
        print(arr if len(case) < 50 else 'Finished sorting large array')

    #
    #
    # print('\n# remove_duplicates example 1')
    # test_cases = (
    #     [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
    #     [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    # )
    # for case in test_cases:
    #     arr = StaticArray(len(case))
    #     for i, value in enumerate(case):
    #         arr[i] = value
    #     print(arr)
    #     print(remove_duplicates(arr))
    # print(arr)
    #
    #
    # print('\n# count_sort example 1')
    # test_cases = (
    #     [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
    #     [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
    #     [random.randrange(-499, 499) for _ in range(1_000_000)]
    # )
    # for case in test_cases:
    #     arr = StaticArray(len(case))
    #     for i, value in enumerate(case):
    #         arr[i] = value
    #     print(arr if len(case) < 50 else 'Started sorting large array')
    #     result = count_sort(arr)
    #     print(result if len(case) < 50 else 'Finished sorting large array')
    #
    #
    # print('\n# sa_intersection example 1')
    # test_cases = (
    #     ([1, 2, 3], [3, 4, 5], [2, 3, 4]),
    #     ([1, 2], [2, 4], [3, 4]),
    #     ([1, 1, 2, 2, 5, 75], [1, 2, 2, 12, 75, 90], [-5, 2, 2, 2, 20, 75, 95])
    # )
    # for case in test_cases:
    #     arr = []
    #     for i, lst in enumerate(case):
    #         arr.append(StaticArray(len(lst)))
    #         for j, value in enumerate(sorted(lst)):
    #             arr[i][j] = value
    #     print(sa_intersection(arr[0], arr[1], arr[2]))
    #
    #
    # print('\n# sorted_squares example 1')
    # test_cases = (
    #     [1, 2, 3, 4, 5],
    #     [-5, -4, -3, -2, -1, 0],
    #     [-3, -2, -2, 0, 1, 2, 3],
    #     [random.randrange(-10_000, 10_000) for _ in range(1_000_000)]
    # )
    # for case in test_cases:
    #     arr = StaticArray(len(case))
    #     for i, value in enumerate(sorted(case)):
    #         arr[i] = value
    #     print(arr if len(case) < 50 else 'Started sorting large array')
    #     result = sorted_squares(arr)
    #     print(result if len(case) < 50 else 'Finished sorting large array')
    #
    #
    # print('\n# add_numbers example 1')
    # test_cases = (
    #     ([1, 2, 3], [4, 5, 6]),
    #     ([0], [2, 5]),
    #     ([2, 0, 9, 0, 7], [1, 0, 8]),
    #     ([9, 9, 9], [9, 9, 9, 9])
    # )
    # for num1, num2 in test_cases:
    #     n1 = StaticArray(len(num1))
    #     n2 = StaticArray(len(num2))
    #     for i, value in enumerate(num1):
    #         n1[i] = value
    #     for i, value in enumerate(num2):
    #         n2[i] = value
    #     print('Original nums:', n1, n2)
    #     print('Sum: ', add_numbers(n1, n2))
    #
    #
    # print('\n# balanced_strings example 1')
    # test_cases = (
    #     'aaabbbccc', 'abcabcabc', 'babcCACBCaaB', 'aBcCbA', 'aBc',
    #     'aBcaCbbAcbCacAbcBa', 'aCBBCAbAAcCAcbCBBa', 'bACcACbbACBa',
    #     'CBACcbcabcAaABb'
    # )
    # for case in test_cases:
    #     print(balanced_strings(case))
    #
    #
    # print('\n# transform_strings example 1')
    # test_cases = ('eMKCPVkRI%~}+$GW9EOQNMI!_%{#ED}#=-~WJbFNWSQqDO-..@}',
    #               'dGAqJLcNC0YFJQEB5JJKETQ0QOODKF8EYX7BGdzAACmrSL0PVKC',
    #               'aLiAnVhSV9}_+QOD3YSIYPR4MCKYUF9QUV9TVvNdFuGqVU4$/%D',
    #               'zmRJWfoKC5RDKVYO3PWMATC7BEIIVX9LJR7FKtDXxXLpFG7PESX',
    #               'hFKGVErCS$**!<OS<_/.>NR*)<<+IR!,=%?OAiPQJILzMI_#[+}',
    #               'EOQUQJLBQLDLAVQSWERAGGAOKUUKOPUWLQSKJNECCPRRXGAUABN',
    #               'WGBKTQSGVHHHHHTZZZZZMQKBLC66666NNR11111OKUN2KTGYUIB',
    #               'YFOWAOYLWGQHJQXZAUPZPNUCEJABRR6MYR1JASNOTF22MAAGTVA',
    #               'GNLXFPEPMYGHQQGZGEPZXGJVEYE666UKNE11111WGNW2NVLCIOK',
    #               'VTABNCKEFTJHXATZTYGZVLXLAB6JVGRATY1GEY1PGCO2QFPRUAP',
    #               'UTCKYKGJBWMHPYGZZZZZWOKQTM66666GLA11111CPF222RUPCJT')
    # for case in test_cases:
    #     print(transform_string(case, '612HZ', '261TO'))
