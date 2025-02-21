#Grocery store Inventory Management
def Capstone1():
    name={'Bread':20,'Cheese':44,'Biscuit':90,'Flour':52,'Chocolate':33}
    d={}
    while True:
        print("*****WELCOME TO GROCERY STORE*****")
        print("1.Add a new product")
        print("2.Update product quantity")
        print("3.View Inventory")
        print("4.Generate Reports")
        print("5.Exit")
        a=eval(input("Enter your choice :"))
        if a==1:
            print("**Add a new product**")
            p=eval(input("Enter product :"))
            if p in name:
                print("Error")
            else:
                pr=eval(input("Enter price :"))
                q=eval(input("Enter Quantity :"))
                print("Adding the product in the stock")
                name.update({p:q})
                print(name.items())
                print(name)
        elif a==2:
            print("**Update Product Quantity**")
            k=eval(input("Enter product :"))
            if k in name:
                q1=eval(input("Enter New Quantity :"))
                name.update({k:q1})
                print(name)
            else:
                print("Item not in Menu")
                
        elif a==3:
            print("**View Inventory**")
            print(name)

        elif a==4:
            d1=[]
            print("**Generate Report**")
            for i in sorted(name.values()):
                d1.append(i)
            print(d1)
            for j in name:
                t=pr*q
                print("Inventory",t)
        elif a==5:
            print("Exit")
            break                                            
Capstone1()


