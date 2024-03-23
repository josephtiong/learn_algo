"""
Pseudocode:
function (number)

prime_probability = 1
non_prime_p = 1
while prime_probability <=0.5^10 or non_prime_p <=0.5^10:
n = randomnumber between 1 and number 
if n^(number-1)%number = 1: prime_probability = prime_probability *0.5
else: non_prime_p = non_prime_p *0.5


close function
"""
import random
from modulus_large_power import mod_power
def checkPrime(number):
    prime_p = 1
   
    while not (prime_p <=0.5**100):
        #n = random.randint(1, number)
        n = random.randrange(1,number)
        
        if mod_power(n, number-1, number) == 1:
            prime_p = prime_p *0.5
            # print("prime_p = %s" % (prime_p))
      

    
    if prime_p <=0.5**10:
        #return ("The number: %s is has a %s chance of being a prime number." % (number, 1- prime_p))
        return True
    return False

def checkPrime2(number, max_tests):
    """this function is incorrect, do not use. """
    
    for i in range(1, max_tests):
        n = random.randrange(1,number)

        if mod_power(n, number-1, number) != 1:
            return False
    return True
    #print(p)
    #print(0.5**(max_tests))
    #a = (1-0.5)**max_tests
    #print(a)
    #if p <=a:
    #    return True
    #else:
    #    return False


    while not (prime_p <=0.5**100 or non_prime_p <=0.5**100):
        #n = random.randint(1, number)
        n = random.randrange(1,number)
        
        if mod_power(n, number-1, number) == 1:
            prime_p = prime_p *0.5
            # print("prime_p = %s" % (prime_p))
        else:
            non_prime_p = non_prime_p*0.5
            # print("non_prime_p = %s" % (non_prime_p))

    
    if prime_p <=0.5**10:
        return ("The number: %s is has a %s chance of being a prime number." % (number, prime_p))
    if non_prime_p <=0.5**10:
        return ("The number: %s is has a %s chance of not being a prime number." % (number, non_prime_p))


if __name__ == "__main__":
    #print(checkPrime(100)) 293089093123317162028407685871
    print(checkPrime2(293089093123317162028407685871,5))