def reverse_digits(x):
    is_negative = False
    if x < 0:
        is_negative = True
        x *= -1
    y = 0
    while x:
        y *= 10
        y += x % 10
        x //= 10
    return y * (1 - (2*is_negative))

x = -413
print(reverse_digits(x))
print(x)