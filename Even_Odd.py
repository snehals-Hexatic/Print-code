

def count(lst):
    even =0
    odd = 0
    for i in lst:
        if i%2 ==0:
            even+=1
        else:
            odd+=1
    return even, odd

lst =[10,21,4,45,66,93,11,70,34,23]
even, odd =count(lst)
print("Even numbers:", even)
print("Odd numbers:", odd)