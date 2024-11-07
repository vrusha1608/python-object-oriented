# WAF that replaces all occurences of "java" with "python" in "practice.txt"

with open("E:/devops-projects/python-object-oriented/file-handling/quiz1-output.txt","r") as f:
    data = f.read()
    newData = data.replace("Java","Python")
    print(newData)

with open("E:/devops-projects/python-object-oriented/file-handling/quiz1-output.txt","w") as f:
    f.write(newData)