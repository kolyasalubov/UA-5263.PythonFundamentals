class Human:
    def __init__(self, name: str):
        self.name = name

    def welcome(self):
        print(f"Welcome, {self.name}!")

    @classmethod
    def species(cls) -> str:
        return "Homosapiens"

    @staticmethod
    def message() -> str:
        return "Have a nice day!"


person = Human("John")
person.welcome()
print(Human.species())
print(Human.message())
