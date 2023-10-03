import App

charcaterDesc = "(Brawler Character Description)"

class Brawler:
    
    # HP --> 0
    # SP --> 1
    # AP --> 2
    # IP --> 3
    
    def __init__(self):
        self._hp = 3
        self._sp = 2
        self._ap = 0
        self._ip = 0
        
    def BeginStory(self):
        