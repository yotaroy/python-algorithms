class Heap:
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
        self.set_heap(i)

        return output

    def set_heap(self, i):
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

    def make_heap_from_array(self, arr):    # O(n)
        if len(self.heap) != 0:
            print('heap already exists')
            return

        self.heap = arr
        i = len(self.heap) - 1
        while i >= 0:
            self.set_heap(i)
            i -= 1



if __name__ == '__main__':
    import random

    print('heap')
    q = Heap()
    x = list(range(1, 31))
    random.shuffle(x)
    q.make_heap_from_array(x)
    print(q.heap)
    y = [q.heap_pop() for _ in range(30)]
    print(y)

