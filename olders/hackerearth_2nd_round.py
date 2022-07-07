def find_pow(x, y):
    if y == 0 :
        return 1
    if y == 1:
        return x
    mult = 1
    for i in range(y):
        mult = mult*x
    return mult


print(find_pow(4,3))