class Queue:
    def __init__(self):
        self.__items = []

    def enqueue(self, item):
        self.__items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def __len__(self):
        return len(self.__items)
    @property
    def first(self):
        if len(self.__items)
            return self.__items[-1]
        return None

    @property
    def is_empty(self):
        return self.__items == []
