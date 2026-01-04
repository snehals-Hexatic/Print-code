
from functools import reduce

nums =[1,2,3,4,5,6,7,8,9,10]

evens =list(filter(lambda x : x%2==0, nums)) #Filter ----->(Select data, function , iterable)

double =list(map(lambda x:x * 2, nums)) # Map ---------->(Transform data, function, iterable)

sum = reduce(lambda x,y: x + y, double) # Reduce ------->(Combine data, function, iterable)

print(evens)
print(double)
print(sum)

