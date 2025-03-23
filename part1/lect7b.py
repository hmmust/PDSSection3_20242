students = [["Khalid Mahmoud",12,13],["Mira Gassan",15,13],
            ["Zaid Saloum",14,11]]
map1 = lambda s: [s[0],s[1]+s[2]]
students_m1 = list(map(map1,students))
#students_m1 = list(map(lambda s: [s[0],s[1]+s[2]],students))
students_m2 = list(map(lambda s:
    [s[0].lower().replace(" ",".")+"@uop.edu.jo",
     s[1]+s[2]],students))
print(students_m1)
print(students_m2)

#str1= "Khalid Mahmoud".lower().replace(" ",".")+"@uop.edu.jo"
#print(str1)
