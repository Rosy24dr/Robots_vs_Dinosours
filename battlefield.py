from fleet import Fleet
from herd import Herd

class Battleship:

    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
    
    def run_game(self):
        pass

    def display_welcome(self):
        print('Welcome to the Robots vs Dinosours battle!!')

    def battle(self):
        pass
    
    def dino_turn(self,dinosour):
        pass

    def robo_turn(self,robot):
        pass

    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winners(self):
        pass

display = Battleship()
print(display.display_welcome())