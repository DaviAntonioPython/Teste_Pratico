class Calculadora(object):
    def __init__(self, num1, num2, op):
        self.numero_1 = num1

        self.numero_2 = num2

        self.operação = op

    def Calcular(self):
        if self.operação == '+':
            print(self.Somar())
        elif self.operação == '-':
            print(self.Subtrair())
        elif self.operação == '*':
            print(self.Multiplicar())
        elif self.operação == '/':
            print(self.Dividir())

    def Somar(self):
        return self.numero_1 + self.numero_2
    
    def Subtrair(self):
        return self.numero_1 - self.numero_2

    def Multiplicar(self):
        return self.numero_1 * self.numero_2

    def Dividir(self):
        return self.numero_1 / self.numero_2

operação = str(input(': '))

input_num1 = float(input(': '))

input_num2 = float(input(': '))

calculadora = Calculadora(input_num1, input_num2, operação)

calculadora.Calcular()