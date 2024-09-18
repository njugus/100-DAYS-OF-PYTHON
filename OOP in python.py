# composition and aggregation
# composition
class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return (self.pay * 12) + self.bonus


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.obj_salary = salary

    def total_salary(self):
        return self.obj_salary.annual_salary()

salary = Salary(1500000, 30000)
employee_1 = Employee("Kelvin", 21, salary)
print(employee_1.total_salary())


# aggregation
class Book:
    def __init__(self, name, author, price):
        self.name  = name
        self.author = author
        self.price = price

    def book_info(self):
        print(f"Book Name : {self.name}")
        print(f"Book Author : {self.author}")
        print(f"Book Price : { self.price}")

class Library:
    def __init__(self, location):
        self.location = location
        self.books_available = []

    def add_a_new_book(self, book):
        self.books_available.append(book)

book_1 = Book("Silva Technique", "hose silva", 5000)
library_system = Library("Limuru")
library_system.add_a_new_book(book_1)


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
