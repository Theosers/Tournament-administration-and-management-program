from models import *
from tinydb import TinyDB, Query


class Controller:
    def __init__(self, View):
        self.view = View
        self.tournament = Tournament
        self.db_tournament = TinyDB('tournaments.json')
        self.db_players = TinyDB('players.json')

    def new_Tournament(self):
        tournoi = Tournament(self.view.prompt_for_new_tournament_infos())
        self.db_tournament.insert(tournoi.serialized_tournament())

        for number_of_player in range(4):

            full_name = self.view.prompt_for_adding_player_to_tournament()

            jou = Query()
            if self.db_players.search(jou.last_name == full_name.split()[0]) == []:
                print("ce joueur n'existe pas : creation du nouveau profil")
                self.db_players.insert(self.view.prompt_for_new_player().serialized_player())
            player = Player(self.db_players.get(jou.last_name == full_name.split()[0]))
            tournoi.players.append(player)

        # ○	Liste des indices correspondant aux instances du joueur stockées en mémoire.

        pairingT1 = self.pairing(tournoi)
        print(pairingT1)


        match = Match()

        match_results = match.match_results(pairingT1)
        self.scoring(tournoi, match_results)

        print("****************************************")

        pairingT2 = self.pairing2(tournoi, match_results)
        match_results = match.match_results(pairingT2)
        self.scoring(tournoi, match_results)


        pairingT3 = self.pairing2(tournoi, match_results)
        match_results = match.match_results(pairingT3)
        self.scoring(tournoi, match_results)




    def pairing(self, tournoi):

        tournoi.players.sort(key=lambda x: x.rank) #reverse peut se faire sur une ligne : reverse = True
        tournoi.players.reverse()

        strong_players = tournoi.players[:(len(tournoi.players) // 2)]
        weak_players = tournoi.players[(len(tournoi.players) // 2):]

        strong_players_rank = [(player.last_name + ' ' + player.first_name, player.rank) for player in strong_players]
        weak_players_rank = [(player.last_name + ' ' + player.first_name, player.rank) for player in weak_players]

        return list(zip(strong_players_rank, weak_players_rank))

    def pairing2(self, tournoi, matchs):

        tournoi.players.sort(key=lambda x: x.score,reverse=True)

        pairing = [(player.last_name + ' ' + player.first_name, player.rank) for player in tournoi.players[::2]]
        pairing2 = [(player.last_name + ' ' + player.first_name, player.rank) for player in tournoi.players[1::2]]

        #si j1 deja jouer j2 => J1,j3, si J1,j3 déjà jouer =>

        return (list(zip(pairing,pairing2)))

    def scoring(self, tournoi, matchs):
        for joueur in tournoi.players:
            for match in matchs:

                if (joueur.last_name + ' ' + joueur.first_name) == match[0][0]:
                    joueur.score += match[1][0]
                elif (joueur.last_name + ' ' + joueur.first_name) == match[0][1]:
                    joueur.score += match[1][1]

            print(f'le score de {joueur.last_name} est {joueur.score}')

