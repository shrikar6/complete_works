def reverse_bits(n):
    result = 0
    while n:
        if n & 1:
            result |= 1
        result <<= 1
        n >>= 1
    return result >> 1

print(reverse_bits(938457) == 637095)