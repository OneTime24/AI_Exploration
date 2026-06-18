#ai

import json

class Student:
    def __init__(self, name, roll, gpa):
        self.name = name
        self.roll = roll
        self.gpa = gpa

    def to_dict(self):
        return {
            "name": self.name,
            "roll": self.roll,
            "gpa": self.gpa
        }

    @staticmethod
    def from_dict(data):
        return Student(data["name"], data["roll"], data["gpa"])


class StudentSystem:
    def __init__(self):
        self.students = []

    # ---------- ADD ----------
    def add_student(self):
        name = input("Name: ")
        roll = input("Roll: ")
        gpa = float(input("GPA: "))
        self.students.append(Student(name, roll, gpa))

    # ---------- VIEW ----------
    def view_students(self):
        if not self.students:
            print("No students found")
            return

        for s in self.students:
            print(s.name, s.roll, s.gpa)

    # ---------- SEARCH ----------
    def search_student(self):
        roll = input("Enter roll: ")

        for s in self.students:
            if s.roll == roll:
                print("Found:", s.name, s.roll, s.gpa)
                return

        print("Not found")

    # ---------- UPDATE ----------
    def update_gpa(self):
        roll = input("Enter roll: ")

        for s in self.students:
            if s.roll == roll:
                s.gpa = float(input("New GPA: "))
                print("Updated")
                return

        print("Not found")

    # ---------- SAVE ----------
    def save(self):
        data = [s.to_dict() for s in self.students]

        with open("students.json", "w") as f:
            json.dump(data, f)

        print("Saved successfully")

    # ---------- LOAD ----------
    def load(self):
        try:
            with open("students.json", "r") as f:
                data = json.load(f)

            self.students = [Student.from_dict(d) for d in data]

            print("Loaded successfully")

        except FileNotFoundError:
            print("No file found")


# ---------------- MAIN PROGRAM ----------------

system = StudentSystem()

while True:
    print("""
1. Add Student
2. View Students
3. Search Student
4. Update GPA
5. Save
6. Load
7. Exit
""")

    choice = input("Enter choice: ")

    if choice == "1":
        system.add_student()

    elif choice == "2":
        system.view_students()

    elif choice == "3":
        system.search_student()

    elif choice == "4":
        system.update_gpa()

    elif choice == "5":
        system.save()

    elif choice == "6":
        system.load()

    elif choice == "7":
        break

    else:
        print("Invalid choice")