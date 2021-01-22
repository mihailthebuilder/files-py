class Human:
    species = "h. sapiens"

    def __init__(self, name):
        self.name = name
        self._age = 0

    @property
    def age(self):
        return self._age


joe = Human("joe")

print(joe.species)
print(joe._age)
