from polygone import Polygone

class Square(Polygone):
    def area(self):
        return self.get_height() * self.get_width()