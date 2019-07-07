import random


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


class heap:
    def __init__(self):
        self.heap = list()

    def heap_push(self, x):     # heapに追加
        self.heap.append(x)

        i = len(self.heap) - 1
        while i > 0:
            if self.heap[i] <= self.heap[i//2]:
                break
            self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            i //= 2

    def heap_pop(self):     # heapから最大値を取り出し、heapを整える
        if len(self.heap) == 1:
            return self.heap.pop(0)
        elif len(self.heap) == 0:   # エラー
            print('heap has no data')
            return None

        output = self.heap[0]
        self.heap[0] = self.heap.pop(len(self.heap)-1)

        i = 0
        while 2*i < len(self.heap):
            if 2*i + 1 == len(self.heap):
                if self.heap[i] < self.heap[2*i]:
                    self.heap[i], self.heap[2*i] = self.heap[2*i], self.heap[i]
                break
            if self.heap[i] >= max(self.heap[2*i], self.heap[2*i+1]):
                break
            if self.heap[2*i] > self.heap[2*i+1]:
                self.heap[i], self.heap[2*i] = self.heap[2*i], self.heap[i]
                i = 2*i
            else:
                self.heap[i], self.heap[2*i+1] = self.heap[2*i+1], self.heap[i]
                i = 2*i+1

        return output

    def make_heap_from_array(self, arr):
        for a in arr:
            self.heap_push(a)


def merge_sort(arr, left, right):
    if right - left == 1:
        return [arr[left]]

    mid = (right + left) // 2

    x = merge_sort(arr, left, mid)
    y = merge_sort(arr, mid, right)

    output = list()

    while len(x) > 0 or len(y) > 0:
        if len(x) == 0:
            output.append(y.pop(0))
        elif len(y) == 0:
            output.append(x.pop(0))
        elif x[0] < y[0]:
            output.append(x.pop(0))
        else:
            output.append(y.pop(0))

    return output




if __name__ == '__main__':
    print('quick sort')
    x = list(range(1, 31))
    random.shuffle(x)
    print(x)
    quick_sort(x, 0, len(x))
    print(x)

    print('heap')
    q = heap()
    x = list(range(1, 31))
    random.shuffle(x)
    q.make_heap_from_array(x)
    print(q.heap)
    y = [q.heap_pop() for _ in range(30)]
    print(y)

    print('merge sort')
    x = list(range(1, 31))
    random.shuffle(x)
    print(x)
    print(merge_sort(x, 0, len(x)))

