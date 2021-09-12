from models import *
from controller import *
from view import *

if __name__ == '__main__':
    view = View()
    control = Controller(view)

    control.menu()


