#hello, sir! draft pa ni :))
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def make_sound(self):
        print(f"{self.name} makes a sound.")


class Lion(Animal):
    def eat(self):
        super().eat()
        print(f"{self.name} eats fresh meat.")

    def make_sound(self):
        print(f"{self.name} roars loudly!")


class Elephant(Animal):
    def eat(self):
        super().eat()
        print(f"{self.name} eats grass and fruits.")

    def make_sound(self):
        print(f"{self.name} trumpets!")


class Monkey(Animal):
    def eat(self):
        super().eat()
        print(f"{self.name} eats bananas.")

    def make_sound(self):
        print(f"{self.name} chatters!")



animals = [
    Lion("Leo"),
    Elephant("Ellie"),
    Monkey("Momo")
]


for animal in animals:
    animal.make_sound()
    animal.eat()
    print()
