
a = 10 # Global Variable

def somethig():
    global a # Refers to the Global Variable
    a = 5  # Local Variable
    print(a)


somethig() #prints 5


print(a) #prints 10