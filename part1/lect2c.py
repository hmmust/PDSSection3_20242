def calc_marks(m1,m2):
    return m1+m2,(m1+m2)/2

def calc_marks2(*marks):
    return sum(marks),sum(marks)/len(marks)

sum_marks = calc_marks2(10,20,30,40,70,44)
print(sum_marks)


#m= calc_marks(30,25)
m,n = calc_marks(30,25)
print(m,n)
x,y,_ = 20,30,40
#(x,y,_) = (20,30,40)
z= 50,40
print(x,y,z)    