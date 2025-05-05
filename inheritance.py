# aim:create base class polygon with variable init and getter and setter function. inhertie these var and function to calc area of triangle and squres

# base class 
class polygone:
    __width = None
    __height = None
    
    def set_params(self,h,w):
        self.__height = h
        self.__width = w
    
    def get_height(self):
        return self.__height
    
    def get_width(self):
        return self.__width
    
# derived class square

class squre(polygone):
    def area(self):
        return self.get_height() * self.get_width()
    
# derived class triangle

class triangle(polygone):
    def area(self):
        return self.get_height() * self.get_width() * 1/2
    
sq = squre()
h = int(input('Enter Height :'))
w = int(input('Enter Width :'))
sq.set_params(h,w)
print(sq.area())

tr = triangle()
ht = int(input('Enter Height T:'))
wt = int(input('Enter Width T:'))
tr.set_params(ht,wt)
print(tr.area())
    

    