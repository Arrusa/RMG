
def RMG(Empid,Fullname,Contact,list,Grdae,Exp):
    print("Employee Details as below:")
    print(f"MY name is {Fullname}.")
    print(f"Emp id :{Empid}.")
    print(f"Contact Number :{Contact}.")
    print (f"My Skills are as below:" , ','.join(list))
    print(f"Grade: {Grdae}.")
    print(f"Experience: {Exp}.")
   



n =int(input("Enter the number of employe:"))




for i in range(n):
    Empid = int(input("Enter the emp id"))
    Fullname = str(input("Enter the Full name "))
    Contact = int(input("Enter Mobile Number"))
    list =[]
    list= input("Enter elements separated by space: ").split()
    Grdae =  str(input("Enter Your Grade"))
    Exp = input("Enter your Experience")
RMG(Empid,Fullname,Contact,list,Grdae,Exp)



