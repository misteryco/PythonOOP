def get_primes(list_of_ints):
    # primenumbers are numbers that are divided without remainder only by 1 and themselves.
    # so if you can divided them without remainder with any number (without 0,1 and themselves) they are not primes:

    def is_prime(n):
        for i in range(2, n):
            if (n % i) == 0:
                return False
        return True

    for el in list_of_ints:
        if is_prime(el) and el > 1:
            yield el


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0, 57, 79])))
