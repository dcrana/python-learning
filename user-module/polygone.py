class Polygone :
    __width = None
    __height = None
    
    def set_value(self,h,w) :
        print(h,w)
        self.__height = h
        self.__width = w
        
    def get_height(self) : 
        return self.__height
    
    def get_width(self) : 
        return self.__width
    
    