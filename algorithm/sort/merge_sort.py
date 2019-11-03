def merge_sort(arr, left, right):
    if right - left == 1:
        return [arr[left]]

    mid = (right + left) // 2

    x = merge_sort(arr, left, mid)
    x.append(float('inf'))
    y = merge_sort(arr, mid, right)
    y.append(float('inf'))

    output = list()

    i = 0
    j = 0
    while i + j < len(x) + len(y) - 2:
        if x[i] > y[j]:
            output.append(y[j])
            j += 1
        else:
            output.append(x[i])
            i += 1

    return output


if __name__ == '__main__':
    import random

    print('merge sort')
    x = list(range(1, 31))
    random.shuffle(x)
    print(x)
    print(merge_sort(x, 0, len(x)))

