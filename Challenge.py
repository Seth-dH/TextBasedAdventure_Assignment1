import random, App
    
'''This script deals with the "Rolling" mechanic. '''
    
'''Deals with the rolling of the ‘dice’ and returns a value from -1 to 2 based on how successful the player was'''
def RollSucess (weakness, actionType, value):
    App.EmptyLine()
    
    wasSuccessful = False
    numOfRolls = 1 + value
    if(weakness == actionType):
        numOfRolls += 1

    App.DisplayMessage("Number of rolls: " + str(numOfRolls))
    
    #begin sucess calculation
    for num in range(numOfRolls):
        roll = random.randint(1, 6)
        
        if(roll == 6):
            wasSuccessful = True
            App.DisplayMessage("roll " + str(num + 1) + " was: " + str(roll) + " (Successfull)")
            break
        App.DisplayMessage("roll " + str(num + 1) + " was: " + str(roll) + " (Un-sucessfull)")
    else:
        roll = random.randint(1, 6)
        if(roll == 6):
            #critical loss
            App.DisplayMessage("Critical loss roll was Sucessfull")
            return -1
        else:
            #loss
            App.DisplayMessage("critical loss roll was Un-sucessfull")
            return 0
            
    if(wasSuccessful):
        roll = random.randint(1, 6)
        if(roll == 6):
            #critical win
            App.DisplayMessage("Critical win roll was Sucessfull")
            return 2
        else:
            #win
            App.DisplayMessage("Critical win roll was Un-sucessfull")
            return 1
    App.EmptyLine()
        