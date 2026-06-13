# 📌 Project: Student Record System (JSON-based)

# You will be able to:

# Add students
# View all students
# Search by roll number
# Save to file
# Load from file




import json

student=[]


def addstd():
    nm=str(input("Enter student name: "))
    roll=str(input("Enter student roll: "))
    gpa=float(input("Enter GPA: "))

    student.append({"name":nm,"roll_number":roll,"gpa":gpa})

def viewstd():

    if len(student)!=0:
        for std in student:
            print(std["name"],": ",std["roll_number"]," : ",std["gpa"])
    else:
        print("No Record found: ") 
def search():
    targ = input("Enter student roll number: ")
    found = False

    for std in student:
        if std["roll_number"].lower() == targ.lower():
            print(std["name"], std["roll_number"], std["gpa"])
            found = True
            break

    if not found:
        print("No student found")

def savef():

    with open("data.json","w") as file:

        json.dump(student,file)

def loadf():
    student.clear()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            student.extend(data)
    except FileNotFoundError:
        print("File not found")


while True:

    print("1. add std\n2. view std\n3. search\n4. save to file\n5. load from a file\n")
    
    ch=int(input("Enter choice: "))

    if(ch==1):
        addstd()
    
    elif(ch==2):
        viewstd()
    elif(ch==3):
        search()

    elif(ch==4):
        savef()
    elif(ch==5):
        loadf()
    elif(ch==6):
        break
    else:
        print("Wrongchouce:")