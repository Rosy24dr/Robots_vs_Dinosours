from fleet import Fleet
from herd import Herd
from robot import Robot



class Battlefield:

    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        self.fleet.create_fleet()
        self.herd.create_herd()
        
    def run_game(self):
        pass

    def display_welcome(self):
        print('Welcome to the Robots vs Dinosours battle!!')

    def battle(self):
            self.herd.dinosours[0].attack(self.fleet.robots[0])
            print('The dino attacked the robot')
            self.fleet.robots.
            self.fleet.robots[0].attack(self.herd.dinosours[0])
        
        

    def dino_turn(self,dinosour):
        print(f"It is {dinosour}'s turn.")

    def robo_turn(self,robot):
        print(f"It is {robot}'s turn.")
        
    def show_dino_opponent_options(self):
        print('These are the dinosours:')
        for dino in self.herd.dinosours:
            print(dino.name)
          

    def show_robo_opponent_options(self):
        print('These are the robots:')
        for robot in self.fleet.robots:
            print(robot.name)
            
            

    def display_winners(self):
        pass

my_battlefield = Battlefield()

my_battlefield.display_welcome()
my_battlefield.show_dino_opponent_options()
my_battlefield.show_robo_opponent_options()
my_battlefield.dino_turn(my_battlefield.herd.dinosours[0].name)
my_battlefield.robo_turn(my_battlefield.fleet.robots[0].name)
my_battlefield.battle()
