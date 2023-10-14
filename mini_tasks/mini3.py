def make_matrice(input_string):
    matrice = [[float(num) for num in line.split()] for line in input_string.split("|")]
    return matrice


# test
a = make_matrice(input())
print(a)
print(a[0][1])
