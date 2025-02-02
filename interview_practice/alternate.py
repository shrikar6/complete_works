def alternate(a):
    increasing = False
    for i in range(len(a) - 1):
        if (increasing and a[i] <= a[i+1]) or (not increasing and a[i] >= a[i+1]):
            temp = a[i]
            a[i] = a[i+1]
            a[i+1] = temp
        increasing = not increasing
    return a