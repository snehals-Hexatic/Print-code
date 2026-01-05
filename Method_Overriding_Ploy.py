
class Animal:
    def sound(self):
        print("Animal Makes Sound")
        
class Dog(Animal):
    def sound(self):
        print("Dog Barks")
        
class Cat(Animal):
    def sound(self):
        print("Cat Meows")
        
animal =[Dog(), Cat()]

for a in animal:
    a.sound()