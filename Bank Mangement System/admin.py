from bank import Bank
from user import AccountHolder
class Admin:
    def __init__(self,name,bank,password) -> None:
        self.bank=bank
        self.name=name
        self.password=password
    def add_user_account(self,name,email,adress,pin,acount_type,bank):
        new_user=AccountHolder(name=name,email=email,pin=pin,acc_type=acount_type,adress=adress)
        bank.users.append(new_user)
        print(f'Welcome {name} !! succesfully create You account***')
        return new_user
    def delete_user_acount(self,acc_no):
        user_find=False
        for user in self.bank.users:
            if user.acc_no==acc_no:
                user_find=True
                print(f"Successfully Deleted account no : {acc_no}")
                self.bank.users.remove(user)
        if not user_find:
            print(f"No acount found !!!")    
    def view_users_acount(self):
        if len(self.bank.users)>0:
            print("*******Users List*********")  
            for user in self.bank.users:
                print(f"\nName : {user.name} Email : {user.email}  Acount Number : {user.acc_no}")
        else:
            print("The bank has no account!!!!!!")      
    def check_bank_balance(self):
        print(f"the {self.bank.name} is have Total : {self.bank.total_bank_balance} tk")   
             
    def check_loan_balance(self):
        print(f"the {self.bank.name} is have Total Loan provide : {self.bank.total_loan} ")   
    
    def loan_status(self,status):
        if status.lower()=="on" or status.lower()=="yes":
            self.bank.bank_loan_system=True  
            print("Loan status succesfully ON")
        elif status.lower()=="no" or status.lower()=="off":
            self.bank.bank_loan_system=False
            print("Loan status succesfully OFF")
        else:
            print("............Wrong status!!!!!!!!!!!!!!!!!!!!")  
    def user_history(self,bank):
        print("*********User History**********")
        for user in bank.users:
            user.transaction_history()
            
            
            
            
            
        
              
                 
            
              
        
            