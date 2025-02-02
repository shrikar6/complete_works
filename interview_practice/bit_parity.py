def bit_parity(x):
    parity = False
    while x:
        if x & 1:
            parity = not parity
        x >>= 1
    return parity

print(bit_parity(0b10110010101011))