#there is a temple in the middle of hanoi
#3 very large diamond-ecnrusted posts
#64 disks in each 3 all of different sizes
#the priests have to move the disks from on post to hte other
#they can only move one disk at a time
#they can never cover up a smaller disk with a larger one

def moveTower(size,fromTower,toTower,spareTower):
    #base case
    if size == 1:
        print('Move disk ', fromTower,' to ',toTower)
    else:
        moveTower(size-1,fromTower,spareTower,toTower)
        moveTower(1,fromTower,toTower,spareTower)
        moveTower(size-1,spareTower,toTower,fromTower)
        
def moveTowerList(size,fromTower,toTower,spareTower):
    #base case
    if size == 1:
        #print('Move disk ', fromTower,' to ',toTower)
        moveElem(fromTower,toTower)
    else:
        moveTowerList(size-1,fromTower,spareTower,toTower)
        moveTowerList(1,fromTower,toTower,spareTower)
        moveTowerList(size-1,spareTower,toTower,fromTower)    

def moveElem(fromTower,toTower):
    toTower.append(fromTower.pop())

def printElems(elem1,elem2,elem3):
    print('elem1:'+str(elem1)+',elem2:'+str(elem2)+',elem3:'+str(elem3))

def moveTowerRec(fromTower,toTower,spareTower):
    size = len(fromTower)
    if(size==0):
        return None
    if(size%2==0):
        toTower.append(fromTower.pop(size-1))
        toTower.append(spareTower)
        printTowerStatus(fromTower,toTower,spareTower)
    else:
        spareTower.append(fromTower.pop(size-1))
        spareTower.append(toTower)
        toTower = spareTower
    spareTower.clear()
    return moveTower(fromTower,toTower,spareTower)

def towers():
    tower1 = []
    tower2 = []
    tower3 = []
    initializeTower(tower1)
    printTowerStatus(tower1,tower2,tower3)
    moveTowerList(len(tower1),tower1,tower2,tower3)
    printTowerStatus(tower1,tower2,tower3)

def printTowerStatus(tower1,tower2,tower3):
    print('Tower 1')
    print(tower1)
    print('Tower 2')
    print(tower2)
    print('Tower 3')
    print(tower3)

def initializeTower(tower):
    for i in range(64,0,-1):
        tower.append(i)
