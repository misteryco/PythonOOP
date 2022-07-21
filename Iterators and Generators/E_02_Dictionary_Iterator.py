class dictionary_iter:
    def __init__(self, a_dict_object: dict):
        self.a_dict_object = a_dict_object
        self.dict_as_list = [(x, y) for x, y in self.a_dict_object.items()]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.dict_as_list):
            current_index = self.index
            self.index += 1
            return self.dict_as_list[current_index]
        else:
            raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
