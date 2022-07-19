def reverse_text(letters: str):
    i = -1
    while i >= -len(letters):
        yield letters[i]
        i -= 1


for char in reverse_text("step"):
    print(char, end='')
