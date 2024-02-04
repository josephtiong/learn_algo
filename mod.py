def mod(number, m):
    k = int(number/m)
    return number - k*m
if __name__ == "__main__":
    print(mod(148383,5))