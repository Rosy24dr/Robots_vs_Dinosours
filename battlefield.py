from fleet import Fleet
from herd import Herd
from robot import Robot



class Battlefield:

    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        self.attack = Robot('Loki')
        self.fleet.create_fleet()
        self.herd.create_herd()
        self.robot_result_list = []
        self.dino_result_list = []

    
    def run_game(self):
        pass

    def display_welcome(self):
        print('Welcome to the Robots vs Dinosours battle!!')

    def battle(self):
        print(f"{self.robot_result_list}'s uses {self.robot.weapon} and {self.robot.attack()} {self.dino_result_list}")

    def dino_turn(self,dinosour):
        print(f"It is {dinosour}'s turn.")

    def robo_turn(self,robot):
        print(f"It is {robot}'s turn.")
        
    def show_dino_opponent_options(self):
        self.dino_result_list  = []
        print('These are the dinosours:')
        for dino in self.herd.dinosours:
            print(dino.name)
            self.dino_result_list.append(dino)

    def show_robo_opponent_options(self):
        self.robot_result_list = []
        print('These are the robots:')
        for robot in self.fleet.robots:
            print(robot.name)
            self.robot_result_list.append[robot]

    def display_winners(self):
        pass

welcome_msg = Battlefield()
robot = Battlefield()
dino = Battlefield()

welcome_msg.display_welcome()
dino.show_dino_opponent_options()
robot.show_robo_opponent_options()
dino.dino_turn(dino.herd.dinosours[0].name)
robot.robo_turn(robot.fleet.robots[0].name)