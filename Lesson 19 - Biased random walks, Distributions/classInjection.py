class Animal:
    def makeSound(self):
        print('aaaa aaaa aaaa')
    def run(self):
        print('Running...')

class Dog(Animal):
    def makeSound(self):
        #call parent make sound
        super().makeSound()
        print('dddd dddd dddd')

class Cat(Animal):
    def makeSound(self):
        print('miau')