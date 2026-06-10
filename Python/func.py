


def calc(x):
    if x >= 90:
        return "A"
    elif x >= 80:
        return "B"
    elif x >= 70:
        return "C"
    elif x >= 60:
        return "D"
    else:
        return "F"

x=float(input("Enter Percentage: "))

grade=calc(x)

print("Grade: ", grade)

