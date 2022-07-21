def fibonacci():
    f1 = 0
    f2 = 1
    counter = 0
    while True:
        if counter < 2:
            f = counter
            counter += 1
            yield f
        else:
            f = f1 + f2
            f1 = f2
            f2 = f
            yield f


generator = fibonacci()
for i in range(1):
    print(next(generator))
