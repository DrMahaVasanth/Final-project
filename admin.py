import json
import csv
import pandas as pd

class Admin:
    
    def admin_login():
        print("*"*10,"Enter your Admin Credentials","*"*10)
        admin_name=input("Enter your admin name: ")
        password=input("Enter your password: ")
        with open(r"D:\DS291022B\Python\finalproject\AdminProfile.json") as file:
            data=json.load(file)
            for i in data:
                for j in data["Admin_profile"]:
                    if admin_name == j["Username"] and password==j["Password"]:
                            print(f"Welcome {admin_name}!! You are successfully logged in!!\n\n")
                            Admin.execute()

    def execute():        
        choice=int(input("Enter the choice: \n1.Add Food item \n2.View Food items \n3.Update Food items \n4.Remove Food item \n5.Logout\n"))
        if choice==1:
            Admin.add_food()
        elif choice==2:
            Admin.view_food()
        elif choice==3:
            Admin.update_food()
        elif choice==4:
            Admin.remove_food()
        elif choice==5:
            return True
    
    def add_food(): 
        print("**************Add food**********")
        food_name=input("Enter the name of the food:")
        food_quantity=str(input("Enter the quantity:"))
        food_price=float(input("Enter the price of the food(INR):"))
        food_discount=float(input("Enter the (%) discount:"))
        food_stock=int(input("Enter the stock amount of the food:"))
        with open("D:\\DS291022B\\Python\\finalproject\\Fooditems.csv","r+") as csvfile:
            csvdata=csv.reader(csvfile)
            header=next(csvdata)
            i=0
            for row in csvdata:
                i+=1
                # print(row)                
            food_ID=i 
        # print(food_ID) 
        with open("D:\\DS291022B\\Python\\finalproject\\Fooditems.csv","a+") as csvfile:
            csvwriter=csv.writer(csvfile,lineterminator="\n")
            csvwriter.writerow([food_ID,food_name,food_quantity,food_price,food_discount,food_stock]) 
        print("*************Food item is added successfully*************")
        print("*"*50)
        choice=int(input("Want to add one more food items to the list: \n1. Yes \n2. No \n"))
        if choice==1:
            Admin.add_food()
        elif choice==2:
            Admin.execute()

    def update_food():        
        print("*"*10,"Upadating Food details", "*"*10)
        print()
        food_ID=int(input("Enter the ID of the food to be updated:"))
        food_ID+=1
        choice=int(input("What you want to update?\n1.Name \n2.Quantity\n3.Price\n3.Discount\n4.Stock\n"))      
        if choice==1:
            food_name=input("Enter the name of the food:")
            df=pd.read_csv("D:\\DS291022B\\Python\\finalproject\\Fooditems.csv")
            df.loc[food_ID,'Name']=food_name
            df.to_csv("D:\\DS291022B\\Python\\finalproject\\Fooditems.csv",index=False)
            option=int(input("*******Food is updated successfully..**********\n Want to edit any other field:?\n1. Yes\n2. No \n"))
            if option==1:
                Admin.update_food()
            else:
                Admin.execute()
        elif choice==2:
            food_quantity=str(input("Enter the quantity:"))
            df=pd.read_csv("D:\\DS291022B\\Python\\finalproject\\Fooditems.csv")
            df.loc[food_ID,'Quantity']=food_quantity
            df.to_csv("D:\\DS291022B\\Python\\finalproject\\Fooditems.csv",index=False)
            option=int(input("Food is updated successfully..\n Want to edit any other field:?\n1. Yes\n2. No \n"))
            if option==1:
                Admin.update_food()
            else:
                Admin.execute()
        elif choice==3:
            food_price=float(input("Enter the price of the food:"))
            df=pd.read_csv("D:\\DS291022B\\Python\\finalproject\\Fooditems.csv")
            df.loc[food_ID,'Price(INR)']=food_price
            df.to_csv("D:\\DS291022B\\Python\\finalproject\\Fooditems.csv",index=False)
            option=int(input("Food is updated successfully..\n Want to edit any other field:?\n1. Yes\n2. No \n"))
            if option==1:
                Admin.update_food()
            else:
                Admin.execute()
        elif choice==4:
            food_discount=float(input("Enter the (%) discount:"))
            df=pd.read_csv("D:\\DS291022B\\Python\\finalproject\\Fooditems.csv")
            df.loc[food_ID,'Discount(%)']=food_discount
            df.to_csv("D:\\DS291022B\\Python\\finalproject\\Fooditems.csv",index=False)
            option=int(input("Food is updated successfully..\n Want to edit any other field:?\n1. Yes\n2. No \n"))
            if option==1:
                Admin.update_food()
            else:
                Admin.execute() 
        elif choice==5:
            food_stock=int(input("Enter the stock amount of the food:"))
            df=pd.read_csv("D:\\DS291022B\\Python\\finalproject\\Fooditems.csv")
            df.loc[food_ID,'Stock']=food_stock
            df.to_csv("D:\\DS291022B\\Python\\finalproject\\Entries.csv",index=False)
            option=int(input("Food is updated successfully..\n Want to edit any other field:?\n1. Yes\n2. No \n"))
            if option==1:
                Admin.update_food()
            else:
                Admin.execute()
           
    
    def remove_food():
        print("*"*30,"Removing Food details", "*"*30)
        food_ID=int(input("Enter the ID of the food to be deleted:"))
        food_ID-=1
        df=pd.read_csv("D:\\DS291022B\\Python\\finalproject\\Fooditems.csv")
        df.loc[food_ID]=" " 
        df.to_csv("D:\\DS291022B\\Python\\finalproject\\Fooditems.csv",index=False)
        # print(df)
        print("Food is removed successfully")
        Admin.view_food()
    
    def view_food():
        print("*"*30,"List of Food items and their details", "*"*30)
        Admin.read_csv()

    def read_csv(filename="D:\\DS291022B\\Python\\finalproject\\Fooditems.csv"):
        with open(filename,'r') as csvfile:
            csvdata=csv.reader(csvfile)          
            rows=[]           
            for row in csvdata:
                rows.append(row)
            for row in rows:
                for col in row:
                    print("%15s"%col,end=" "),
                print()
        Admin.execute()

       





