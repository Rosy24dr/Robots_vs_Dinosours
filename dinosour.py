from urllib import robotparser


class Dinosours:
    def __init__(self,name,attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 50
    
    
    def attack(self,robot):
            while self.attack_power <= self.health:
                self.health -= 10
                print(f'The dinosour attacked the{robot.name}')
                return self.health

dino = Dinosours('Julio', 50)
print(dino.name)

dino.attack()