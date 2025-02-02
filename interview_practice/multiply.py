def get_num(num_arr):
    negative = False
    if num_arr[0] < 0:
        negative = True
        num_arr[0] *= -1
    num = 0
    for i in range(len(num_arr)):
        num += num_arr[i] * 10 ** (len(num_arr) - i - 1)
    if negative:
        num *= -1
    return num

def multiply(a, b):
    num_a = get_num(a)
    num_b = get_num(b)

    mul = num_a * num_b
    negative = False
    if mul < 0:
        negative = True
        mul *= -1
    stack = []
    while mul > 0:
        stack.append(mul % 10)
        mul //= 10
    
    mul_arr = []
    while stack:
        mul_arr.append(stack.pop())
    if negative:
        mul_arr[0] *= -1
    return mul_arr

print(multiply([-1, 2, 3], [4, 5, 6]))