def mod_power_back(number, power, k):
    
    if power == 1:
        return(number%k)
    
    x = mod_power_back(number, int(power/2), k)
    # print(x)
        
    if power%2==0:
        return(x*x%k)
    else:
        return(number*x*x%k)

def mod_power(number, power, k):
    temp = mod_power_back(number, power, k)
    t1 = None
    while temp > 10:
        t1= temp
        temp = mod_power_back(number, temp-1, temp)
    if temp ==0:
        return t1    
    return temp

if __name__ == "__main__":
    k = mod_power_back(623455,746068747670064760314263134249-1, 746068747670064760314263134249)

    while k > 10:
        k = mod_power_back(623455, k-1, k)
        print(k)

    #print(mod_power(113551343,26904200625-1, 26904200625))
    print(mod_power(623455,746068747670064760314263134249-1, 746068747670064760314263134249))