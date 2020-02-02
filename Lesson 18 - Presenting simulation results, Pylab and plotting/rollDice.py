from random import choice
from pylab import *

diceValues = (1,2,3,4,5,6)

throws = []

#print(choice)

for i in range(1000):
    throw = choice(diceValues) + choice(diceValues)
    #print(throw)
    throws.append(throw)

#print(throws)

hist(throws)
xlabel('throw')
ylabel('n.º of times')
title('Dice roll')
grid(True)
show()


