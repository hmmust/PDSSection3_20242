students = [["Khalid Mahmoud",12,13],["Mira Gassan",15,13],
            ["Zaid Saloum",14,11]]
sort1 = lambda s: s[1]+s[2]
sort2 = lambda s: s[0].split()[1]
#students.sort(key=sort1)
students_s1 = list(sorted(students,key=sort1))
students_s2 = list(sorted(students,key=sort2))
print(students_s1)
print(students_s2)
#str1= "Khalid Mahmoud".split()[1]

