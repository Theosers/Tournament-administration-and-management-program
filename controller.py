from models import Tournament,Round,Match,Player
from tinydb import TinyDB, Query
from faker import Faker
import random
import time
import sys
from os import system, name

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

class Controller:
    def __init__(self, View):
        self.view = View
        self.tournament = Tournament
        self.db = TinyDB('tournaments.json', indent=4)
        self.db_tournament_table = self.db.table('tournament')
        self.db_players_table = self.db.table('players')

    def new_Tournament(self):
        current_tournament = Tournament(self.view.prompt_for_new_tournament_infos())
        self.db_tournament_table.insert(current_tournament.serialized_tournament())

        for number_of_player in range(current_tournament.number_of_players):
            self.add_player_to_db(current_tournament)
        for round in range(current_tournament.number_of_rounds):


            clear()
            self.view.prompt_begin_pairing()
            if round == 0:
                pairing = self.pairing_round_one(current_tournament)
            else:


                pairing = self.pairing_others(current_tournament, r.matchs)
            for pair in pairing:
                self.view.prompt_for_opponent(pair)

            r = Round(round)

            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            self.view.prompt_start_round(round, current_time)
            clear()
            r.time.append(current_time)

            for index, pair in enumerate(pairing):

                winner = self.view.prompt_for_winner(pair)

                if winner == str(pair[0]):
                    match = Match(([pair[0], pair[1]], [1, 0]))
                    pair[0].score += 1
                elif winner == str(pair[1]):

                    match = Match(([pair[0], pair[1]], [0, 1]))
                    pair[1].score += 1
                elif winner == 'tie':
                    match = Match(([pair[0], pair[1]], [0.5, 0.5]))
                    pair[0].score += 0.5
                    pair[1].score += 0.5
                else:
                    print("error")
                match.name = 'match ' + str(index + 1)

                r.matchs.append(match)


            self.view.prompt_end_round(round,current_time)
            r.time.append(current_time)
            current_tournament.rounds.append(r)
            current_tournament.serialized_rounds.append(r.serialized_round())
            for player in current_tournament.players:
                self.view.prompt_for_end_of_tournament(player.last_name + ' ' + player.first_name, player.score)




        self.view.prompt_press_enter()
        self.db_tournament_table.insert(current_tournament.serialized_tournament())

    def add_player_to_db(self, current_tournament):

        full_name = self.view.prompt_for_asking_player_name().split()

        who = Query()
        exist = False

        for elem in self.db_players_table.search(who.last_name == full_name[0]):
            for elem2 in self.db_players_table.search(who.first_name == full_name[1]):

                if (elem['last_name'] == elem2['last_name']) and elem['first_name'] == elem2['first_name']:
                    this_player = elem
                    self.view.prompt_profile_exist()
                    exist = True
                    break
        if exist == False:
            self.view.prompt_new_profile()
            this_player = self.view.prompt_for_new_player()
            self.db_players_table.insert(this_player)

        if current_tournament:
            player = Player(this_player)
            current_tournament.players.append(player)
            current_tournament.serialized_players.append(player.serialized_player())

    def pairing_round_one(self, current_tournament):

        current_tournament.players.sort(key=lambda x: x.rank)  # reverse peut se faire sur une ligne : reverse = True
        current_tournament.players.reverse()

        strong_players = current_tournament.players[:(len(current_tournament.players) // 2)]
        weak_players = current_tournament.players[(len(current_tournament.players) // 2):]


        return list(zip(strong_players, weak_players))

    def pairing_others(self, current_tournament, matchs):

        current_tournament.players.sort(key=lambda x: x.score, reverse=True)



        pairing = [player for player in current_tournament.players[::2]]
        pairing2 = [player for player in current_tournament.players[1::2]]

        final_pairing = (list(zip(pairing, pairing2)))
        for match in matchs:
            for pair in final_pairing:
                if match.joueur[0] == pair[0] and match.joueur[1] == pair[1]:
                    pass

        # si j1 deja jouer j2 => J1,j3, si J1,j3 déjà jouer =>

        return

    def update_player_score(self, current_tournament, matchs):
        for joueur in current_tournament.players:
            for match in matchs:

                if (joueur.last_name + ' ' + joueur.first_name) == match[0][0]:
                    joueur.score += match[1][0]
                elif (joueur.last_name + ' ' + joueur.first_name) == match[0][1]:
                    joueur.score += match[1][1]

    def fake_player(self):
        fake = Faker()
        for n in range(100):
            self.db_players.insert({'last_name': fake.last_name(), 'first_name': fake.first_name(),
                                    'birthday_date': str(random.randint(1, 30)) + '/' + str(
                                        random.randint(1, 12)) + '/' + str(random.randint(1940, 2021)),
                                    'gender': random.choice(['M', 'F']), 'rank': random.randint(1, 2000)})

    def all_db_players(self):

        players = sorted(self.db_players_table.all(), key=lambda x: x['last_name'])
        for n, player in enumerate(players):
            self.view.prompt_all_db_players(player,n)
        self.view.prompt_press_enter()

    def one_db_player(self, player):

        try:
            who = Query()
            this_player = self.db_players_table.get(
                who.last_name == player.split(' ')[0] and who.first_name == player.split(' ')[1])
            self.view.prompt_all_db_players(this_player)
        except TypeError:
            print("ce joueur n'exste pas")
        self.view.prompt_press_enter()

    def all_tournaments(self):
        tournaments = sorted(self.db_tournament_table.all(), key=lambda x: x['name'])
        for n, tournament in enumerate(tournaments):
            self.view.prompt_all_tournaments(n,tournament)
        self.view.prompt_press_enter()

    def all_round_in_tournament(self):
        tournament = Query()
        while True:
            name = self.view.prompt_asking_tournament_name()
            if self.db_tournament_table.search(tournament.name == name) == []:
                choice = self.view.prompt_all_round_in_tournament_choice()
                if choice == 1:
                    continue
                elif choice == 2:
                    break

            for index, round in enumerate(self.db_tournament_table.get(tournament.name == name)['rounds']):
                self.view.prompt_all_rounds(index)

                for jindex, match in enumerate(round['Round ' + str(index + 1)]):

                    self.view.prompt_all_matchs(index,jindex,round)

            break
        self.view.prompt_press_enter()
    def menu(self):
        clear()
        while True:
            choice = self.view.prompt_menu()
            clear()
            if choice == 1:
                self.new_Tournament()
                clear()
            elif choice == 2:
                self.add_player_to_db(current_tournament=False)
                self.view.prompt_press_enter()
                clear()
            elif choice == 3:
                second_choice = self.view.prompt_menu_player_db()
                if second_choice == 1:
                    self.all_db_players()
                elif second_choice == 2:
                    self.one_db_player(self.view.prompt_for_asking_player_name())
                clear()
            elif choice == 4:
                self.all_tournaments()
                clear()
            elif choice == 5:
                self.all_round_in_tournament()
                clear()
            elif choice == 6:
                break
            else:
                print("error")

    def waitingAnimation(self,n):
        n = n*3
        for _ in range(n):
            _ = _ % 3 + 1
            dots = _ * '.' + (3 - _) * ' '
            sys.stdout.write('\r Waiting ' + dots)
            sys.stdout.flush()
            time.sleep(0.3)