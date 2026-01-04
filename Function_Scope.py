
a = 10 # Global Variable

def somethig():
    global a
    a = 5  # Local Variable
    print(a)


somethig() #prints 5


print(a) #prints 10