"""
配列の前の部分arr[0:i]がソートされている時に，arr[i]を適切な場所に挿入することでソートをする
"""


def insertion_sort(arr):
    n = len(arr)

    for i in range(n):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1

    return arr


if __name__ == '__main__':
    import random

    print('insertion sort')
    x = list(range(1, 31))
    random.shuffle(x)
    print(x)
    print(insertion_sort(x))

