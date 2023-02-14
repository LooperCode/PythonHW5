def summa (a, b):
    if b == 0:
        return a
    return summa(a+1, b-1) 
    
        
    

a = int(input("first: "))
b = int(input("second: "))
print(summa(a, b))
    
    
    