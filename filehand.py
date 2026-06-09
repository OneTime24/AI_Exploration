

with open("file.txt","w") as f:
    f.write("hellow world")
    f.write("\nThis is a new line.")
    f.write("\nThis is another line.")

with open("file.txt","r") as f:
    content=f.read()
    print(content)


file=open("file.txt","r")

content=file.read()
print(content)
file.seek(0) # to move the file pointer back to the beginning of the file
l1=file.readline()
l2=file.readline()
print(l1)
print(l2)

file.seek(0)
line=file.readlines()
print(line)

file.close()