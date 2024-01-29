
# Online Python - IDE, Editor, Compiler, Interpreter

def power(a, n):
    if n==1:
        return(a)
    #Initially using n==0 return 1. 
    #But n never get to 0 in this algorithm, miss this out, troubleshooted. 

    x = power(a, int(n/2))
    #Using func round(), will get roundup when decimal is more or equal to 0.5 
    #When that happened, the calculation will be wrong
        
    if n%2==0:
        return(x*x)
    else:
        return(a*x*x)
#Always check intermediate value in the algorithm, error carry forwards in the calculation
#Always check a number of cases. For example, this algorithm cannot calculate for power in decimals 
print(power(8,90))