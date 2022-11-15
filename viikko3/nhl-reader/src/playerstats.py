

class PlayerStats:

    def __init__(self, reader):
        
        self.reader = reader
        self.players = self.reader.player_dic

    def top_scorers_by_nationality(self, nationality):

        players_by_nationality = [player for player in self.players if player.nationality == nationality]
        players_by_nationality = self.order_players_by_points(players_by_nationality)

        return players_by_nationality

    def order_players_by_points(self, player_lst):

        return sorted(player_lst, key=lambda player: self.player_points(player), reverse=True)

    def player_points(self, player):
        player.points = player.goals + player.assists
        return player.goals+player.assists

    def player_point_print(self, player):

        return f"{player.name}{' '*(25-len(player.name))}{player.team}{' '*(4-len(str(player.goals)))}{player.goals} + {player.assists}{' '*(3-len(str(player.assists)))} = {player.points}"

