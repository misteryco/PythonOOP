class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.stepped_value = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.count > 0:
            current_value = self.stepped_value
            self.stepped_value += self.step
            self.count -= 1
            return current_value
        else:
            raise StopIteration


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
