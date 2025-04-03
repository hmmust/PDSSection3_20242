from numpy import random
print(int(random.rand()*200+100))
print(round(random.rand()*200+100,2))
print(random.randint(100,300))
print(random.randint(low=100,high=300))
print(random.randint(100,300,size=10))
print(random.randint(100,300,size=(5,5)))
print(random.randint(300))
chars = ['@','.','_','-','$']
print(random.choice(chars,size=(2,2)))

