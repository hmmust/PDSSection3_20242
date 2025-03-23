students = [["Khalid",12,13],["Mira",15,13],
            ["Zaid",14,11]]

students_emails = [ s[0].lower()+"@uop.edu.jo" 
                   for s in students]
print(students_emails)