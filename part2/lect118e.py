import numpy as np
students= np.array(['Khalid','Lana','Mira','Zaid','Mohammad','Baryhan'])
print(np.random.choice(students))
print(np.random.choice(students,size=2))
print(np.random.choice(students,size=(2,2)))

print(np.random.choice(students,size=(7,2)))
