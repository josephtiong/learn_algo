list = ['A','B','C','D']

for i in range(len(list)): #N
    
    for j in list[i:]:     #N-1
        print(list[i]+j)

#total N^2