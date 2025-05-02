class Std: 
    def __init__(self):  # ignored
        self.name = ''
        self.age = 34
        self.roll = 2
        print('init called')
        
    def __init__(self,name):
        print('2 init called',name)
        
    def logs(self,n):
       print(f'Name:{n}')
       print('Age:',self.age)
       print('Roll:',self.roll)
        

s1 = Std('raj')
