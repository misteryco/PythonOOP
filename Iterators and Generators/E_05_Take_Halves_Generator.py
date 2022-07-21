def solution():
    def integers():
        i = 0
        while True:
            i += 1
            yield i

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        result = []
        for i in range(n):
            generator_value = next(seq)
            result.append(generator_value)
        return result

    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))

take = solution()[0]
halves = solution()[1]
print(take(0, halves()))
