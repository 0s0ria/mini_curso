from superclass.exe11 import Funcionario

class Gerente(Funcionario):
    def __init__(self, nome, idade, sexo, loja):
        Funcionario.__init__(self,nome,idade, sexo)
        self.loja = loja


boss = Gerente ('Macena', 68, 'M', 'americanas')

print(boss.loja)
print(boss.nome)
print(boss.sexo)
