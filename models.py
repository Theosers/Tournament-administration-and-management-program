class Tournament:
    def __init__(self, infos):

        self.name = infos[0]
        self.place = infos[1]
        self.date = infos[2]
        self.number_of_turn = infos[3]
        self.round = infos[4]
        self.number_of_players = infos[5]
        self.time_control = infos[6]
        self.description = infos[7]

        self.players = []


    def serialized_tournament(self):
        return {'name': self.name, 'place': self.place, 'date': self.date,
                'number_of_turn': self.number_of_turn, 'round': self.round, 'players': self.number_of_players,
                'time_control': self.time_control, 'description': self.description}
class Tour:
    def __init__(self):
        self.listedematch = 0

class Match:
    def __init__(self,score_joueur=([],[])):
        self.joueur = score_joueur[0]
        self.score = score_joueur[1]

    def match_results(self,pairingT2):
        matchs = []
        for pair in pairingT2:
            resultat = input("if there is a winner, enter his last_name and first_name, if it is a tie, enter 'tie':")
            #mettre cet input dans le view et l'appeller dans le controller
            if resultat == pair[0][0]:

                match = Match(([pair[0][0], pair[1][0]], [1, 0]))
            elif resultat == pair[1][0]:

                match = Match(([pair[0][0], pair[1][0]], [0, 1]))
            elif resultat == 'tie':
                match = Match(([pair[0][0], pair[1][0]], [0.5, 0.5]))
            else:
                print("error")
            matchs.append((match.joueur, match.score))
        print(matchs)
        return matchs

class Player:
    def __init__(self, infos):

        self.last_name = infos['last_name']
        self.first_name = infos['first_name']
        self.birthday_date = infos['birthday_date']
        self.gender = infos['gender']
        self.rank = int(infos['rank'])

        self.score = 0
    def __str__(self):
        return self.last_name
    def serialized_player(self):
        return {'last_name': self.last_name, 'first_name': self.first_name, 'birthday_date': self.birthday_date,
                'gender': self.gender, 'rank': self.rank}

'''   def add_new_player(self,):
        full_name = self.view.prompt_for_adding_player_to_tournament()
        jou = Query()
        if self.db_players.search(jou.last_name == full_name.split()[0]) == []:
            # crrer un nouveau joueur
            print("ce joueur n'existe pas : creation du nouveau profil")

            player1 = Player(self.view.prompt_for_new_player())
            self.db_players.insert(player1.serialized_player())
        else:
            print("yes")
            # si le joueur existe déjà dans la liste alors erreur, sinon ajouter le joueur
            player1 = self.db_players.get(jou.last_name == full_name.split()[0])
        print(player1.last_name)
        return player1'''

