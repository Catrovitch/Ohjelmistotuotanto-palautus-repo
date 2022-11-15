from playerreader import PlayerReader
from playerstats import PlayerStats
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"

    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    players = stats.top_scorers_by_nationality("FIN")

    print("Players from FIN 2021-01-04:")
    
    for player in players:
        print(player)

if __name__ == "__main__":
    main()
