class Human:
    species = "Animal"

    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"Welcome, {self.name}!")

    @classmethod
    def get_species(cls):
        return f"This is a species of {cls.species}."

    @staticmethod
    def arbitrary_message():
        return "Have a productive day coding in Python!"


# TEST:
if __name__ == "__main__":
    person = Human("Vitaliy")
    person.welcome()
    print(Human.get_species())
    print(Human.arbitrary_message())