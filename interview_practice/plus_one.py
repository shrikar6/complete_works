def plus_one(x):
    i = len(x) - 1
    while i >= 0:
        if x[i] == 9:
            x[i] = 0
            i -= 1
        else:
            x[i] += 1
            break
    if i == -1:
        x[0] = 1
        x.append(0)
    return x

print(plus_one([9]))