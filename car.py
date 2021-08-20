class Car: 
    
    x = 'Sou atributo da classe não do objeto' 
    
    def __init__(self, name, make, year, color):
        self.name = name
        self.make = make
        self.year = year
        self.color = color
         
    def drive(self):
        print(self.name + ' started')
    
    @staticmethod        
    def hello():
        print('Salve rapaziada')
        
    @classmethod        
    def show(cls):
        print(cls.x)