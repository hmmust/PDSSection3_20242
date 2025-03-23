import random
students = {"Khalid":[12,13],"Mira":[15,13],"Zaid":[14,11]}
students2 = dict(map(lambda s: (s[0],s[1][0]+s[1][1]),students.items()))
print(students2)
students3 = dict(map(lambda s: (
    f"{s[0].lower()}@uop.edu.jo",
    f"{s[0][0].lower()}{random.randint(100,999)}"
    ),students.items()))
print(students3)

"""m1 = lambda s: (s[0],s[1][0]+s[1][1])
for s in students.items():
    print(m1(s))"""