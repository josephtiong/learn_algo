def gcd(a,b):
    while (b !=0):
        remainder = a%b
        a=b
        b=remainder
    return a

print(gcd(10230,200))
