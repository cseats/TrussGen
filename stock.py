import random

def getStock():

    n = 20
    lB = 1
    uB = 8
    stock = []
    for i in range(50):

        r = random.randint(lB,uB)
        stock.append(r)
    
    return stock