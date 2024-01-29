#Calculate surface of a cube N x N x N 

def surfacecube(n):
    return (n * n * 6)

def cubic_edges(n):
    four_pillars = n * 4
    eight_supp = (n-2) * 8
    return (four_pillars+eight_supp)

print(cubic_edges(5))