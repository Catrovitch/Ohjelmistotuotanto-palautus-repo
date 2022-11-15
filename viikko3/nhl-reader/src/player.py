class Player:
    def __init__(self, name, team, goals, assists, nationality, penalties, games):

        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
        self.nationality = nationality
        self.penalties = penalties
        self.games = games
        self.points = self.goals + self.assists
    
    def __str__(self):
        return f"{self.name}{' '*(25-len(self.name))}{self.team}{' '*(4-len(str(self.goals)))}{self.goals} + {self.assists}{' '*(3-len(str(self.assists)))} = {self.points}"
