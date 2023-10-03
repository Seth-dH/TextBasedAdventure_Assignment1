import random
    
def RollSucess (weakness, actionType, value):
    wasSuccessful = False
    numberOfRolls = 1 + value
    if(weakness == actionType):
        numberOfRolls += 1
    
    #begin sucess calculation
    for num in numberOfRolls:
        roll = random.randint(1, 12)
        
        if(roll == 12):
            wasSuccessful = True
            break
    else:
        roll = random.randint(1, 12)
        if(roll == 12):
            #critical loss
            return -1
        else:
            #loss
            return 0
            
    if(wasSuccessful):
        roll = random.randint(1, 12)
        if(roll == 12):
            #critical win
            return 2
        else:
            #win
            return 1
        