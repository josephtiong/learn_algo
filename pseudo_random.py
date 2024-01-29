import sys
'''
Intructions
----------
1. cd to ~/Codes/python-play
2. "python3 pseudo_random.py" 
3. Followed by any whole numbers as a seed to generate a random number
'''
def pseudo(seed, min=0, max=1, set=False):
    seed = int(seed)
    result = seed
    A = 151346
    B = 326245
    M = 10011136

    fixed_range = 100

    for i in range(100):
        temp = result
        result = (A * result + B )  % M
        fair_result = min + result/M * (max - min)
        # print('Step: ' + str(i) + '; random number: ' + str(result)+ '>>> ' + str(fair_result))
        if temp == result:
            return 0

    if set:
        fair_result = min + result/M * (max + 1 - min)
        if round(fair_result) > max:
            fair_result = fair_result-1
        return round(fair_result)
    else:
        return fair_result
    
# print(pseudo(sys.argv[1]))