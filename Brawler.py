import App, Challenge

'''This module is for playing the brawler storyline. It deals with all the mechanics that are involved in the character’s story along with the unique dialogue for the brawler’s story'''

charcaterDesc = "The Brawns of the operation, this character uses his heavily augmented fists to get most jobs done. His favorite food is Mashed Potatoes."

# stats numeric value:  
# HP --> 0
# SP --> 1
# AP --> 2
# IP --> 3
hp = 5 # helth points
sp = 2 # strength points
ap = 0 # accuracy points
ip = 0 # intellegence points

"""Starts whatever challenge number is passed into this function"""
def StartChallenege(challengeNum):
    global hp
    global sp
    global ap
    global ip
    
    # challenege description
    if(challengeNum == 1):
        currentWeakness = 3
        App.DisplayMessage("for the fist challenge of this mission you must find the map of this building so you know where you need to go. Weakness: IP")
        choice = App.AskOptionedQuestion("What should you do:", "beat the crap out of a grunt lying on the floor until he sends you the map data: SP", "throw a brick at a fire alarm on a higher floor causing exit maps to appear: AP", "guess what the passcode for the main computer is: IP")
        ResultOfRoll(RollSuccess(choice, currentWeakness), choice)
    elif(challengeNum == 2):
        currentWeakness = 2
        App.DisplayMessage("As you are walking along, you come aross security drones that start to hinder your path. you must now destroy them to move on. Weakness: AP")
        choice = App.AskOptionedQuestion("What should you do:", "smash them all, with your bare hands: SP", "use debris from the ground to knock them out of the air: AP", "set an explosion to go off in the main corridor to lure all the security bots out: IP")
        ResultOfRoll(RollSuccess(choice, currentWeakness), choice)
    elif(challengeNum == 3):
        currentWeakness = 3
        App.DisplayMessage("Finaly, to get to the room that storing the data, you have to go up an elevator shaft. Weakness: IP")
        choice = App.AskOptionedQuestion("What should you do:", "call the elevator and fight all of the grunts that rush out: SP", "shoot the cables holding up the elevator and then climb the elevator shaft: AP", "call the elevator, and then sneak in behind all the guard that come pouring out: IP")
        ResultOfRoll(RollSuccess(choice, currentWeakness), choice)
    elif(challengeNum >= 4):
        PlayFinalBoss()
        App.DisplayMessage("Thanks For Playing")
        exit()
    
    StartChallenege(challengeNum + 1)

'''Starts the final boss challenge '''
def PlayFinalBoss():
    global hp
    
    bossHp = 3
    App.DisplayMessage("finally, as you make your way up the elevator you head inot the final room. this is where you meet the rival gang boss. In order to get back the dats you have to pry it from his cold dead hands. Weakness: NONE")
    while (bossHp > 0 and hp > 0):
        choice = App.AskOptionedQuestion("What will you do: ", "Shoot him with you gun: SP", "fight him with your bare fists: AP", "Try and convince him to hand over the data so nobody get's hurt: IP")
        successValue = RollSuccess(choice, None)
        ResultOfRoll(successValue, choice)
        if(successValue == 1):
            App.DisplayMessage("The boss has lost HP")
            bossHp -= 1
        if(successValue == 2):
            App.DisplayMessage("The boss has lost a lot of HP")
            bossHp -= 2
            
        App.DisplayMessage("The boss has " + str(bossHp) + " HP left")
        
    if(bossHp <= 0):
        App.DisplayMessage("You Killed the boss! you were able to sucessfully retrive the data and save your gang!")
        App.DisplayMessage("Congradulations! You Won!")
    
'''Rolls the success of the challenge depending on which option the player chose to use'''     
def RollSuccess(choice, currentWeakness):
    global hp
    global sp
    global ap
    global ip
    
    successValue = None
    if(choice == 1):
        successValue = Challenge.RollSucess(currentWeakness, 1, sp)
    elif(choice == 2):
        successValue = Challenge.RollSucess(currentWeakness, 2, ap)
    elif(choice == 3):
        successValue = Challenge.RollSucess(currentWeakness, 3, ip)  
    return successValue

'''Updates the result of the roll to the players stats depending on if it was a critical loss, loss, win or critical win'''
def ResultOfRoll(successValue, choice):
    global hp
    global sp
    global ap
    global ip
    
    # results of  the roll
    if(successValue == -1):
        # critical loss
        hp -=1
        if(choice == 1):
            App.DisplayMessage("Unfortunately, you were critically unsuccessful. you will now loose one HP point and one STRENGTH point (SP) ")
            sp -= 1
            if(sp <= 0): sp = 0
        elif(choice == 2):
            App.DisplayMessage("Unfortunately, you were critically unsuccessful. you will now loose one HP point and one ACCURACY point (AP) ")
            ap -= 1
            if(ap <= 0): ap = 0
        elif(choice == 3):
            App.DisplayMessage("Unfortunately, you were critically unsuccessful. you will now loose one HP point and one INTELLEGENCE point (IP) ")
            ip -=1
            if(ip <= 0): ip = 0
    elif(successValue == 0):
        # loss
        App.DisplayMessage("Unfortunately, you were unsuccessful. you will now loose one HP point")
        hp -= 1
    elif(successValue == 2):
        # critical win
        if(choice == 1):
            App.DisplayMessage("You were successfull! you will now gain one STRENGTH point (SP)")
            sp += 1
        elif(choice == 2):
            App.DisplayMessage("You were successfull! you will now gain one Accuracy point (AP)")
            ap += 1
        elif(choice == 3):
            App.DisplayMessage("You were successfull! you will now gain one INTELLEGENCE point (IP)")
            ip +=1
            
    if(hp <= 0):
        App.DisplayMessage("You died! Game over :(")
        exit()
            
    DisplayStats()
    
'''Displays the user's current stat points'''         
def DisplayStats():
    global hp
    global sp
    global ap
    global ip
    
    App.DisplayMessage("Your current stats are:")
    App.DisplayMessage("HP: " + str(hp))
    App.DisplayMessage("SP: " + str(sp))
    App.DisplayMessage("AP: " + str(ap))
    App.DisplayMessage("IP: " + str(ip))
    