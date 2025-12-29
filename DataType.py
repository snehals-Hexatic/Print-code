#Integer
y=10
print(y)

print(id(y))
print(type(y)) # Data type of y is int

print("------------------------------------------------------------------")

#Float
price=99.99
print(price)

print(id(price))
print(type(price)) # Data type of price is float

print("------------------------------------------------------------------")

#Complex

com = 5+7j
print(com)

print(id(com))
print(type(com)) # Data type of com is complex

print("------------------------------------------------------------------")
 #String
 
str1 = "Snehal"
print(str1)

print(id(str1))
print(type(str1)) # Data type of str1 is string

print("------------------------------------------------------------------")
# Lists

data =[1,'love',99.99,5+7j]
print(data)

print(id(data))
print(type(data)) # Data type of data is list
print(data[1])

data[2] = "Python"
print(data)

print("------------------------------------------------------------------")
# Tuple

data1=(1,'love',99.99,5+7j)
print(data1)

print(id(data1))
print(type(data1)) # Data type of data1 is tuple
print(data1[1])

print("------------------------------------------------------------------")
# Range

data2=range(1,10)
print(data2)

print(id(data2))
print(type(data2)) # Data type of data2 is range
print(data2[1])

print("------------------------------------------------------------------")
# Sets

data3={1,'love',99.99,5+7j}
print(data3)

print(id(data3))
print(type(data3))

print("------------------------------------------------------------------")
# MApping Type

data4={'name':'Snehal','age':24,'City':'Pune'}
print(data4)

print(data4['name'])
print(id(data4))
print(type(data4))