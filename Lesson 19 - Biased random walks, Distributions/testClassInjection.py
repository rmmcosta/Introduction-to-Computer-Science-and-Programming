from classInjection import *

def createAnimal(AnimalType):
    return AnimalType()

a = createAnimal(Animal)
a.makeSound()
a.run()

d = createAnimal(Dog)
d.makeSound()
d.run()

c = createAnimal(Cat)
c.makeSound()
c.run()
