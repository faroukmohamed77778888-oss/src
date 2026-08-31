import numpy as np

def secure_reshape_and_stack(data1, data2, new_shape):

    try:
        arr1 = np.array(data1)
        arr2 = np.array(data2)

        reshaped_arr1 = arr1.reshape(new_shape)

        combined_dataset = np.vstack((reshaped_arr1, arr2))

        return combined_dataset

    except ValueError as e:
        raise ValueError(f"Company-grade Error: {e}")


branch_a = [1, 2, 3, 4, 5, 6]

branch_b = [[7, 8, 9],
            [10, 11, 12]]

final_report = secure_reshape_and_stack(branch_a, branch_b, (2, 3))

print(final_report)
print(final_report.shape)