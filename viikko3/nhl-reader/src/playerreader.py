import requests
from player import Player

class PlayerReader:

    def __init__(self, url):

        self.response = requests.get(url).json()
        self.player_dic = self.player_dic_list()
    
    def player_dic_list(self):

        self.players = []

        for player_dict in self.response:

            player = Player(
                player_dict['name'],
                player_dict['team'],
                player_dict['goals'],
                player_dict['assists'],
                player_dict['nationality'],
                player_dict['penalties'],
                player_dict['games']
            )

            self.players.append(player)

        return self.players