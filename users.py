import re
import csv
import json
import pandas as pd
from admin import Admin

from exception import InvalidNameError, InvalidMobileNumberError, InvalidEmailError, InvalidaddressError, PasswordCheck, InvalidPasswordError
class User:
    def registration():     
        print("*"*20 ,"Enter your details for registration","*"*20)     
        name=str(input("Enter your full name: "))
        res_name=re.findall(r"[A-Z][a-z]",name)
        if res_name:
            mob_no=input("Enter your mobile number: ")
            res_mob_no=re.findall(r"^[1-9]{1}[0-9]{9}$",mob_no)
            if res_mob_no:
                e_mail=input("Enter your E-mail address: ")
                res_e_mail=re.findall(r"^[A-Za-z_+-.0-9]+@[A-Za-z.-]+\.[a-z]{1,3}$",e_mail)
                if res_e_mail:
                    address=input("Enter your address (city,state): ")
                    res_address=re.findall(r"[A-Za-z]+\s+[A-Za-z]",address)
                    if res_address:
                        print("\nPassword should contain atleast 8 characters,\none lowercase,\none uppercase,\none digit,\none special character")
                        passwd=input("Enter your password: ")
                        if PasswordCheck.password_validation(passwd=passwd):
                            print("You are successfully registered!!")
                            print("You can now sign-in using your name and password..")
                            choice=int(input("Whether you want to register as an Admin or an User? \n1. Admin \n2. User\n"))
                            if choice==1:
                                with open("D:\\DS291022B\\Python\\finalproject\\admin.csv","a") as csvfile:
                                    csvwriter=csv.writer(csvfile,lineterminator="\n")
                                    csvwriter.writerow([name,mob_no,e_mail,address])
                                user_profile={"Username":name,"Password":passwd}
                                User.write_admin(user_profile)
                            else:                                
                                with open("D:\\DS291022B\\Python\\finalproject\\Entries.csv","a") as csvfile:
                                    csvwriter=csv.writer(csvfile,lineterminator="\n")
                                    csvwriter.writerow([name,mob_no,e_mail,address])
                                user_profile={"Username":name,"Password":passwd}
                                User.write_json(user_profile)  
                        else:
                            raise InvalidPasswordError           
                    else:
                        raise InvalidaddressError
                else:
                    raise InvalidEmailError
            else:
                raise InvalidMobileNumberError
        else:
            raise InvalidNameError      
       
    def write_admin(new_data,filename="D:\\DS291022B\\Python\\finalproject\\AdminProfile.json"):
        with open(filename,"r+") as file:
            file_data=json.load(file)
            # print(file_data)
            file_data["Admin_profile"].append(new_data)
            # print(file_data)
            file.seek(0)
            json.dump(file_data,file,indent=4)

    def write_json(new_data,filename="D:\\DS291022B\\Python\\finalproject\\UserProfile.json"):
        with open(filename,"r+") as file:
            file_data=json.load(file)
            # print(file_data)
            file_data["User_profile"].append(new_data)
            # print(file_data)
            file.seek(0)
            json.dump(file_data,file,indent=4)

    def user_login():
        print("Please enter your Username here to login...\n")
        user_name=input("Enter Username: ")
        with open(r"D:\DS291022B\Python\finalproject\UserProfile.json") as file:
            data=json.load(file)
            for i in data:
                for j in data["User_profile"]:
                    if user_name == j["Username"]:
                        print("Please enter your password...")
                        password=input("Enter your password: ")
                        if password==j["Password"]:
                            print(f"Welcome {user_name}!! You are successfully logged in!!\n\n")
                            User.execute()
                        else:
                            print("Password do not match")      

    def execute():
        print("*"*10,"Welcome to food ordering","*"*10)
        print("1.Place New Order \n2.View Order History \n3.Update Your Profile")
        print("*"*35)
        print("Please select the option:")
        choice=int(input("Enter the option: "))
        if choice==1:
            User.new_order()
        elif choice==2:
            User.order_history()
        elif choice==3:
            User.update_profile()
        else:
            return True

    def new_order():
        
        df=pd.read_csv("D:\\DS291022B\\Python\\finalproject\\Fooditems.csv",usecols=["Food_ID","Name","Quantity","Price(INR)","Discount(%)"])
        print(df)
        print()
        print("***************Select your favourite dishes from the list above*******************\n")      
        choice=input("Enter the ID of the food items to be ordered separated by comma:  ").split(",")
        for i in choice:
            with open("D:\\DS291022B\\Python\\finalproject\\Fooditems.csv",'r') as csvfile:
                csvdata=csv.reader(csvfile,lineterminator="\n")
                header=next(csvdata)
                for row in csvdata:                      
                    if row[0]==i:                                           
                        print(f"[{i}],[Food Name:{row[1]}][Quantity: {row[2]}][Price: {row[3]}]")                        
                        order=[i,row[1],row[2],row[3]]                        
                        with open("D:\\DS291022B\\Python\\finalproject\\OrderHistory.csv",'a+') as csvfile:
                            csvwriter=csv.writer(csvfile,lineterminator="\n")
                            csvwriter.writerow(order)
        User.execute()

    def order_history():
        print()
        print ("************Ordered food items so far****************")
        print()
        with open("D:\\DS291022B\\Python\\finalproject\\OrderHistory.csv",'r+') as csvfile:
            csvdata=csv.reader(csvfile,lineterminator="\n")
                # print(csvdata)
                # for row in csvdata:
                #     print(row)
            rows=[]           
            for row in csvdata:
                rows.append(row)
            for row in rows:
                for col in row:
                    print("%10s"%col,end=" "),
                print()
        User.execute()

    def update_profile():
        User.read_csv()
        name=input("Enter your name:")
        user_ID=int(input("Enter the row number to be updated (starts from 1): "))
        user_ID-=1
        print("\n\nProfile details subjected to update!\n1.Mobile Number \n2.E-mail ID \n3.Address")
        choice=int(input("Enter your choice:"))                                                                                                 
        if choice==1:           
            mob_no=input("Enter your new mobile number: ")
            res_mob_no=re.findall(r"^[1-9]{1}[0-9]{9}$",mob_no)                    
            if res_mob_no:
                df=pd.read_csv("D:\\DS291022B\\Python\\finalproject\\Entries.csv")
                df.loc[user_ID,"Mobile Number"]=mob_no
                df.to_csv("D:\\DS291022B\\Python\\finalproject\\Entries.csv",index=False)
                User.read_csv()               
                option=int(input("\nYour profile is updated successfully\nWant to edit anything else? \n1. Yes \n2. No\n"))
                if option==1:
                    User.update_profile()
                else:
                    User.execute()                
            else:
                raise InvalidMobileNumberError
        elif choice==2:
            e_mail=(input("Enter your E-mail address: "))
            res_e_mail=re.findall(r"^[A-Za-z_+-.0-9]+@[A-Za-z.-]+\.[a-z]{1,3}$",e_mail)                        
            if res_e_mail:
                df=pd.read_csv("D:\\DS291022B\\Python\\finalproject\\Entries.csv")
                df.loc[user_ID,'E-mail ID']=e_mail
                df.to_csv("D:\\DS291022B\\Python\\finalproject\\Entries.csv",index=False)
                option=int(input("\nYour profile is updated successfully\nWant to edit anything else? \n1. Yes \n2. No\n"))
                if option==1:
                    User.update_profile()
                else:
                    User.execute()  
            else:
                raise InvalidEmailError
        elif choice==3:                        
            address=(input("Enter your address (city,state): "))
            res_address=re.findall(r"[A-Za-z]+\s+[A-Za-z]",address)                            
            if res_address:                                                           
                df=pd.read_csv("D:\\DS291022B\\Python\\finalproject\\Entries.csv")
                df.loc[user_ID,'Address']=address
                df.to_csv("D:\\DS291022B\\Python\\finalproject\\Entries.csv",index=False)
                option=int(input("\nYour profile is updated successfully\nWant to edit anything else? \n1. Yes \n2. No\n"))
                if option==1:
                    User.update_profile()
                else:
                    User.execute()                                                              
            else:
                raise InvalidaddressError  
        else:
            exit()

    def read_csv(filename="D:\\DS291022B\\Python\\finalproject\\Entries.csv"):
           with open(filename,'r') as csvfile:
            csvdata=csv.reader(csvfile,lineterminator="\n")            
            rows=[]
            for row in csvdata:
                rows.append(row)
            for row in rows:
                for col in row:
                    print("%10s"%col,end=" "),
                print("\n")


        

                   