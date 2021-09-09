from models import *
from controller import *
from view import *

if __name__ == '__main__':
    view = View()
    Newplayer = Controller(view)
    Newplayer.new_Tournament()
# model


"""class Tournament(self) :

Nom, Lieu, Date, nombre de tour(defaut=4), tournées (liste des instances rondes),
Joueurs(○	Liste des indices correspondant aux instances du joueur stockées en mémoire);
controle du temps (○	Cest toujours un bullet, un blitz ou un coup rapide.), description(○	Les remarques générales du directeur du tournoi vont ici.)


"""
