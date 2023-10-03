'''This is the method that deals with player interaction, along with displaying messages/story to the player'''

# used for displaying text to the player
def DisplayMessage(textToDisplay):
    print (textToDisplay)
    
def EmptyLine():
    print(" ")
    
def AskOptionedQuestion(textToAsk, option1, option2, option3, option4):
    numOfOptions = 0
    while(True): 
        print(textToAsk)
        print(" ")
        
        if(option1 != None):
            print("1: " + option1)
            numOfOptions = 1
        if(option2 != None):
            print("2: " + option2)
            numOfOptions = 2
        if(option3 != None):
            print("3: " + option3)
            numOfOptions = 3
        if(option4 != None):
            print("4: " + option4)
            numOfOptions = 4
            
        print(" ")
        playerCh = input("Select one by typing the option number: ")
        
        if(playerCh.isdigit()):
            playerCh = int(playerCh)
            if(0 < playerCh <= numOfOptions):
                return playerCh
            else:
                print("Invalid input, Please try again.")
                continue
        else:
                print("Invalid input, Please try again.")
                continue

def AskOpenQuestion(textToAsk):
    return input(textToAsk)