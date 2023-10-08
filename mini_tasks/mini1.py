n = int(input())
k = 0

if n >= 0:
    while n:
        k += (n % 2)
        n >>= 1
else:
    # до первой 1 включительно все цифры совпадают, затем все цифры отличаются
    n = abs(n)
    weFacedFirst1 = False
    while n:
        if n % 2:
            weFacedFirst1 = True
        elif weFacedFirst1:
            k += 1
        n >>= 1
    k += 2  # +fist1 and +sign

print(k)
