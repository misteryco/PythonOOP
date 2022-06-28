def rhombus_of_stars(n):
    string = ""
    for i in range(n):
        stars = 1 + i
        spaces = n - stars
        string += f'{" " * spaces + "* " * stars}\n'
    for i in range(n - 2, -1, -1):
        stars = 1 + i
        spaces = n - stars
        string += f'{" " * spaces + "* " * stars}\n'
    return string

print(rhombus_of_stars(int(input())))
