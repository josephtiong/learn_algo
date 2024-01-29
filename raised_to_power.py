import time
def raisedToPower(integer, power):
    for i in range(0,power,2):
        if i == 0:
            i = 1
        
        if i < power:
            last=integer
            integer = integer**i
            print(integer)
        elif i == power:
            integer = integer
            print(integer)


def raisedToPowerImproved(integer, power):
    array = dict()
    last = integer
    for i in range(0,int(power/2)+1,2):
        
        print(i)
        if i == 0:
            i = 1
            array[i] = integer

        if i < power:
            ans = integer**i
            array[i] = ans
            
            print(i , " produces: ", ans)

        if i == power:
            ans = integer
            array[i] = ans
            print('when')
            print(i , " produces: ", ans)


def raised(integer, power):
    array = dict()
    i = 0
    while i <= power:
        print(integer**i)
        array[i]=integer**i
        i = i+ 1

    print(array.get(i))


# start  = time.perf_counter()
# raisedToPowerImproved(2,17)
# stop = time.perf_counter()

# print("Time run: " + str(stop-start) + " seconds.")

# raisedToPower(2,8)
# raisedToPowerImproved(2,50)
print(2**1000000)
# raised(2,8)
