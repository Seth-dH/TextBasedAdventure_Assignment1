import App, Challenge

charcaterDesc = "This character excels in Ranged weaponry, they are known as one of the most accurate Sharpshooters in Cyber City."
    
# HP --> 0
# SP --> 1
# AP --> 2
# IP --> 3
hp = 3
sp = 2
ap = 0
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