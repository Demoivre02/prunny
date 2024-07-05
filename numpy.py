import numpy as np

# Given NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Replace all even numbers with their negative values
arr[arr % 2 == 0] *= -1

# Calculate the mean and standard deviation of the array
mean = np.mean(arr)
std_dev = np.std(arr)

print("Modified array:", arr)
print("Mean:", mean)
print("Standard deviation:", std_dev)