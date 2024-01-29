#Calculate surface of a cube N x N x N 

def surfacecube(n):
    return (n * n * 6)

def cubic_edges(n):
    four_pillars = n * 4
    eight_supp = (n-2) * 8
    return (four_pillars+eight_supp)

def layers(n):
    sum =0
    for i in range(n):
        j = i + 1 
        sum = sum + j
    return sum

def sliced_cube(n):
    sum = 0
    for i in range(n):
        j = i + 1
        sum = sum + layers(j)
    return sum

print(sliced_cube(8))