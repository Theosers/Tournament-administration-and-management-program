from models import *
from controller import *
from view import *

if __name__ == '__main__':
    view = View()
    control = Controller(view)

    print("1. New tournament")
    print("2. Add a player")
    print("3. Player's database")
    print("4")
    a = input("Choisissez une action, 1 = nouveau tournoi, 2 = ajouter un joueur")
    a = int(a)
    if a == 1:
        control.new_Tournament()
    elif a == 2:
        control.add_player_to_db(tournoi=False)
    elif a == 3:
        print("1. Show all players")
        print("2. Research a player")
        b = input("Choice : ")
        b = int(b)
        if  b == 1:
            control.all_db_players()
        elif b == 2:
            c = input("Enter the last name and first name")
            print(c.split(' '))
            control.one_db_player(c)
    elif a == 4:
        print("List of all tournaments")
    elif a == 5:
        print("list of all rounds in the tournament")
    elif a == 6 :
        print("list of all matchs in the tournament")

