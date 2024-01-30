def mod_power(number, power, k):
    
    if power == 1:
        return(number%k)
    
    x = mod_power(number, int(power/2), k)
    print(x)
        
    if power%2==0:
        return(x*x%k)
    else:
        return(number*x*x%k)

print(mod_power(2,769283283,5))