"""
Task (3.1): Create a function named grades that takes marks of a student in one subject as input and prints:
 "Grade A" if marks are at least 90
 "Grade B" if marks are at least 75
 "Grade C" if marks secured are at least 40
 "Fail" otherwise
Task (3.2): Given an integer list as input that represents marks of a student in 5 subjects. Use grades function from Task 3.1 that prints marks of student in each subject. [78,75,40,39,99]
"""

def Grades(n):
  if n>=90:
    return "Grade A"
  elif n>=75:
    return "Grade B"
  elif n>=40:
    return "Grade C"
  else:
    return "Fail"

ls = [78,75,40,39,99]
ln = len(ls)
for i in range(0,ln):
  e = ls[i]
  print(f"Subject#{i+1}: {Grades(e)}")
  