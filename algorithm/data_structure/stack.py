class Stack:
    def __init__(self, size=10**2):
        self.stack = [None] * size
        self.size = size
        self.top = 0

    def pop(self):
        if self.top == 0:
            print('No data error')
            return None
        self.top -= 1
        return self.stack[self.top]

    def push(self, item):
        if self.top == self.size:
            print('Data overflow error')
            return
        self.stack[self.top] = item
        self.top += 1


if __name__ == '__main__':
    s = Stack(size=3)
    print(s.pop())
    s.push('t')
    s.push('k')
    s.push('j')
    s.push('i')
    print(s.pop())
    print(s.pop())
