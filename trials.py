# aggregation example 3

class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def player_info(self):
        print(f"Player Name : {self.name}")
        print(f"Player Position: {self.position}")


class Team:
    def __init__(self, team_name):
        self.name = team_name
        self.players = []

    def add_team_players(self, player):
        self.players.append(player)

    def no_of_team_players(self):
        return len(self.players)

    def view_players_info(self):
        count = 1
        for player in self.players:
            print(f"Player {count}")
            player.player_info()
            count+=1



player_1 = Player("Mohammed Salah", 11)
player_2 = Player("Trent Alexander Arnold", 66)
player_3 = Player("Cole Palmer", 20)
player_4 = Player("Christopher Nkunku", 18)

team_1 = Team("Liverpool")
team_2 = Team("Chelsea")

team_1.add_team_players(player_1)
team_1.add_team_players(player_2)
team_2.add_team_players(player_3)
team_2.add_team_players(player_4)


team_2.view_players_info()
