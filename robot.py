from weapon import Weapon

class Robot: 
    def __init__(self,name):
        self.name = name
        self.health = 50
        self.weapon = Weapon('sword', 10)

    def attack(self,dinosour):
        pass
