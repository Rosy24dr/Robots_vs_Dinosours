from dinosour import Dinosours

class Herd: 
    def __init__(self): 
        self.dinosours = []

    def create_herd(self):
        dinosour_one = Dinosours('Ju')
        self.dinosours.append(dinosour_one)

        dinosour_two= Dinosours('Lit')
        self.dinosours.append(dinosour_two)

        dinosour_three = Dinosours('Jake')
        self.dinosours.append(dinosour_three)

