import unittest
from statistics import Statistics
from index import SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53), 
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_player_exists(self):

        player = self.statistics.search("Semenko")

        self.assertEqual((player.name, player.team, player.goals, player.assists), ("Semenko", "EDM", 4, 12))

    def test_search_player_non_existing(self):

        self.assertEqual(self.statistics.search("Gozzilla"), None)

    def test_team_test(self):

        team_search = self.statistics.team("EDM")
        
        for player in team_search:
            self.assertEqual(player.team, "EDM")

    def test_top_none(self):

        top_three_none = self.statistics.top(3)


        self.assertEqual((top_three_none[0].name, top_three_none[1].name, top_three_none[2].name), ("Gretzky", "Lemieux", "Yzerman"))

    def test_top_points(self):

        top_three_points = self.statistics.top(3, SortBy.POINTS)

        self.assertEqual((top_three_points[0].name, top_three_points[1].name, top_three_points[2].name), ("Gretzky", "Lemieux", "Yzerman"))


    def test_top_goals(self):

        top_three_goals = self.statistics.top(3, SortBy.GOALS)

        self.assertEqual((top_three_goals[0].name, top_three_goals[1].name, top_three_goals[2].name), ("Lemieux", "Yzerman", "Kurri"))

    def test_top_assists(self):

        top_three_assist = self.statistics.top(3, SortBy.ASSISTS)

        self.assertEqual((top_three_assist[0].name, top_three_assist[1].name, top_three_assist[2].name), ("Gretzky", "Yzerman", "Lemieux"))

    def test_top_incorrect_input(self):

        value = self.statistics.top(3, 4)

        self.assertEqual(value, None)


