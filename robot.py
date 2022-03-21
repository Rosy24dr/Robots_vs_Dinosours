from Robots_vs_Dinosours.weapon import Weapon


from weapon import Weapon

class Robot: 
    def __init__(self,name):
        self.name = name
        self.health = 50
        self.weapon = Weapon()

    def attack(self,dinosour):
        pass
