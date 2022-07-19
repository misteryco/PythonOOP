def squares(n):
    i = 0
    while i < n:
        i += 1
        yield i ** 2


a = list(squares(5))
print(a)
a = 5
