import numpy as np

def apply_threshold(arr, threshold, replacement_value=-1):

    arr = np.array(arr)

    condition = arr >= threshold

    modified_arr = np.where(condition, replacement_value, arr)

    return modified_arr


v = np.array([1, 2, 3])

result = apply_threshold(v, 2, -20)

print(result)