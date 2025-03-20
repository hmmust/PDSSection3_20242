import random
import sys
print(sys.argv)
student=sys.argv[1]
username= f"{student.lower()}@uop.edu.jo",
password = f"{student[0].lower()}{random.randint(100,999)}"
print(username,password)