
class Computer:
    
    def __init__(self):
        self.name ="Snehal"
        self.age = "22"
        
    def update(self):
        self.age ="28"
        
c1 = Computer()
c2 = Computer()

c1.name ="Pratik"
c1.age ="24"

c1.update()

print(c1.name)
print(c2.name)

print(c1.age)
print(c2.age)


