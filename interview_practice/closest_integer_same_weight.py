def closest_integer_same_weight(x):
    idx = 0
    while x >> idx:
        if ((x >> idx) ^ (x >> (idx + 1))) & 1:
            x ^= 0b11 << idx
            break
        idx += 1
    return x

def closest_integer_same_weight_new(x):
    mask = (x ^ (x - 1 + (2 * (x & 1))))
    x ^= mask ^ (mask >> 2)
    return x

print(closest_integer_same_weight_new(0b101111111) == 0b110111111)