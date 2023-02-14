def Degree (a, b, result):
    if b == 1:
        return result
    result*=a
    return Degree(a, b - 1, result)


a = int(input("first: "))
b = int(input("scnd: "))
result = a
print(Degree(a,b,result))