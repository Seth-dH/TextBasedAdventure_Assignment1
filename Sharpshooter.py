import App, Challenge

'''This class deals with the sharshooter storyline, running all of the challeneges'''

charcaterDesc = "This character excels in Ranged weaponry, they are known as one of the most accurate Sharpshooters in Cyber City."
    
# stats numeric value:  
# HP --> 0
# SP --> 1
# AP --> 2
# IP --> 3

hp = 3 # helth points
sp = 0 # strength points
ap = 2 # accuracy points
ip = 1 # intellegence points
    
def StartChallenege(challengeNum):
    global hp
    global sp
    global ap
    global ip
    
    # challenege description
    if(challengeNum == 1):
        currentWeakness = 1
        App.DisplayMessage("The first challenege you must complete is destroying the security systems. Weakness: SP")
        choice = App.AskOptionedQuestion("What should you do:", "Smash the emergeny stop button: SP", "Shoot the electrical box that supplies power for the security system: AP", "Call up a guard on the comms and tell them that the enemy has take control of the security system, making them shut it down: IP")
        ResultOfRoll(RollSuccess(choice, currentWeakness), choice)
    elif(challengeNum == 2):
        currentWeakness = 3
        App.DisplayMessage("As you walk into the next room you are confronted by a grunt. Weakness: IP")
        choice = App.AskOptionedQuestion("What should you do:", "Hit him with a metal bar you picked up off the ground: SP", "Shoot him with your lazer gun: AP", "Trick him into thinking you’re another grunt: IP")
        ResultOfRoll(RollSuccess(choice, currentWeakness), choice)
    elif(challengeNum == 3):
        currentWeakness = 2
        App.DisplayMessage("Finally, you have one last challenge to face. In order to get to the final room you have to fight your way up the stairs. Weakness: AP")
        choice = App.AskOptionedQuestion("What should you do:", "bash your way up the good ‘ol fashion way: SP", "pick them all off as they’re coming down the stairs: AP", "set off the sprinkler systems s the grunts all fall down the stairs: IP")
        ResultOfRoll(RollSuccess(choice, currentWeakness), choice)
    elif(challengeNum >= 4):
        PlayFinalBoss()
        App.DisplayMessage("Thanks For Playing")
        exit()
    
    StartChallenege(challengeNum + 1)
    
def PlayFinalBoss():
    global hp
    
    bossHp = 3
    App.DisplayMessage("finally, as you make your way up the sair you head inot the final room. this is where you meet the rival gang boss. In order to get back the dats you have to pry it from his cold dead hands. Weakness: NONE")
    while (bossHp > 0 and hp > 0):
        choice = App.AskOptionedQuestion("What will you do: ", "Shoot him with you gun: SP", "fight him with your bare fists: AP", "Try and convince him to hand over the data so nobody get's hurt: IP", None)
        successValue = RollSuccess(choice, None)
        ResultOfRoll(successValue, choice)
        if(successValue == 1):
            App.DisplayMessage("The boos has lost HP")
            bossHp -= 1
        if(successValue == 2):
            App.DisplayMessage("The boss has lost a lot of HP")
            bossHp -= 2
            
        App.DisplayMessage("The boss has " + str(bossHp) + " HP left")
        
    if(bossHp <= 0):
        App.DisplayMessage("You Killed the boss! you were able to sucessfully retrive the data and save your gang!")
        App.DisplayMessage("Congradulations! You Won!")
    if(hp <= 0):
        App.DisplayMessage("You died! Game Over")
    
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
            
    DisplayStats()
            
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
    
    