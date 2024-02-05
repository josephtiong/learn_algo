from math import sqrt
def find_prime(number):
    prime_factors = list()

    while (number % 2 == 0):
        prime_factors.append(2)
        number = number/2

    candidate = 3
    max_factor = sqrt(number)
    while (candidate <=max_factor):
        while (number % candidate ==0):
            prime_factors.append(candidate)

            number = number/candidate

            max_factor = sqrt(number)

        candidate = candidate +2

    if (number >1):
        # print("Last number")
        prime_factors.append(int(number))

    return prime_factors

print(find_prime(786))