
class Team():
    def __init__(self,name,players,coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0

    def add_player(self,name):
        self.players.append(name)
    
    def has_player(self,name):
            if name in self.players:
                return True
            else:
                return False
    
    def play_game(self,has_won):
        if has_won == True:
            self.points += 3
       