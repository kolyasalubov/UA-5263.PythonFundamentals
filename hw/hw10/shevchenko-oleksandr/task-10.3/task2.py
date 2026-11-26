class Human:
    def __init__(self, name):
        self.name = name

    def greeting_for_person(self):
        return f"Hello, {self.name}!"

    @classmethod
    def species_of_human(cls):
        return f"{cls.__name__} is a species of Homosapiens."

    @staticmethod
    def arbitrary_message():
        return "A message from the Human class."


def main():
    people = [Human("John"), Human("Jane")]

    for person in people:
        print(person.greeting_for_person())

    print(Human.species_of_human())
    print(Human.arbitrary_message())


if __name__ == "__main__":
    main()
