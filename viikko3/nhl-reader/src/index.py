import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:

        if player_dict['nationality'] == 'FIN':
            player = Player(
                player_dict['name'],
                player_dict['team'],
                player_dict['goals'],
                player_dict['assists']
        )

            players.append(player)

    print("Players from FIN 2021-01-04:")
    print("")

    players_by_goals = order_players_by_points(players)

    for player in players_by_goals:
        print(player_point_print(player))

def order_players_by_points(player_lst):

    return sorted(player_lst, key=lambda player: player_points(player), reverse=True)

def player_points(player):
    player.points = player.goals + player.assists
    return player.goals+player.assists

def player_point_print(player):

    return f"{player.name}{' '*(25-len(player.name))}{player.team}{' '*(4-len(str(player.goals)))}{player.goals} + {player.assists}{' '*(3-len(str(player.assists)))} = {player.points}"



if __name__ == "__main__":
    main()
