
class Laptop:
    def code(self):
        print("Coding")

class Mobile:
    def code(self):
        print("Mobile Coding")
        
def developer(device):
    device.code()
    
    
developer(Laptop())
developer(Mobile())
