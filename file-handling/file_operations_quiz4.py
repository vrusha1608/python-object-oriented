# WAF to find in which line of the file does the word "learning" occur first.
# print -1 if word not found



def find_for_line(word):
    data = True
    line_no = 1
    ans = -1
    with open("E:/devops-projects/python-object-oriented/file-handling/quiz1-output.txt","r") as f:
        while data:
            data = f.readline()
            if (word in data):
                ans = line_no
                break            
            line_no += 1

    return ans


word = "Python"

res = find_for_line(word)

print(res)