class Std: 
    def __init__(self):
        self.name = 'test'
        self.age = 34
        self.roll = 2
        print('init called')
        
    def logs(self,n):
       print(f'Name:{n}')
       print('Age:',self.age)
       print('Roll:',self.roll)
        

s1 = Std()
s1.logs()