class Dog:

    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

bob = Dog("Bob", 5)
fluff = Dog("Fluff", 9)
hen = Dog("Hen", 2)


def get_biggest_number(*args):
    return max(args)


print("The oldest dog is {} years old.".format(
    get_biggest_number(bob.age, fluff.age, hen.age)))
