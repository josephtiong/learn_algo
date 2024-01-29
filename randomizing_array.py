import os
os.environ['SEED'] = '2453318469341'

from pseudo_random import pseudo
array = [1,2,3,4,5]
# print(len(array))
# print(pseudo(245331846941, 1, 500,True))
seed = os.getenv('SEED')
def randomArray(array):
    for index in range(len(array)):
        swap = pseudo(seed,0,len(array)-1,True)
        temp = array[index]
        array[index] = array[swap]
        array[swap]=temp
    os.environ['SEED'] = str(pseudo(os.getenv('SEED'),18243942,1238892894,True)) 
    return array

print(randomArray(array))
print(randomArray(array))
print(randomArray(array))
print(randomArray(array))
print(randomArray(array))
print(randomArray(array))
print(randomArray(array))
