# WHile Loop

a = 1
while a<=10 :
    print(a)
    a+=1
print("Rest of the Code")

print("------------------------------------------------------------------")

a =2
while a<=20:
    print(a)
    a+=2
print("Rest of the Code")

# While Else loop

a = 6
while a <= 5:
    print(a)
    a+=1
else:
    print("While Loop Condition is False, So Executing Else Block")
    
print("------------------------------------------------------------------")

# while True:
#     print("Infinite Loop")
# print("Rest of the Code")

# Nested While Loop

i = 1
while i <=3:
    print("Outer Loop Iteration:", i)
    i +=1
    j = 1
    while j<=5:
       print("  Inner Loop Iteration:", j)
       j +=1
       
print("Rest of the Code")