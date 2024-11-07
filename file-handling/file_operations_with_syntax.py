# File operations with combined file modes and with syntax

with open("E:/devops-projects/python-object-oriented/file-handling/demo.txt","+a") as f:
    print(f.read())
    f.write("Appending new line in the file")
    print(f.read())