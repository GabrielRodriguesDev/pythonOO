class Bank1Account(object):
    
    def __init__(self, number):
        self.number = number
        self.__total = 0 #O uso do __ antes do atributo o torna "private" (privado)
        
# Conceito de encapsulamento de código, deixamos o atributo "total" para sofrer alterações ou consultas através
# de métodos oque nós trás uma maior confiança sobre o processo. Não devem acessar ou alterar o atributo direto.
    def deposit(self, value):
        self.__total += value
        
    def withdraw(self, value):
        self.__total -= value
        self._total -= 1
        
    def getTotal(self):
        return self.__total
    
class Bank2Account(Bank1Account):
    
    def __init__(self, number, cvv): # Sobrescrevendo o construtor herdade da class pai adicionando um parametro (Atributo)
        super().__init__(number) #Passando o atributo que precisa ser passado o construtor (__init__) para a classe pai (No caso é o number)
        self.cvv = cvv # Recebendo o atributo novo apenas nessa instancia herda que sobrescreveu o objt


    def withDraw(self, value):
        self._Bank1Account__total -= value # Usando o _"Nome da classe pai" para acessar os atributos "private" da classe pai, pois  Herança não permite acessar os atributos explicitamente
        self._Bank1Account__total -= 2

    