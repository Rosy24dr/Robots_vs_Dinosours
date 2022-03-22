from fleet import Fleet
from herd import Herd
# from robot import Robot

class Battleship:

    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        # self.robot = Robot()
        self.fleet.create_fleet()
        self.herd.create_herd()
        # self.robot.attack()
    
    def run_game(self):
        pass

    def display_welcome(self):
        print('Welcome to the Robots vs Dinosours battle!!')

    def battle(self):
        # self.herd.robot_one.attack(self.dinosour_one)
        # self.herd.robot_two.attack(self.dinosour_two)
        pass
    
    def dino_turn(self,dinosour):
        pass

    def robo_turn(self,robot):
        print(f"It is the {robot}'s turn.")
        
    def show_dino_opponent_options(self):
        for dino in self.herd.dinosours:
            print(dino.name)

    def show_robo_opponent_options(self):
        for robot in self.fleet.robots:
            print(robot.name)

    def display_winners(self):
        pass

welcome_msg = Battleship()
print(welcome_msg.display_welcome())

robot_opponents = Battleship()
print(robot_opponents.show_robo_opponent_options())

dino_opponents = Battleship()
print(dino_opponents.show_dino_opponent_options())

the_robots_turn = Battleship()
print(the_robots_turn.robo_turn(dino_opponents.show_robo_opponent_options[0].name))