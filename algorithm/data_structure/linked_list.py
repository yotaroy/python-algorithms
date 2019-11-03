class Cell:
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, item):
        if self.head is None:
            self.head = Cell(item)
        else:
            next_cell = self.head
            while True:
                if next_cell.next is None:
                    next_cell.next = Cell(item)
                    break
                next_cell = next_cell.next

    def delete(self, item):
        if self.head is None:
            print('No data error')
        elif self.head.item == item:
            if self.head.next is None:
                self.head = None
            else:
                self.head = self.head.next
        else:
            cell = self.head
            while True:
                next_cell = cell.next
                if next_cell.item == item:
                    cell.next = next_cell.next
                    break
                cell = next_cell
                if cell.next is None:
                    break

    def list_print(self):
        next_cell = self.head
        while next_cell is not None:
            print(next_cell.item, end=', ')
            next_cell = next_cell.next
        print()


if __name__ == '__main__':
    l = LinkedList()
    l.insert('first')
    l.insert('second')
    l.list_print()
    l.insert('third')
    l.insert('forth')
    l.list_print()
    l.delete('first')
    l.list_print()
    l.delete('forth')
    l.list_print()
    l.insert('new')
    l.list_print()
