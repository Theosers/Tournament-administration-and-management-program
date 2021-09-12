class View:
    def prompt_for_new_tournament_infos(self):
        print(f"A new tournament has begun")
        name = input("Name of this tournament : ")
        place = input("Place of this tournament : ")
        date = input("date : ")
        rounds = input("Number of rounds : ")
        number_of_players = input("Number of players : ")
        time_control = input("Bullet, blitz or rapid tournament ? : ")
        description = input("Enter a quick description of this tournament : ")
        return [name, place, date, int(rounds), int(number_of_players), time_control, description]

    def prompt_for_adding_player_to_tournament(self):
        return input("Veuillez tapez le nom et prénom du joueur à ajouter au tournoi")

    def prompt_for_new_player(self):
        last_name = input("Veuillez entrer last_name")
        first_name = input("first_name")
        birthday_date = input("birthday_date")
        gender = input("gender")
        rank = input("rank")
        new_player_infos = {'last_name': last_name, 'first_name': first_name, 'birthday_date': birthday_date,
                            'gender': gender, 'rank': rank}

        return new_player_infos

    def prompt_for_end_of_tournament(self,joueur, resultats):
        print(f'le score de {joueur} est {resultats}')
