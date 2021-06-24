class Calculation1:
    def Sum(self, a, b):
     return a + b;


class Calculation2:
    def Multiplication(self, a, b):
        return a * b;


class derived(Calculation1, Calculation2):
    def Divide(self, a, b):
        return a / b;


d = derived()
print(isinstance(d,derived))
print(issubclass(derived,Calculation2))
print(issubclass(Calculation1,Calculation2))
