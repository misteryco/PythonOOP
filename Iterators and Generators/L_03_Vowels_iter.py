class vowels:
    def __init__(self, letters: str):
        self.letters = letters
        self.filtered_for_vowels = [x for x in self.letters if x.upper() in "AOUEIY"]
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.filtered_for_vowels):
            current_index = self.index
            self.index += 1
            return self.filtered_for_vowels[current_index]
        else:
            raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
