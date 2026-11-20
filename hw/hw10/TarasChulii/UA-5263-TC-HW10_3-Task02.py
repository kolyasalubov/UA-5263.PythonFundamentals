class Human():
    def __init__(self, name):
        self.name = name

    def greeting_for_person(self):
        return f"Hello, {self.name.capitalize()}!"

    @classmethod
    def species_of_human(cls):
        return f"Human is a species of Homo sapiens."

    @staticmethod
    def arbitrary_message():
        return f"This is a message from static method"


def self_test():
    #Create Instance#1 of Human
    inst_1 = Human("john")

    #Create Instance#2 of Human
    inst_2 = Human("Jane")

    #Test method in the class
    print(f"Test method in the class =>")
    print(inst_1.greeting_for_person())
    print(inst_2.greeting_for_person())
    print(f"")

    #Test class method
    print(f"Test class method =>")
    print(Human.species_of_human())
    print(inst_1.species_of_human())
    print(inst_2.species_of_human())
    print(f"")

    #Test static method
    print(f"Test static method =>")
    print(Human.arbitrary_message())
    print(inst_1.arbitrary_message())
    print(inst_2.arbitrary_message())
    print(f"")


if __name__ == "__main__":
    self_test()