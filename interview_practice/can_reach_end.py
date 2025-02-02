def can_reach_end(x):
    max_reachable = 0
    curr_idx = 0
    while curr_idx <= max_reachable and max_reachable < len(x) - 1:
        max_reachable = max(max_reachable, curr_idx + x[curr_idx])
        curr_idx += 1
    return max_reachable >= (len(x) - 1)

def min_steps_to_end(x):
    min_steps_per_idx = [-1] * len(x)
    min_steps_per_idx[0] = 0
    max_reachable = 0
    curr_idx = 0
    while curr_idx <= max_reachable and max_reachable < len(x) - 1:
        if x[curr_idx] + curr_idx > max_reachable:
            for i in range(max_reachable + 1, min(len(x), x[curr_idx] + curr_idx + 1)):
                min_steps_per_idx[i] = min_steps_per_idx[curr_idx] + 1
            max_reachable = x[curr_idx] + curr_idx
        curr_idx += 1
    return min_steps_per_idx[-1]

print(min_steps_to_end([3,2,0,0,2,0,1]))