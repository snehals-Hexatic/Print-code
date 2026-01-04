
from re import sub


def greet():
    print("Hello Snehal")
    print("Welcome to Hexatic Private Limited")

greet()
print("-----------------------------------------------------------------")
greet()


print("-----------------------------------------------------------------")
def add(x,y):
    c = x + y
    print(c)
    
add(10, 20)

print("-----------------------------------------------------------------")

def add_sub(a,b):
    c = a + b
    d = a - b

    print(c)
    print(d)
add_sub(50,20)

print("-----------------------------------------------------------------")

def update(x):
    print(id(x))
    x=8
    print(x)
    
a=10
update(10)
print(id(a))
print(a)

    