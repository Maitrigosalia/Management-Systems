d={}

def addcontact():
    nm=input("Enter Contact Name : ")
    mb=input("Enter Phone Number : ")
    d[nm]=mb   
    print("Data Added Successfully")
def searchcontact():
    nm=input("Enter Name to search : ")
    if nm in d:
        print("successful")
        print("----------------------------")
        print("Name Exists ")
        print("Mobile Number = ",d[nm])
        print("----------------------------")
        print("Do you want to change mobile number(y/n) : ")
        ch=input()
        if ch =='y':
            val=input("Enter New Mobile Number : ")
            d[nm]=val
        print("Data Update Successfully")
        print("Mobile Number = ",d[nm])
    else:
        print("No Data Found")
def deletecontact():
    nm=input("Enter Name to search : ")
    if nm in d:
        del d[nm]
        print("Data Deleted Successfully")
    else:
        print("No Data Found")
        
def display():
    print("\n"*5)
    print("----------------------------")
    for i,j in d.items():
        print(i,"\t",j)
    print("----------------------------")
    print("\n"*5)
while True:
    print("\nTelephone Directory Management System")
    print("1.Add contact")
    print("2.Search contact")
    print("3.Delete contact")
    print("4.Display contact")
    print("5.Exit")
    ch=eval(input("Enter Your Choice : "))
    if ch==1:
        addcontact()
    elif ch==2:
        searchcontact()
    elif ch==3:
        deletecontact()
    elif ch==4:
        display()
    elif ch==5:
        print("Bye....")
        break
    else:
        print("Invalid Choice")
