
class Funcionario ():

    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def calcular_salario(self, salario):
        self.salario = int(salario - (salario * 0.05))
        return self.salario
