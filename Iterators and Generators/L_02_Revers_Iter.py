class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = -1

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        if self.index >= -len(self.iterable):
            current_index = self.index
            self.index -= 1
            return self.iterable[current_index]
        else:
            raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
