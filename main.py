from users import User
from admin import Admin

class main():    
        
    def execute(self,option):
        
        if option==1:
            print("*"*20, "Registration", "*"*20)
            User.registration()
        elif option==2:
            print("*"*20, "User Login", "*"*20)
            User.user_login()
        elif option==3:
            print("*"*20, "Admin Login", "*"*20)
            Admin.admin_login()
        else:
            print("Invalid option!! Try again")
        
if __name__=="__main__":
    obj=main()
    
    while True:
        print("\n\n")
        print("*"*20 ,"Welcome to Maha Food Ordering","*"*20)
        print("\n\n")
        print("Please select the option you want to proceed with!!")
        print("1. Sign-up \n2. User Sign-in \n3. Admin Sign-in\n")
        option=int(input("Enter your option:"))
        print("\n\n")
        obj.execute(option)
        
    
   







