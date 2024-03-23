def bigMod(number, power, k):
    res = 1 #result

    while (power >0):
        if (power%2==1): #if power is odd
            res = (res*number)%k
            power -=1
            print(power)
        else:
            number = (number *number)%k
            power = power/2
            print(power)
    return res

if __name__ == "__main__":
    
    #k = bigMod(623455,746068747670064760314263134249-1, 746068747670064760314263134249)

    #while k > 10:
    #    k = bigMod(623455, k-1, k)
    #    print(k)


    print(bigMod(623455,746068747670064760314263134249-1, 746068747670064760314263134249))