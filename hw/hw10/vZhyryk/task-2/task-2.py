from random import randint

class Ghost:
    @staticmethod
    def get_random_color() -> str:
        return ["white", "yellow", "purple", "red"][randint(0, 3)]

    def __init__(self):
        self.color = self.get_random_color()
