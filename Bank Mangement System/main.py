from user import AccountHolder
from admin import Admin
from bank import Bank

islami_bank=Bank("Isalmi Bank Limited")

admin=Admin("Admin",islami_bank,"admin")
while True:
    print(f"***Welcome to The {islami_bank.name}****")
    print("1.Admin")
    print("2.User")
    print("3.Exit")
    op=int(input("Enter a Option : "))
    if op==1:
        print("********Admin Login Page*******")
        name=input("Enter Admin Name : ")
        password=input("Enter Admin Password : ")
        if name==admin.name and password==admin.password:
            print(" Admin Login Successfully")
        while True:
            print("1.Add User Account")
            print("2.Delete User  Account")
            print("3.View All Users")
            print("4.Check Bank Balance")
            print("5.Check Loan Provide")
            print("6.Loan System ON/OFF")
            print("7.View All User history")
            print("8.Logged Out")
            op=int(input("Enter a Option : "))
            if op==1:
                name=input("Enter User Name : ")
                email=input("Enter User email : ")
                adress=input("Enter User adress : ")
                acount_type=input("Enter User acount_type : ")
                pin=input("Enter User pin : ")
                admin.add_user_account(name,email,adress,pin,acount_type,islami_bank)
            elif op==2:
                acc_no=int(input("Enter User Account Number : "))    
                admin.delete_user_acount(acc_no)
            elif op==3:
                admin.view_users_acount()
                
            elif op==4:
                admin.check_bank_balance()
            elif op==5:
                admin.check_loan_balance()
            elif op==6:
                 stat=input("Enter Status - ON/OFF : ")
                 admin.loan_status(stat)
                 
            elif op==7:
                admin.user_history(islami_bank)
                 
            elif op==8:
                 print("***Admin Logged Out Successfully******")
                 break
            else:
                print("Invalid OPtion !!!!!!!!!!!!!. Enter Valid OPtion >>>>")
    elif op==2:
        print("********User Login Page*******")
        acc_no=int(input("Enter Your Account Number : "))
        pin=input("Enter Your PIN : ")
        user_acc=None
        for user in islami_bank.users:
            user_acc=user
            print(user.acc_no,user.pin)
            if user.acc_no==acc_no and user.pin==pin:
                print("User Login Successfully")
                while True:
                    print("1.Deposit Money")
                    print("2.Withdraw Money")
                    print("3.Check Balance")
                    print("4.Transaction History")
                    print("5.Take Loan")
                    print("6.Transfer Money")
                    print("7.Logged Out")
                    op=int(input("Enter a Option : "))
                    if op==1:
                        amount=int(input("Enter Your Deposit Amount : "))
                        user_acc.deposit(islami_bank,amount)
                    elif op==2:
                        amount=int(input("Enter Your Withdraw Amount : "))
                        user_acc. withdraw(islami_bank,amount)
                    elif op==3:
                        user_acc.check_balance() 
                    elif op==4:
                        user_acc.transaction_history()
                    elif op==5:
                        amount=int(input("Enter Your Loan Amount : "))
                        user_acc.take_loan(islami_bank,amount)
                    elif op==6:
                        acc_no=int(input("Enter Reciver Account Number : "))
                        amount=int(input("Enter Your Transfer Amount : "))
                        user_acc.transfer_money(islami_bank,amount,acc_no)
                    elif op==7:
                        print("User Logged Out Successfully")
                        break
                    else:
                        print("Invalid Option !!!!!!!!. Enter Valid Option >>>>")
            else:
                print("Invalid Account Number or PIN !!!!!!!!. Enter Valid Account") 
    elif op==3:
                        
        print("********Thanks Visited Our Bank Management System ********")  
        break
    else:
        print("Invalid Option !!!!!!!!. Enter Valid Option >>>>")
                        