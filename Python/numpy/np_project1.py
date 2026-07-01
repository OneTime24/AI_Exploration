import numpy as np

# -----------------------------
# Generate Random Student Marks
# -----------------------------
np.random.seed(42)

marks = np.random.randint(0, 101, 100)

print("===== Student Marks =====")
print(marks)

# -----------------------------
# Statistics
# -----------------------------
print("\n===== Statistics =====")

print("Highest Marks :", np.max(marks))
print("Lowest Marks  :", np.min(marks))
print("Average Marks :", np.mean(marks))
print("Total Marks   :", np.sum(marks))
print("Standard Dev. :", np.std(marks))
print("Variance      :", np.var(marks))

# -----------------------------
# Topper & Lowest
# -----------------------------
print("\n===== Topper =====")

topper_index = np.argmax(marks)

print("Topper Index :", topper_index)
print("Topper Marks :", marks[topper_index])

print("\n===== Lowest Student =====")

lowest_index = np.argmin(marks)

print("Lowest Index :", lowest_index)
print("Lowest Marks :", marks[lowest_index])

# -----------------------------
# Boolean Masking
# -----------------------------
passed = marks >= 50
failed = marks < 50
distinction = marks >= 80

print("\n===== Passed Students =====")
print(marks[passed])

print("\n===== Failed Students =====")
print(marks[failed])

print("\n===== Distinction Students =====")
print(marks[distinction])

# -----------------------------
# Counts
# -----------------------------
print("\n===== Counts =====")

print("Passed :", np.sum(passed))
print("Failed :", np.sum(failed))
print("Distinction :", np.sum(distinction))

print("Pass Percentage :",
      (np.sum(passed) / len(marks)) * 100)

# -----------------------------
# Sorting
# -----------------------------
print("\n===== Sorted Marks =====")

print(np.sort(marks))

# -----------------------------
# Unique Values
# -----------------------------
print("\n===== Unique Marks =====")

print(np.unique(marks))

# -----------------------------
# Grace Marks
# -----------------------------
print("\n===== Grace Marks (+5) =====")

new_marks = np.clip(marks + 5, 0, 100)

print(new_marks)

# -----------------------------
# Attendance
# -----------------------------
attendance = np.random.randint(50, 101, 100)

eligible = (attendance >= 75) & (marks >= 50)

print("\n===== Attendance =====")
print(attendance)

print("\n===== Eligible Students =====")
print(marks[eligible])

print("\nTotal Eligible Students :", np.sum(eligible))