students = [["Khalid",12,13],["Mira",15,13],
            ["Zaid",14,11]]
def generate_email(name,y):
  return y(name) + '@uop.edu.jo'
lowerName = lambda s:s[0].lower()
name2 = lambda s:s.lower()

#y= lowerName
print(generate_email('Lana',lowerName))
print(generate_email('Lana',name2))
