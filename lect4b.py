students = [["Khalid",12,13],["Mira",15,13],
            ["Zaid",14,11]]

student_t = [ [s[0],s[1]+s[2]] for s in students ]
print(student_t)

student_f1 = [ s for s in student_t if s[1]>25]
print(student_f1)

student_f2 = [ s for s in student_t 
              if s[0][0] in ('Z','K')]
print(student_f2)