from controller import Controller
from view import View


if __name__ == '__main__':
    view = View()
    control = Controller(view)

    control.menu()
