class Person:
    def __init__(self,firstname,lastname):
        self._firstname = firstname
        self._lastname = lastname

    def present(self):
        print('My name is {} {}'.format(self._firstname, self._lastname))

    def __str__(self):
        return self._lastname + ', ' + self._firstname

class Child(Person):
    numChilds = 0

    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)
        Child.incChilds()
        self._childNum = Child.numChilds

    def __str__(self):
        return super().__str__() + ', Child number:{}'.format(self._childNum)

    def cry(self):
        print('{},{} is crying'.format(self._lastname,self._firstname))

    def incChilds():
        if(Child.numChilds<1):
            Child.numChilds = 1
        else:
            Child.numChilds+=1
    
    def getNumChilds():
        return Child.numChilds

    def printNumChilds():
        print('num childs:',Child.numChilds)

class Reader(Person):

    def __init__(self,firstname,lastname):
        super().__init__(firstname,lastname)
        self._books = {}

    def addBook(self,category,name):
        if(category in self._books):
            self._books[category].append(name)
        else:
            self._books[category] = [name]

    def getBooksByCategory(self,category):
        return self._books[category]

    def getBooks(self):
        return self._books

class House:
    def __init__(self):
        super().__init__()
        self._habitants = []

    def addHabitant(self,Person):
        self._habitants.append(Person)

    def __iter__(self):
        self.n = 0
        return self
    
    def __next__(self):
        if(self.n>len(self._habitants)-1):
            raise StopIteration
        person = self._habitants[self.n]
        self.n += 1
        if(type(person) == Child):
            return 'The Child: ' + str(person)
        elif(type(person) == Reader):
            return 'The Reader:' + str(person)
        else:
            return 'Standard:' + str(person)

    def printHabitants(self):
        print('Habitants:',self._habitants)

    def length(self):
        return len(self._habitants)