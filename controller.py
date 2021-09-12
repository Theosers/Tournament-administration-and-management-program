from models import *
from tinydb import TinyDB, Query
from faker import Faker
import random


class Controller:
    def __init__(self, View):
        self.view = View
        self.tournament = Tournament
        self.db = TinyDB('tournaments.json', indent=4)
        self.db_tournament_table = self.db.table('tournament')
        self.db_players_table = self.db.table('players')

    def new_Tournament(self):
        tournoi = Tournament(self.view.prompt_for_new_tournament_infos())
        self.db_tournament_table.insert(tournoi.serialized_tournament())

        for number_of_player in range(tournoi.number_of_players):
            self.add_player_to_db(tournoi)
        print(tournoi.rounds)
        for round in range(tournoi.number_of_rounds):
            if round == 0:
                pairing = self.pairing_round_one(tournoi)
            else:
                pairing = self.pairing_others(tournoi, matchs)

            print(pairing)  # dans le view : le joueur a joue contre b, etc
            matchs = self.matchs_results(pairing)
            self.update_player_score(tournoi, matchs)

            print("****************************************")
            r = Round(matchs)
            tournoi.rounds.append(r.serialized_round(round))
        for player in tournoi.players:
            self.view.prompt_for_end_of_tournament(player.last_name, player.score)

        self.db_tournament_table.insert(tournoi.serialized_tournament())

    def add_player_to_db(self, tournoi):

        full_name = self.view.prompt_for_adding_player_to_tournament().split()

        who = Query()
        exist = False
        if self.db_players_table.search(who.last_name == full_name[0]) == [] or \
                self.db_players_table.search(who.first_name == full_name[1]) == []:
            print("ce joueur n'existe pas : creation du nouveau profil")
            self.db_players_table.insert(self.view.prompt_for_new_player())
        else:
            for elem in self.db_players_table.search(who.last_name == full_name[0]):
                for elem2 in self.db_players_table.search(who.first_name == full_name[1]):

                    if (elem['last_name'] == elem2['last_name']) and elem['first_name'] == elem2['first_name']:
                        print("ce joueur existe déjà")
                        exist = True
                        break
            if exist == False:
                print("ce joueur n'existe pas : creation du nouveau profil")
                self.db_players_table.insert(self.view.prompt_for_new_player())

        if tournoi:
            player = Player(self.db_players_table.get(who.last_name == full_name[0] and who.first_name == full_name[1]))
            tournoi.players.append(player)
            tournoi.serialized_players.append(player.serialized_player())

    def pairing_round_one(self, tournoi):
        print(tournoi.players)
        tournoi.players.sort(key=lambda x: x.rank)  # reverse peut se faire sur une ligne : reverse = True
        tournoi.players.reverse()

        strong_players = tournoi.players[:(len(tournoi.players) // 2)]
        weak_players = tournoi.players[(len(tournoi.players) // 2):]

        strong_players_rank = [(player.last_name + ' ' + player.first_name, player.rank) for player in strong_players]
        weak_players_rank = [(player.last_name + ' ' + player.first_name, player.rank) for player in weak_players]

        return list(zip(strong_players_rank, weak_players_rank))

    def pairing_others(self, tournoi, matchs):

        tournoi.players.sort(key=lambda x: x.score, reverse=True)

        pairing = [(player.last_name + ' ' + player.first_name, player.rank) for player in tournoi.players[::2]]
        pairing2 = [(player.last_name + ' ' + player.first_name, player.rank) for player in tournoi.players[1::2]]

        # si j1 deja jouer j2 => J1,j3, si J1,j3 déjà jouer =>

        return (list(zip(pairing, pairing2)))

    def matchs_results(self, pairing):
        matchs = []
        for pair in pairing:
            winner = input("if there is a winner, enter his last_name and first_name, if it is a tie, enter 'tie':")
            # mettre cet input dans le view et l'appeller dans le controller
            if winner == pair[0][0]:

                match = Match(([pair[0][0], pair[1][0]], [1, 0]))
            elif winner == pair[1][0]:

                match = Match(([pair[0][0], pair[1][0]], [0, 1]))
            elif winner == 'tie':
                match = Match(([pair[0][0], pair[1][0]], [0.5, 0.5]))
            else:
                print("error")
            matchs.append((match.joueur, match.score))
        return matchs

    def update_player_score(self, tournoi, matchs):
        for joueur in tournoi.players:
            for match in matchs:

                if (joueur.last_name + ' ' + joueur.first_name) == match[0][0]:
                    joueur.score += match[1][0]
                elif (joueur.last_name + ' ' + joueur.first_name) == match[0][1]:
                    joueur.score += match[1][1]

    def fake_player(self):
        fake = Faker()
        for n in range(100):
            print()
            self.db_players.insert({'last_name': fake.last_name(), 'first_name': fake.first_name(),
                                    'birthday_date': str(random.randint(1, 30)) + '/' + str(
                                        random.randint(1, 12)) + '/' + str(random.randint(1940, 2021)),
                                    'gender': random.choice(['M', 'F']), 'rank': random.randint(1, 2000)})

    def all_db_players(self):

        players = sorted(self.db_players_table.all(), key=lambda x: x['last_name'])
        for n, player in enumerate(players):
            print('n°', n, ':', 'full name : ', player['last_name'], player['first_name'], '||', 'birthday_date :',
                  player['birthday_date'], '||', 'gender', player['gender'], '||', 'rank :', player['rank'])

            print(
                '-----------------------------------------------------------------------------------------------------')

    def one_db_player(self, player):

        try:
            who = Query()
            this_player = self.db_players_table.get(
                who.last_name == player.split(' ')[0] and who.first_name == player.split(' ')[1])
            print('full name : ', this_player['last_name'], this_player['first_name'], '||', 'birthday_date :',
                  this_player['birthday_date'], '||', 'gender', this_player['gender'], '||', 'rank :',
                  this_player['rank'])
        except TypeError:
            print("ce joueur n'exste pas")
