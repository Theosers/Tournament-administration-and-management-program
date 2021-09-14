class View:
    def prompt_for_new_tournament_infos(self):
        print("A new tournament has begun\n")
        print(
            '-----------------------------------------------------------------------------------------------------')
        name = input("Name of this tournament : ")
        place = input("Place of this tournament : ")
        date = input("Date : ")
        number_of_rounds = input("Number of rounds : ")
        number_of_players = input("Number of players : ")
        time_control = input("Bullet, blitz or rapid tournament ? : ")
        description = input("Enter a quick description of this tournament : ")
        print(
            '-----------------------------------------------------------------------------------------------------')
        return [name, place, date, int(number_of_rounds), int(number_of_players), time_control, description]

    def prompt_for_asking_player_name(self):
        return input("\nWhat is the full name of this player ? : ")

    def prompt_for_new_player(self):
        print(
            '***********************************************')
        last_name = input("Last name :")
        first_name = input("First name :")
        birthday_date = input("Birthday date :")
        gender = input("Gender :")
        rank = input("Rank :")
        print("New player added successfully\n")
        new_player_infos = {'last_name': last_name, 'first_name': first_name, 'birthday_date': birthday_date,
                            'gender': gender, 'rank': rank}
        print(
            '***********************************************')

        return new_player_infos

    def prompt_for_end_of_tournament(self, joueur, resultats):
        print(f'The score of {joueur} is {resultats}')

    def prompt_for_winner(self, pairing):
        return input(
            f"Who wins between {pairing[0]} and {pairing[1]} : ")

    def prompt_menu(self):
        print("----------------------------------------------------------------------------")
        print("1. New tournament")
        print("2. Add a player")
        print("3. Player's database")
        print("4. List all tournaments")
        print("5. List of all rounds in a tournament")
        print("6. Exit")
        print("----------------------------------------------------------------------------")
        choice = input("Your choice ? :")
        choice = int(choice)
        return choice

    def prompt_menu_player_db(self):
        print("1. Show all players")
        print("2. Research a player\n")
        choice = input("Choice : ")
        choice = int(choice)
        return choice

    def prompt_new_profile(self):
        print("\nThis player does not exist")
        print("Adding a new profile...\n")


    def prompt_profile_exist(self):
        print("Player found")

    def prompt_all_db_players(self, player, n=0):
        print(
            '-----------------------------------------------------------------------------------------------------\n')
        print(
            f"N° : {n} || Full name : {player['last_name']} {player['first_name']} ||"
            f" Birthday_date : {player['birthday_date']} || Gender {player['gender']} || rank : {player['rank']}")




    def prompt_all_tournaments(self, n, tournament):
        print(
            '-----------------------------------------------------------------------------------------------------')

        print(f"N° {n} || Name : {tournament['name']} || Place : {tournament['place']} || Date : {tournament['date']} ||"
              f" Number of rounds : {tournament['number_of_rounds']} || Time : {tournament['time_control']} ||"
              f" Description : {tournament['description']}\n")



    def prompt_all_rounds(self, index):
        print("-------------------------------------------------------------")
        print(f"Round {str(index + 1)} : ")

    def prompt_all_matchs(self, index, jindex, round):
        print(f"Match {str(jindex + 1)} || Name : "
              f"{round['Round ' + str(index + 1)][jindex]['match ' + str(jindex + 1)][0][0]['last_name']} "
              f"{round['Round ' + str(index + 1)][jindex]['match ' + str(jindex + 1)][0][0]['first_name']} "
              f"( {round['Round ' + str(index + 1)][jindex]['match ' + str(jindex + 1)][1][0]} ) "
              f"|| Name : ",
              f"{round['Round ' + str(index + 1)][jindex]['match ' + str(jindex + 1)][0][1]['last_name']} "
              f"{round['Round ' + str(index + 1)][jindex]['match ' + str(jindex + 1)][0][1]['first_name']} "
              f"( {round['Round ' + str(index + 1)][jindex]['match ' + str(jindex + 1)][1][1]} )")


    def prompt_asking_tournament_name(self):
        return input("Name of the tournament : ")

    def prompt_start_round(self, round, current_time):
        input(f"\nPress enter to start the round {round + 1}\n")

        print(f"Round {round + 1} has started at {current_time}\n")

    def prompt_end_round(self, round, current_time):
        print(f"\nEnd of round {round + 1} at {current_time}\n")

    def prompt_press_enter(self):
        input("\nPress enter to continue")

    def prompt_begin_pairing(self):
        print("Press enter to begin pairing")

    def prompt_for_opponent(self):
        print(f"\nplayer [{pair[0]}] plays against [{pair[1]}]")