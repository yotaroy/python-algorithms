"""
挿入ソートの改良版．間隔を変えて挿入ソートを行う
増分列(gap sequence) hをつかう
ここでは，h_i+1 = h_i とする
"""


def shell_sort(arr):
    n = len(arr)
    h = []
    x = 1
    while x < n:
        h.append(x)
        x = 3 * x + 1
    m = len(h) - 1
    while m >= 0:
        for i in range(h[m], n):
            j = i
            while j > 0 and arr[j-h[m]] > arr[j]:
                arr[j-h[m]], arr[j] = arr[j], arr[j-h[m]]
                j -= h[m]
        m -= 1

    return arr


if __name__ == '__main__':
    import random

    print('insertion sort')
    x = list(range(1, 31))
    random.shuffle(x)
    print(x)
    print(shell_sort(x))
