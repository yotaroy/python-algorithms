def bubble_sort(arr):
    n = len(arr)
    for j in range(1, n):
        sorted = True
        for i in range(n - j):
            if arr[i] > arr[i+1]:
                arr[i+1], arr[i] = arr[i], arr[i+1]
                sorted = False
        if sorted:
            break

    return arr


if __name__ == '__main__':
    import random

    print('insertion sort')
    x = list(range(1, 31))
    random.shuffle(x)
    print(x)
    print(bubble_sort(x))
