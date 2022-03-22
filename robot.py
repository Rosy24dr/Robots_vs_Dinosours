from weapon import Weapon

class Robot: 
    def __init__(self,name):
        self.name = name
        self.health = 50
        self.weapon = Weapon('sword', 10)

    def attack(self,dinosour):
        dinosour.health -= self.weapon.attack_power


# dino_one = Dinosours('Luis', 10)
# robot_one = Robot('Jiu')

# robot_one.attack(dino_one)