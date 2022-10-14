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
    take a static array and return a new one omitting duplicates
    """
    size = arr.size()
    # create a temporary array that will hold the non-duplicates
    new_arr = StaticArray(size)
    pos = 1
    new_arr.set(0, arr.get(0))
    for i in range(1, size):
        if arr.get(i) != arr.get(i-1):
            new_arr.set(pos, arr.get(i))
            pos += 1
    # final array that will be the correct size
    final_arr = StaticArray(pos)
    for i in range(pos):
        final_arr.set(i, new_arr.get(i))
    return final_arr


# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------


def count_sort(arr: StaticArray) -> StaticArray:
    """
    count sort
    """

    min, max = min_max(arr)
    domain = max - min
    size = arr.size()

    # create count array to keep track of amount of each value
    count = StaticArray(domain+1)
    for i in range(domain+1):
        count.set(i, 0)

    for i in range(size):
        val = arr.get(i)
        pos = val-min
        count.set(pos, count.get(pos)+1)

    for i in range(1, domain+1):
        prev = count.get(i-1)
        cur = count.get(i)
        count.set(i, prev + cur)

    # out array to put sorted values in
    out = StaticArray(size)

    for i in range(size):
        val = arr.get(i)
        pos = val-min
        count.set(pos, count.get(pos)-1)
        ind = size - count.get(pos) - 1
        out.set(ind, val)

    return out




# ------------------- PROBLEM 10 - SA_INTERSECTION --------------------------


def sa_intersection(arr1: StaticArray, arr2: StaticArray, arr3: StaticArray) \
        -> StaticArray:
    """
    take 3 arrays and return a new array consisting only of values
    found in all 3
    """
    # get sizes of the 3 arrays
    size1 = arr1.size()
    size2 = arr2.size()
    size3 = arr3.size()

    # get minimum array size to initialize temp array
    min = size1
    if size2 < min:
        min = size2
    if size3 < min:
        min = size3

    temp = StaticArray(min)
    count = 0

    i1 = 0
    i2 = 0
    i3 = 0

    while True:
        v1 = arr1[i1]
        v2 = arr2[i2]
        v3 = arr3[i3]
        if arr1[i1] == arr2[i2] == arr3[i3]:
            #print("found match at " + i1 + " " + i2 + " " + i3)
            temp[count] = arr1[i1]
            count += 1
            i1 += 1
            i2 += 1
            i3 += 1
            if i1 >= size1 or i2 >= size2 or i3 >= size3:
                break
        elif arr1[i1] < arr2[i2] or arr1[i1] < arr3[i3]:
            #print("increment i1")
            i1 += 1
            if i1 >= size1:
                break
        elif arr2[i2] < arr1[i1] or arr2[i2] < arr3[i3]:
            #print("increment i2")
            i2 += 1
            if i2 >= size2:
                break
        elif arr3[i3] < arr1[i1] or arr3[i3] < arr2[i2]:
            #print("increment i3")
            i3 += 1
            if i3 >= size3:
                break
    if count == 0:
        return StaticArray(1)

    final = StaticArray(count)
    for i in range(count):
        final[i] = temp[i]
    return final



# ------------------- PROBLEM 11 - SORTED SQUARES ---------------------------


def sorted_squares(arr: StaticArray) -> StaticArray:
    """
    take an array as input and return a new array of the squares of the original
    """
    size = arr.size()
    output = StaticArray(size)
    # if all values in original array are positive, just put the squares in a new
    # array and return it. If all values are negative, do the same but reverse
    # the new array before returning
    if arr[0] >= 0 or arr[size-1] <= 0:
        for i in range(size):
            output[i] = arr[i] ** 2
        if arr[size-1] <= 0:
            reverse(output)
    # if both positive and negative values are present,
    # create two separate arrays, reverse the negatives,
    # then merge into final output
    else:
        negs = 0
        pos = 0
        temp_negative = StaticArray(size)
        temp_positive = StaticArray(size)
        for i in range(size):
            if arr[i] < 0:
                negs += 1
                temp_negative[i] = arr[i] ** 2
            else:
                temp_positive[pos] = arr[i] ** 2
                pos += 1

        negative = StaticArray(negs)
        for i in range(negs):
            negative[i] = temp_negative[i]
        reverse(negative)
        positive = StaticArray(pos)
        for i in range(pos):
            positive[i] = temp_positive[i]

        pi = 0
        ni = 0
        oi = 0

        # while there are still values in both lists
        # compare the two current values and put lowest
        # in output list
        while pi < positive.size() and ni < negative.size():
            if positive[pi] < negative[ni]:
                output[oi] = positive[pi]
                oi += 1
                pi += 1
            else:
                output[oi] = negative[ni]
                oi += 1
                ni += 1
        # if end of negative list is reached first,
        # add the rest of the positive values to output
        while pi < positive.size():
            output[oi] = positive[pi]
            oi += 1
            pi += 1

        # if end of positive list is reached first, add
        # the rest of the negative values to output
        while ni < negative.size():
            output[oi] = negative[ni]
            oi += 1
            ni += 1

    return output






# ------------------- PROBLEM 12 - ADD_NUMBERS ------------------------------


def add_numbers(arr1: StaticArray, arr2: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """



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


    # print('\n# sa_sort example 1')
    # test_cases = (
    #     [1, 10, 2, 20, 3, 30, 4, 40, 5],
    #     ['zebra2', 'apple', 'tomato', 'apple', 'zebra1'],
    #     [(1, 1), (20, 1), (1, 20), (2, 20)],
    #     [random.randrange(-30000, 30000) for _ in range(5_000)]
    # )
    # for case in test_cases:
    #     arr = StaticArray(len(case))
    #     for i, value in enumerate(case):
    #         arr[i] = value
    #     print(arr if len(case) < 50 else 'Started sorting large array')
    #     sa_sort(arr)
    #     print(arr if len(case) < 50 else 'Finished sorting large array')



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


    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
        [random.randrange(-10_000, 10_000) for _ in range(1_000_000)]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr if len(case) < 50 else 'Started sorting large array')
        result = sorted_squares(arr)
        print(result if len(case) < 50 else 'Finished sorting large array')

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
