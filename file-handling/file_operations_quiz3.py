# Search if the word "learning" exists in the file or not


word = "learning"


with open("E:/devops-projects/python-object-oriented/file-handling/quiz1-output.txt", "r") as f:
    data = f.read()
    
    if (data.find(word) != -1):
        print("found!")
    else:
        print("not found!")