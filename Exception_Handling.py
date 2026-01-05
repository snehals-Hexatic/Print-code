
a = 5
b = 0

try:
    print("Resource Open")
    print(a/b)
    k =int(input("Enter a Number :"))
    print(k)
    
except ZeroDivisionError as e:
    print("Hey, You cannot divide a Number by zero", e)
    
except ValueError as e:
    print("Invaild Input")
    
except Exception as e:
    print("Something went Wrong ....")
        
finally:
     print("Bye")
  