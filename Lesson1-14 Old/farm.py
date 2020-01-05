def getAnimals(heads,legs):
    '''given the heads and legs returns the quantity of 
    pigs, chickens and spiders'''
    assert heads>0, 'you must specify a positive number of heads'
    assert legs>=heads*2, 'each animal (head) must have at least two legs'
    for pigs in range(heads+1):
        for chickens in range(heads+1-pigs):
            for spiders in range(heads+1-pigs-chickens):
                if( sumLegs(pigs,chickens,spiders)==legs
                    and
                    sumHeads(pigs,chickens,spiders)==heads
                ):
                    #returns a dictionary
                    return {"pigs":pigs,"chickens":chickens,"spiders":spiders}
    return 'the number of heads and legs don\'t match'

def getAllAnimals(heads,legs):
    '''given the heads and legs returns the quantity of 
    pigs, chickens and spiders'''
    assert heads>0, 'you must specify a positive number of heads'
    assert legs>=heads*2, 'each animal (head) must have at least two legs'
    #ans will be a list of dictionaries
    #it can't be a tuple because a tuple is an immutable object
    ans = []
    for pigs in range(heads+1):
        for chickens in range(heads+1-pigs):
            for spiders in range(heads+1-pigs-chickens):
                if( sumLegs(pigs,chickens,spiders)==legs
                    and
                    sumHeads(pigs,chickens,spiders)==heads
                ):
                    #returns a dictionary
                    ans.append({"pigs":pigs,"chickens":chickens,"spiders":spiders})
    if(len(ans)>0):
        return ans
    else:
        return 'the number of heads and legs don\'t match'
            
def sumLegs(pigs,chickens,spiders):
    '''for the given number of pigs, chickens and
    spiders returns the total number of legs'''
    return pigs*4+chickens*2+spiders*8

def sumHeads(pigs,chickens,spiders):
    '''for the given number of pigs, chickens and 
    spiders returns the total number of heads'''
    return pigs+chickens+spiders
