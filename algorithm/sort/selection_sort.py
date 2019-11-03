"""
iからnまでの数字の最小値を繰り返し選んでいくことでソートをする
"""


def selection_sort(arr):
    n = len(arr)

    for i in range(n-1):
        minimum = arr[i]
        min_index = i
        for j in range(i+1, n):
            if arr[j] < minimum:
                minimum = arr[j]
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


if __name__ == '__main__':
    import random

    print('insertion sort')
    x = list(range(1, 31))
    random.shuffle(x)
    print(x)
    print(selection_sort(x))

