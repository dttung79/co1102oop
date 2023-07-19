class Animal:
    def say(self):
        print('I am an animal')

class Dog(Animal):
    def woof(self):
        print('I am a dog')

class Cat(Animal):
    def meow(self):
        print('I am a cat')

class Fox(Animal):
    def hitch(self):
        print('I am a fox')

def what_does_the_animal_say(animal):
    if type(animal) == Animal:
        animal.say()
    elif type(animal) == Dog:
        animal.woof()
    elif type(animal) == Cat:
        animal.meow()
    elif type(animal) == Fox:
        animal.hitch()


a = Animal()
what_does_the_animal_say(a)

d = Dog()
what_does_the_animal_say(d)

c = Cat()
what_does_the_animal_say(c)

f = Fox()
what_does_the_animal_say(f)