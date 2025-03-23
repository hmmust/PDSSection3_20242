import random
students = [["Khalid",12,13],["Mira",15,13],
            ["Zaid",14,11]]
#{'khalid': ['khalid@uop.edu.jo', 'K@8178'], ...  }
students_emails = { s[0].lower() : 
                  [ f"{s[0].lower()}@uop.edu.jo",
                     f"{s[0][0]}_{random.randint(1000,9999)}"] 
                   for s in students}
print(students_emails)
print(students_emails['khalid'])