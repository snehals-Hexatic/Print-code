
# Append function

from array import *
stu_roll = array('i',[101,102,103,104,105])
n = len(stu_roll)
i = 0
while( i < n):
    print(stu_roll[i])
    i+=1
    
print("Array After Append")
stu_roll.append(106)
n = len(stu_roll)
i = 0
while( i < n):
    print(stu_roll[i])
    i+=1
    
print("------------------------------------------------------------------")
print("------------------------------------------------------------------")

from array import *
stu_roll = array('i',[])

n = int(input("Enter Number of Elements :"))

for i in range(n):
    stu_roll.append(int(input("Enter Element :")))
    
for i in range(len(stu_roll)):
    print(stu_roll[i])
    
    
print("------------------------------------------------------------------")
print("------------------------------------------------------------------")

    
    
    
    

    



