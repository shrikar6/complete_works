def swap_bits(x, i, j):
    if ((x >> i) ^ (x >> j)) & 1 == 0:
        return x
    mask = 0
    mask = mask | (1 << i) | (1 << j)
    x ^= mask
    return x

print(swap_bits(0b101010011110100101, 4, 7) == 0b101010011100110101)