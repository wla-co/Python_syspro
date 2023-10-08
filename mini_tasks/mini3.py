def make_matrice(input_string):
    matrice = []
    line_count = 0
    for line in input_string.split("|"):
        matrice.append([])
        for num in line.split():
            matrice[line_count].append(float(num))
        line_count += 1

    return matrice


# test
a = make_matrice(input())
print(a[0][1])
