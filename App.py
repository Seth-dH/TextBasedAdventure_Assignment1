'''This is the module that deals with player interaction, along with displaying messages/story to the player'''

'''Is called from other modules in order to display messages to the user'''
def DisplayMessage(textToDisplay):
    print (textToDisplay)

'''Adds an empty line to the terminal to break up the text to make it a bit more readable'''
def EmptyLine():
    print(" ")

'''When called this function asks a question and then returns a number based on whichever choice the player decided to pick'''
def AskOptionedQuestion(textToAsk, option1, option2, option3):
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

'''When called this function asked the player a question and then reurns the player’s answer (could be anything)'''
def AskOpenQuestion(textToAsk):
    return input(textToAsk)