class Car: #Classe
    
    x = 'Abcd' # Atributos de classe, está disponivel mesmo com o objeto não insciando é geral para todos os objetos gerados da classe
    
    def __init__(self): #Construtor "self nesse contexto significa que estou acessando a instancia ou seja acessando ao proprio objeto". O que determina que o método é um costrutor é a chamada do __init__
        self.name = 'Gol' # Atributos de instancia, cada instancia pode ter seu atributos
        self.make = 'Volks'
        self.year = 2016
        self.color = 'Silver'
    
    def drive(self): #Métodos de instancia após inciar uma instacia é possivel ter acesso a esse metodo.
        print(self.name + ' started')
        
        
    @staticmethod  #Decorator de método estatico
    def hello():#Metodo estatico que pode ser usado ao instanciar um objeto ou na própria classe porém não tem acesso as informações da instacia portanto não depende da instancia e seus atributos.
        print('Salve rapaziada')
        
        
    @classmethod # Decorator de método da classe
    def show(TAMALUCO):#Método da classe é possue funcionamento parecido com o método estatico, porém tem acesso as informações da classe, como atributos da classe, só é necessário passar o parametro e usalo como no exemplo abaixo, não tem acesso aos atributos da instacia
        print(TAMALUCO.x)        