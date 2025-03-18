students = [["Khalid",12,13],["Mira",15,13],
            ["Zaid",14,11]]
filter1 = lambda  s: s[1]+s[2] > 25
filter2 = lambda  s: s[0][0].lower() in ('a','k')
students2 = list(filter(filter1,students))
#students2 = [*filter(filter1,students)]
students3 = list(filter(filter2,students))
print(students2,students3)

