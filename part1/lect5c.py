students = [["Khalid",12,13],["Mira",15,13],
            ["Zaid",14,11]]

def sum_marks(student):
  return student[1]+student[2]

sum_marks2 = lambda student:student[1]+student[2]
print(type(sum_marks2),sum_marks2)
print(sum_marks(students[0]))