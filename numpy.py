import numpy as np

arr = np.array([1, 2, 3, 4, 5])

arr[arr % 2 == 0] *= -1

mean = np.mean(arr)
std_dev = np.std(arr)

print("Modified array:", arr)
print("Mean:", mean)
print("Standard deviation:", std_dev)