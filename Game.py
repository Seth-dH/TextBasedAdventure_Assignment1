import App, Sharpshooter, Brawler

'''
This method deals with the gameplay
'''

# Game Introduction
App.DisplayMessage("Welcome to Cyberheist!")
App.DisplayMessage("In this game you are a member of a bandit team in a futuristic dystopia. You are running a heist on a rival gang’s headquarters. You have been hired by gang leader 'Barron'. He his hired you in order to find a memory chip hidden inside the rival gang’s headquarters. This memory chip was stolen from Barron and has the location to the gang’s weapons storehouse.")
App.DisplayMessage("How to play:") 
App.DisplayMessage("You will face 3 challenges. For each decision you make, there will be an attribute related to that decision. The more points your character has in that attribute, the higher chance you will  have at succeeding in that decision. ")
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
    Sharpshooter.StartChallenege(1)
    
elif(choice == 2):
   App.DisplayMessage("Welcome %s, The Brawler" % (playerName)) 
   