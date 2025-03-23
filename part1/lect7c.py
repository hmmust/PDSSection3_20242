students = [["Khalid Mahmoud",12,13],["Mira Gassan",15,13],
            ["Zaid Saloum",14,11]]
map1 = lambda s: (s[0].replace(" ",'.'),[s[1],s[2]])
students_m1 = dict(map(map1,students))
print(students_m1)

#l1 = dict([('ahmad',[25,12]),("Gassan",[15,15])])
#print(l1)
