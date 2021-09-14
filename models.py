class Tournament:
    def __init__(self, infos):
        self.name = infos[0]
        self.place = infos[1]
        self.date = infos[2]
        self.number_of_rounds = infos[3]
        self.number_of_players = infos[4]
        self.time_control = infos[5]
        self.description = infos[6]

        self.players = []
        self.serialized_players = []
        self.rounds = []
        self.serialized_rounds = []

    def serialized_tournament(self):
        return {'name': self.name, 'place': self.place, 'date': self.date,
                'number_of_rounds': self.number_of_rounds, 'number_of_players': self.number_of_players,
                'time_control': self.time_control, 'description': self.description,
                'players': self.serialized_players, 'rounds': self.serialized_rounds}


class Round:
    def __init__(self, round):
        self.name = 'Round ' + str(round + 1)
        self.matchs = []
        self.time = []

    def serialized_round(self):
        return {self.name: [(match.serialized_match()) for match in self.matchs]}


class Match:
    def __init__(self, score_joueur=([], [])):
        self.joueur = score_joueur[0]
        self.score = score_joueur[1]
        self.name = ''

    def serialized_match(self):
        return {self.name: ([self.joueur[0].serialized_player(), self.joueur[1].serialized_player()], self.score)}


class Player:
    def __init__(self, infos):
        self.last_name = infos['last_name']
        self.first_name = infos['first_name']
        self.birthday_date = infos['birthday_date']
        self.gender = infos['gender']
        self.rank = int(infos['rank'])

        self.score = 0

    def __str__(self):
        return self.last_name + ' ' + self.first_name

    def serialized_player(self):
        return {'last_name': self.last_name, 'first_name': self.first_name, 'birthday_date': self.birthday_date,
                'gender': self.gender, 'rank': self.rank}
