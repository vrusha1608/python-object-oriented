# You are given a list of subjects for students. Assume one classroom is required for one subject.
# How many classrooms are needed by all students

# ["python", "java", "C++","python", "javascript", "java", "python", "java", "C++", "C"]

subjects = ["python", "java", "C++","python", "javascript", "java", "python", "java", "C++", "C"]

subjects_set = {"python", "java", "C++","python", "javascript", "java", "python", "java", "C++", "C"}

print(subjects_set)

print("No of classrooms required is=>",len(subjects_set))
