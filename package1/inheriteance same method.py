class Calculation1:
    def Sum(self, a, b):
     return a + b;


class Calculation2:
    def Sum(self, a, b):
        return a * b;


class derived(Calculation1, Calculation2):
    def Divide(self, a, b):
        return a / b;


d = derived()
print(d.Sum(10, 20))

print(d.Divide(10, 20))
