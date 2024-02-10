"""
Pseudocode:

function: number
list: prime_list
for i starting 2 to number (inclusive)
    if i%2!=0, 
        add i into prime_list
x(prime_list)



function(x): list, index=1
        if len(list)==0
            return list
        if index == len(list)-1
            return list

        if prime_list[0] == 2:
            smallest_prime = prime_list[index]
        if item%smallest_prime==0:
            remove item from prime_list
        if index < len(prime_list)-1
            index=index+1
            x(prime_list,index)

"""

def check(prime_list, index=1):
    
    if len(prime_list)==0:

        return prime_list
    if index >= len(prime_list):

        return prime_list
    
    
    smallest_prime = prime_list[index]
    
    for item in prime_list[index+1:]:
        if item%smallest_prime==0:
            prime_list.remove(item)
    
    
    index=index+1
    
    return check(prime_list, index)


def find_prime(number):
    prime_list = list()
    prime_list.append(2)
    for i in range(2, number+1):
        if i%2!=0:
            prime_list.append(i)
    return check(prime_list)
    
    



print(find_prime(997))
print(len(find_prime(997)))