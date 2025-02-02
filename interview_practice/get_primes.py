import math
import matplotlib.pyplot as plt

def get_primes(n):
    is_prime = [True] * n
    is_prime[0] = False
    primes = []
    for i in range(n):
        if not is_prime[i]:
            continue
        curr_num = i + 1
        primes.append(curr_num)
        multiplier = 2
        while curr_num * multiplier <= n:
            is_prime[(curr_num * multiplier) - 1] = False
            multiplier += 1
    return primes

primes = get_primes(10000000)
prime_diffs = [primes[i+1] - primes[i] for i in range(len(primes) - 1)]
avg_sliding_window_size = 10000
avgs = [sum(prime_diffs[(avg_sliding_window_size*i):(avg_sliding_window_size*(i+1))])/len(prime_diffs[(avg_sliding_window_size*i):(avg_sliding_window_size*(i+1))]) for i in range(math.ceil(len(primes)/avg_sliding_window_size))]

plt.plot(prime_diffs)
plt.show()