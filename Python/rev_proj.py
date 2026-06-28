def create_student(name, *marks, **info):

    print("Name:", name)

    print("\nMarks:")

    for mark in marks:
        print(mark)

    print("\nExtra Information:")

    for key, value in info.items():
        print(key, ":", value)

create_student(
    "Ali",
    85,
    90,
    78,
    city="Lahore",
    cgpa=3.7,
    semester=3
)