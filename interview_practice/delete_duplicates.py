def delete_duplicates(sorted_arr):
    curr_idx = 0
    curr_idx_to_swap = 0
    while curr_idx < len(sorted_arr):
        if curr_idx == 0 or sorted_arr[curr_idx] != sorted_arr[curr_idx_to_swap - 1]:
            if curr_idx != curr_idx_to_swap:
                sorted_arr[curr_idx_to_swap] = sorted_arr[curr_idx]
            curr_idx_to_swap += 1
        curr_idx += 1
    return sorted_arr[:curr_idx_to_swap]

def delete_nums_from_array(arr, key):
    curr_idx = 0
    curr_idx_to_swap = 0
    while curr_idx < len(arr):
        if arr[curr_idx] != key:
            if curr_idx_to_swap != curr_idx:
                arr[curr_idx_to_swap] = arr[curr_idx]
            curr_idx_to_swap += 1
        curr_idx += 1
    return arr[:curr_idx_to_swap]

def delete_duplicates_beyond_m(sorted_arr, m):
    curr_idx = 0
    curr_idx_to_swap = 0
    count = 1
    while curr_idx < len(sorted_arr):
        if curr_idx == 0 or sorted_arr[curr_idx] != sorted_arr[curr_idx_to_swap - 1]:
            if curr_idx != curr_idx_to_swap:
                sorted_arr[curr_idx_to_swap] = sorted_arr[curr_idx]
            curr_idx_to_swap += 1
            count = 1
        else:
            if count < m:
                curr_idx_to_swap += 1
            count += 1
        curr_idx += 1
    return sorted_arr[:curr_idx_to_swap]


print(delete_duplicates_beyond_m([2,3,5,5,7,11,11,11,13], 3))