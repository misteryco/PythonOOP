from PythonOOP.First_Steps_in_OOP.project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        # what is "pokemon: Pokemon" the first part is the name of the attribute that we're going to use in the
        # current method.
        # The part after ":" explain that this is class "Pokemon" it's not necessary to be used
        # but is highly recommended.
        if pokemon in self.pokemons:
            return f"This pokemon is already caught"
        self.pokemons.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name):
        for pokemon in self.pokemons:
            if pokemon.name == pokemon_name:
                self.pokemons.remove(pokemon)
                return f"You have released {pokemon_name}"
        return f"Pokemon is not caught"

    def trainer_data(self):
        string = ""
        string += f"Pokemon Trainer {self.name}\n"
        string += f"Pokemon count {len(self.pokemons)}\n"
        for pok in self.pokemons:
            string += f"- {pok.pokemon_details()}\n"
        return string.strip()
