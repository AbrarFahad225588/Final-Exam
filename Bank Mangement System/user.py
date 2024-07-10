from abc import ABC
import random
from bank import Bank
class User(ABC):
    def __init__(self, name, email,adress):
        self.name=name
        self.email=email
        self.adress=adress
class AccountHolder(User):
    def __init__(self, name, email, adress,acc_type,pin):
        super().__init__(name, email, adress) 
        self.acc_type=acc_type
        self.pin=pin
        self.loan_take=0
        self.loan_limit=0
        self.current_balance=0
        self.acc_no=random.randint(1000,10000000)
        self.trans_history=[] 
    def deposit(self,bank,amount):
        
        if amount>0:
            self.current_balance+=amount
            bank.total_bank_balance+=amount
            self.trans_history.append(f"Deposit : {amount} tk")
            print(f"You have succesfully deposit : {amount} tk")
        else:
            print('Deposit fail!!! please, Recheck your Amount....')
    def withdraw(self,bank,amount):
        if bank.bankcruft==False:
            if 0<amount<=self.current_balance:
                self.current_balance-=amount
                bank.total_bank_balance-=amount
                self.trans_history.append(f"Withdraw : {amount} tk")
                print(f"You have succesfully Withdarw : {amount} tk")
            elif amount> self.current_balance:
                print("You have not Enough money")
            else:
                print('Withdarw fail!!! please, Recheck your Amount....') 
        else:
            print(f"The {bank.name} is bankcruft !!!!")   
    def check_balance(self):
        print(f"Your current balance {self.current_balance} tk")       
    def transaction_history(self):
        print("***Transaction History****")
        if len(self.trans_history)>0:
            for transaction in self.trans_history:
                print(f'{transaction}')
        else:
            print("There is no Transaction !!!!")  
    def take_loan(self,bank,amount):
        if bank.bankcruft==False:
            if bank.bank_loan_system==True :
                if self.loan_take<2 and amount>0:
                    self.current_balance+=amount
                    bank.total_bank_balance-=amount    
                    bank.total_loan+=1
                    self.loan_take+=1
                    self.trans_history.append(f"Loan : {amount} tk")
                    print(f"You have succesfully Loan : {amount} tk")
                else:
                    print("You can't take loan.Loan limit cross")  
            else:
                 print(f'The {bank.name} ise no loan system !!!')        
        else:
            print(f'The {bank.name} ise bankcrupt !!!')    
    def transfer_money(self,bank,amount,receiver_acc_no)     :
        receiver=None
        receiver_found=False
        for user in bank.users:
            if user.acc_no==receiver_acc_no:
                receiver=user
                receiver_found=True
                break
        if receiver_found:
            if bank.bankcruft==False:
                if 0<amount<=self.current_balance:
                    self.current_balance-=amount
                    receiver.current_balance+=amount
                    print(f"Transfered : {amount} Tk successfully to bank acount : {receiver_acc_no}")
                    print(f"Your current balance : {self.current_balance}")
                elif amount> self.current_balance:
                    print("You have not Enough money")
                else:
                    print('Transfer fail  !!! please, Recheck your Amount....')  
            else:
                 print(f'The {bank.name} ise bankcrupt !!!')  
        else:
            print(f" acc_no : {receiver_acc_no} not found !!!!! ")    
                        
                
               
                    
                  
                      
            
            
            
            
            
            
                  
                
                
                      
              
        
        
