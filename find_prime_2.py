"""
This is the example algorithm in the textbook.
Different approach used c.f. find_prime.py
"""
from math import sqrt

def FindPrime(max_number):
    #Allocate a list to store Boolean (True if not prime, False if prime) up to the max_number
    is_composite = [False]*max_number

    for i in range(4, max_number, 2):
        is_composite[i] = True

    next_prime = 3
    stop_at = sqrt(max_number)
    while next_prime<stop_at:
        for i in range(next_prime*2, max_number, next_prime):
            is_composite[i] = True

        next_prime = next_prime + 2

        while (next_prime<=max_number) and (is_composite[next_prime]):
            next_prime = next_prime +2

    prime = list()
    for i in range(2, max_number):
        if not is_composite[i]:
            prime.append(i)
    return prime

print(FindPrime(100))