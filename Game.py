import App, Sharpshooter, Brawler

'''
This method deals with the gameplay
'''

# Game Introduction
App.DisplayMessage("Game intro")
choice = App.AskOptionedQuestion("To begin, Select Play", "Play", "Quit", None, None)
if(choice == 2):
    print("Thank you! Have a good day")
    exit()
    
choice = App.DisplayMessage("Here are the 2 characters you can play as: ")
App.EmptyLine()
App.DisplayMessage("1. SharpShooter: ")
App.DisplayMessage(Sharpshooter.charcaterDesc)
App.EmptyLine()
App.DisplayMessage("2. Brawler: ")
App.DisplayMessage(Brawler.charcaterDesc)
App.EmptyLine()
choice = App.AskOptionedQuestion("Please choose a character: ", "Sharpshooter", "Brawler", None, None)

playerName = App.AskOpenQuestion("Please input your name: ")

if(choice == 1):
    App.DisplayMessage("Welcome %s, The Sharpshooter" % (playerName))
    
elif(choice == 2):
   App.DisplayMessage("Welcome %s, The Brawler" % (playerName)) 