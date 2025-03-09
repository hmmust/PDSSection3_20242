def calcTotal(m1, m2):
    return m1+m2

students = {"Zaid": [20,20,20], "Khalid":[20,21,19],"Mira":[20,22,20]}

for s in students:
    print(s,students[s])
    
print(students["Khalid"])

for k,v in students.items():
    print(k,v)
    
    