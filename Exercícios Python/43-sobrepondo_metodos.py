
class Animal():
    
    def comer(self):
        print("Este animal está comendo")

class Coelho(Animal):
    def comer(self):
        print("Este animal está comendo uma cenoura")
    
coelho = Coelho()

coelho.comer()