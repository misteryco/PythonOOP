def read_next(*iterables):
    for row in range(len(iterables)):
        for el in iterables[row]:
            yield el


for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')
