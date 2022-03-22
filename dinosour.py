class Dinosours:
    def __init__(self,name,attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 50
    
    
    def attack(self,robot):
        robot.health -= self.attack_power

# dino = Dinosours('Julio', 50)
# print(dino.name)

# dino_two = Dinosours('Kia', 10)

# robot_one = Robot('Hiu')
# print(robot_one.name)

# dino_two.attack(robot_one)

