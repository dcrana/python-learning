from polygone import Polygone

class Triangle(Polygone) : 
    def area(self) :
        return self.get_height() * self.get_width() * 1/2