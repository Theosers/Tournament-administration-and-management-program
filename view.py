class View:
    def prompt_for_new_tournament_infos(self):
        print(f"A new tournament has begun")
        name = input("Name of this tournament : ")
        place = input("Place of this tournament : ")
        date = input("date : ")
        number_of_rounds = input("Number of rounds : ")
        number_of_players = input("Number of players : ")
        time_control = input("Bullet, blitz or rapid tournament ? : ")
        description = input("Enter a quick description of this tournament : ")
        return [name, place, date, int(number_of_rounds), int(number_of_players), time_control, description]

    def prompt_for_asking_player_name(self):
        return input("What is the last_name and first_name of this player ?")

    def prompt_for_new_player(self):
        last_name = input("Last_name :")
        first_name = input("First_name :")
        birthday_date = input("Birthday_date :")
        gender = input("Gender :")
        rank = input("Rank :")
        new_player_infos = {'last_name': last_name, 'first_name': first_name, 'birthday_date': birthday_date,
                            'gender': gender, 'rank': rank}

        return new_player_infos

    def prompt_for_end_of_tournament(self, joueur, resultats):
        print(f'The score of {joueur} is {resultats}')

    def prompt_for_winner(self):
        return input("if there is a winner, enter his full name, if it is a tie, enter 'tie':")

    def prompt_menu(self):
        print("----------------------------------------------------------------------------")
        print("1. New tournament")
        print("2. Add a player")
        print("3. Player's database")
        print("4. List all tournaments")
        print("5 .List of all rounds in a tournament")
        print("----------------------------------------------------------------------------")
        choice = input("Your choice ? :")
        choice = int(choice)
        return choice

    def prompt_menu_player_db(self):
        print("1. Show all players")
        print("2. Research a player")
        choice = input("Choice : ")
        choice = int(choice)
        return choice
