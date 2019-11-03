class Queue:
    def __init__(self, size=10**2):
        self.queue = [None] * size
        self.size = size
        self.head = 0
        self.tail = 0

    def pop(self):
        if self.head == self.tail:
            print('No data error')
            return None

        popped_item = self.queue[self.head]
        self.head = (self.head + 1) % self.size
        return popped_item

    def push(self, item):
        if (self.tail + 1) % self.size == self.head:
            print('Data overflow error')
            return

        self.queue[self.tail] = item
        self.tail = (self.tail + 1) % self.size


if __name__ == '__main__':
    q = Queue(size=3)
    q.push('a')
    q.push('c')
    q.push('d')
    print(q.pop())
    q.push('y')
    print(q.pop())
    print(q.pop())
    print(q.pop())
