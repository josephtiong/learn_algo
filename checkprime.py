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
def checkPrime(number):
    prime_p = 1
    non_prime_p = 1

    while not (prime_p <=0.5**10 or non_prime_p <=0.5**10):
        n = random.randint(1, number)
        if (n**(number-1))%number == 1:
            prime_p = prime_p *0.5
            # print("prime_p = %s" % (prime_p))
        else:
            non_prime_p = non_prime_p*0.5
            # print("non_prime_p = %s" % (non_prime_p))

    
    if prime_p <=0.5**10:
        return ("The number: %s is has a %s chance of being a prime number." % (number, prime_p))
    if non_prime_p <=0.5**10:
        return ("The number: %s is has a %s chance of not being a prime number." % (number, non_prime_p))

print(checkPrime(12))