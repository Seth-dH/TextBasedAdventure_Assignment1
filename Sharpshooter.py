import App, Challenge

charcaterDesc = "(Sharpshooter Character Description)"

class Sharpshooter:
    
    # HP --> 0
    # SP --> 1
    # AP --> 2
    # IP --> 3
    
    def __init__(self):
        self._hp = 3
        self._sp = 0
        self._ap = 2
        self._ip = 1
        
    def BeginStory(self):
        App.DisplayMessage("the start of the challenge, Weakness: AP")
        choice = App.AskOptionedQuestion("What should you do", "SP", "AP", "IP", None)
        
        successValue = None
        if(choice == 1):
            successValue = Challenge.RollSucess(2, 1, self._sp)
        elif(choice == 2):
            successValue = Challenge.RollSucess(2, 2, self._ap)
        elif(choice == 3):
            successValue = Challenge.RollSucess(2, 3, self._ip)
            
        
        