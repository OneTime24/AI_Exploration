

students = [
    {"name":"Ali","cgpa":3.5},
    {"name":"Ahmed","cgpa":2.8},
    {"name":"Bilal","cgpa":3.9},
    {"name":"Usman","cgpa":2.5}
]


names=[std for std in students if std["cgpa"]>3.0]

for std in names:
    print(std["name"],": ",std["cgpa"])