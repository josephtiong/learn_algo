from mod import mod
def gcd(a,b):
    while (b !=0):
        remainder = mod(a,b)
        # remainder = a%b
        a=b
        b=remainder
    return a

print(gcd(4851,3003))
