import numpy as np

# Student Marks
marks = np.array([78, 92, 45, 67, 89, 92, 56, 45, 81, 73])

print("Student Marks:")
print(marks)

print("\n----- Statistics -----")

print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))

print("Average Marks:", np.mean(marks))

print("Total Marks:", np.sum(marks))

print("Standard Deviation:", np.std(marks))

print("Variance:", np.var(marks))

print("\n----- Searching -----")

print("Index of Highest Marks:", np.argmax(marks))

print("Index of Lowest Marks:", np.argmin(marks))

print("\n----- Unique Marks -----")

print(np.unique(marks))

print("\n----- Sorting -----")

print("Sorted Marks:")
print(np.sort(marks))

print("\nIndices after Sorting:")
print(np.argsort(marks))


filter_pass=marks[marks>=50]
print(filter_pass)

print(len(filter_pass))
filter_fail=marks[marks<50]
print(len(filter_fail))

for std in filter_pass:
    print((std/160)*100)

