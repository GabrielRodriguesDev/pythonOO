class Account:
    
    def __init__(self, number):
        self.number = number
        self.total = 0
        
# Conceito de encapsulamento de código, deixamos o atributo "total" para sofrer alterações ou consultas através
# de métodos oque nós trás uma maior confiança sobre o processo. Não devem acessar ou alterar o atributo direto.
    def deposit(self, value):
        self.total += value
        
    def withdraw(self, value):
        self.total -= value
        
    def getTotal(self):
        return self.total