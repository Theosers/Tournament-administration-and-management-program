class View:
    def prompt_for_new_tournament_infos(self):
        print(f"Un nouveau tournoi commence")
        name = input("Nom du tournoi")
        place = input("endroit du tournoi")
        Date = input("date")
        number_of_turn = '4'
        round = input("nombre de rondes")  #○	La liste des instances rondes.
        players = '8' #○	Liste des indices correspondant aux instances du joueur stockées en mémoire.
        time_control = input("temps choisi") #○	C'est toujours un bullet, un blitz ou un coup rapide.
        description = input("description")
        new_tournament_infos = [name,place,Date,number_of_turn,round,players,time_control,description]

        return new_tournament_infos

    def prompt_for_adding_player_to_tournament(self):
        return input("Veuillez tapez le nom et prénom du joueur à ajouter au tournoi")

    def prompt_for_new_player(self):

        last_name = input("Veuillez entrer last_name")
        first_name = input("first_name")
        birthday_date = input("birthday_date")
        gender = input("gender")
        rank = input("rank")
        new_player_infos = [last_name,first_name,birthday_date,gender,rank]

        return new_player_infos
