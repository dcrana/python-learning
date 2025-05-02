# encapsulation = restrict access of methods and variables outside class using private and getter and setter methods

class encaps : 
    def __init__(self):
        self.speed = 10 
        self.__newSpeed = 20 #private data
        print(self.__newSpeed)
        self.__private_funcyion()
        
    # getter
    def get_speed_value(self):
        return self.__newSpeed
    # setter
    def set_speed_value(self,value):
        self.__newSpeed = value
        
    def __private_funcyion(self):
        print('private')
        
    
obj = encaps()
# print(obj.speed)
# print(obj.get_speed_value())
# obj.set_speed_value(1900)
# print(obj.get_speed_value())
# obj.__private_funcyion()
