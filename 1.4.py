X = [3, 4, 56, 100, 15, 2, 20, 30]
Y = 1
for x in X:
    if x % 3 == 0 and x % 5 == 0:
        Y *= x
print(Y)