import random
students = [["Khalid",12,13],["Mira",15,13],
            ["Zaid",14,11]]
pass_chars = ['_','@','$','.']
students_emails = [ [s[0].lower()+"@uop.edu.jo",
                     s[0][0]+"_"+str(random.randint(1000,9999))] 
                   for s in students]
students_emails = [ [  f"{s[0].lower()}@uop.edu.jo",
                     f"{s[0][0]}{random.choice(pass_chars)}{random.randint(1000,9999)}"] 
                   for s in students]
print(students_emails)