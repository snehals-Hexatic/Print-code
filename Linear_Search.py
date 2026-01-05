
pos =-1
def search(list,n):
    i = 0
    
    while i< len(list):
        if list[i] == n:
            globals() ['pos'] =i
            return True
        i = i + 1
    return False
    
list =[5,6,7,9,2,13,5,6,56,34,12]

n = 34

if search(list,n):
    print("Found Element at :",pos)
else:
    print("Not Found")