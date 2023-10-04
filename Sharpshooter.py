import App, Challenge

'''This class deals with the sharshooter storyline, running all of the challeneges'''

charcaterDesc = "(Sharpshooter Character Description)"
    
# HP --> 0
# SP --> 1
# AP --> 2
# IP --> 3
hp = 3
sp = 0
ap = 2
ip = 1
    
def StartChallenege(challengeNum):
    global hp
    global sp
    global ap
    global ip
    
    # challenege description
    if(challengeNum == 1):
        currentWeakness = 2
        App.DisplayMessage("the start of first challenge, Weakness: AP")
        choice = App.AskOptionedQuestion("What should you do", "SP", "AP", "IP", None)
        ResultOfRoll(RollSuccess(choice, currentWeakness), choice)
    
    StartChallenege(challengeNum + 1)
    
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
    
    