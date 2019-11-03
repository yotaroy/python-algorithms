def quick_sort(arr, left, right):
    if right - left <= 1:
        return

    mid_index = (left + right) // 2     # 基準となるindex
    mid = arr[mid_index]        # 基準値

    arr[mid_index], arr[right-1] = arr[right-1], arr[mid_index]

    i = left        # 基準値以上の値の左端
    for j in range(left, right-1):
        if arr[j] < mid:        # 基準値より小さい値の場合左に
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right-1] = arr[right-1], arr[i] # 基準値を分け目に戻す

    quick_sort(arr, left, i)    # 基準よりも左を再帰的にソート
    quick_sort(arr, i+1, right)     # 基準よりも右を再帰的にソート


if __name__ == '__main__':
    import random

    print('quick sort')
    x = list(range(1, 31))
    random.shuffle(x)
    print(x)
    quick_sort(x, 0, len(x))
    print(x)

