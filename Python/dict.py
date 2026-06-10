

student= {
    "name":"ali",
    "age":20
}

# print(student)


for key in student.keys():
    print(key)

for value in student.values():
    print(value)    

student["marks"]=90

print(student)

del student["age"]
print(student)

for key, value in student.items():
    print(key,"|",value)