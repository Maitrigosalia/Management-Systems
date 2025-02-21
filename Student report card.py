#Exam 3
l=[]
l1=[]
l2=[]
for i in range(5):
    Student_name=input("Enter name of student:")
    l.append(Student_name)
for i in range(5):
    marks=eval(input("Enter marks of student :"))
    l1.append(marks)
print(l)
print(l1)
for i in l1:
    if i>=90 and i<=100:
        l2.append("A")
    elif i>=80 and i<=90:
        l2.append("B")
    elif i>=70 and i<=80:
        l2.append("C")
    elif i<=70 and i>=60:
        l2.append("D")
    elif i<60:
        l2.append("E")
print(l2)

print("Name"," ","Marks"," ","Grade")
for i in range(0,5):
    
    print(l[i],"\t",l1[i],"\t",l2[i])
    
