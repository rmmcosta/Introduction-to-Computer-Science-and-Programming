from person import Person
from person import Child
from person import Reader
from person import House

p1 = Person('Ricardo','Costa')

p1.present()

print('num childs->',Child.getNumChilds())

c1 = Child('Baby','Costa')

c1.present()
c1.cry()
Child.printNumChilds()
#c1.printNumChilds() #this will not work because the method is a class method
# and not an instance method. Doesn't receive the self

#p1.cry() #will fail because person object has no method cry

print(p1)
print(c1)

print('now the reader...')
r1 = Reader('John','Reader')
print('the initial books:',r1.getBooks())
r1.addBook('tech','How to be a programmer')
print('return tech books:',r1.getBooksByCategory('tech'))
r1.addBook('tech','Clean Code')
r1.addBook('romance','In the Lake')
print('all books:',r1.getBooks())

h1 = House()

print(h1)

h1.addHabitant(p1)
h1.addHabitant(c1)
h1.addHabitant(r1)
h1.printHabitants()

it = iter(h1)
print(it)


for i in range(h1.length()):
    print(next(h1))

for p in iter(h1):
    print(p)

for p in h1:
    print(p)