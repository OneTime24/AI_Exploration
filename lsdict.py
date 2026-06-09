

students=[
    {"name":"Alice","age":20,"grade":"A","marks":90},
    {"name":"Bob","age":22,"grade":"B","marks":80},
    {"name":"Charlie","age":21,"grade":"A","marks":85},
]

print(students[0]["name"])

for std in students:
    print(f"{std['name']} is {std['age']} years old and got grade {std['grade']}.") # WHAT F STRING DOES is it allows you to embed expressions inside string literals, using curly braces {}. The expressions are evaluated at runtime and then formatted using the __format__ protocol. This makes it easier to create strings that include variable values or expressions without needing to concatenate strings or use the older % formatting method.
    # print(std["name"]," is ",std["age"]," years old and got grade ",std["grade"],".")   # the diffrence 

students.append({"name":"David","age":23,"grade":"C","marks":70})
students.append({"name":"Eve","age":20,"grade":"B","marks":75})

print(students)

max_std=students[0]
for std in students:
    if std["marks"] >= max_std["marks"]:
        max_std=std
    
print("The highest marks is ",max_std["marks"]," and the student is ",max_std["name"])