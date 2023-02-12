#!/usr/bin/env python
# coding: utf-8

# In[3]:


from AccountClass import Account
from CustomerClass import Customer
import random as random
import json
class Bank:
    def __init__(self):
        self.customerList = []
        self.currentCustomer = None
                   
    def log_in(self, userName, passWord):
        for customer in self.customerList:
            if userName == customer.get_customer_name() and passWord == customer.get_customer_password():
                self.currentCustomer = customer
                print(f"You logged in to {self.currentCustomer.get_customer_name()}'s account")
                return
            
        print("Wrong username or password!")

    def log_out(self):
        if self.currentCustomer == None:
            print("You are not logged in to an account")
        else:
            print(f"Logged out from {self.currentCustomer.get_customer_name()}'s account")
            self.currentCustomer = None
            
    def add_customer(self, name, password):
        self.name = name
        self.password = password
        customer = Customer(self.name, self.password)
        self.customerList.append(Customer(customer.name, customer.password))
        print(f"Added new customer to bank \nUsername: {self.name} \nPassword: {self.password}")
        
    def remove_customer(self, nameInput):
        for name in self.customerList:
            if nameInput == name.get_customer_name():
                self.customerList.remove(name)
                print(f"removed customer: {nameInput}")
                return
        print(f"'{nameInput}' does not exist in our customer database. Can not delete")
        
            
    def get_customers(self):
        if len(self.customerList) > 0:
            i = 1
            print("List of bank customers \n")
            for customer in self.customerList:
                print(f"customer {i}: {customer.name}")
                i += 1
        else:
            print("Bank has no customers")
            
    def get_customer(self):
        for customer in self.customerList:
                print(f"Customer username: {self.currentCustomer.get_customer_name()} \nPassword: {self.currentCustomer.get_customer_password()}")
                self.get_all_accounts_and_balances()
                return
        
    def change_password(self, nameInput, newPassword):
        for customer in self.customerList:
            if nameInput == customer.get_customer_name():
                customer.password = newPassword
                return True
        
        print("Wrong username!")
        


        
        
    def add_account_to_customer(self):
        randomAccNumber = random.randint(1,100)
        self.currentCustomer.used_numbers.append(randomAccNumber)
        if self.currentCustomer.used_numbers.count(randomAccNumber) > 1:
            print("account number already exists, try again")
            return
        else:
            self.currentCustomer.accountList.append(Account(randomAccNumber, 0))
            print(f"You just added a new account with account number: {randomAccNumber} \ncurrent balance: {0}$ ")


        
    def get_all_accounts(self):
        if len(self.currentCustomer.accountList) > 0:
            i = 1
            for accounts in self.currentCustomer.accountList:
                print(f"Account {i}: {accounts.get_accountNumber()}")
                i += 1
        else:
            print("You have no accounts")
                    
    def get_all_accounts_and_balances(self):
        for accounts in self.currentCustomer.accountList:
            print(f"Account {accounts.get_accountNumber()} has {accounts.get_balance()}$")
    
    def deposit(self, accNum, amount):
        for account in self.currentCustomer.accountList:
            if accNum == account.get_accountNumber():
                if amount < 0 or amount == 0:
                    print("You can only deposit an amount greater than 0$!")
                    return
                
                else:
                    account.increase_balance(accNum, amount)
                    print(f"You deposited {amount}$ to account: {account.get_accountNumber()} \ncurrent balance: {account.get_balance()}$")
                    return
   
        print("Wrong account number!")
        
        
    def withdraw(self, accNum, amount):
        for account in self.currentCustomer.accountList:
            if accNum == account.get_accountNumber():
                if amount < 0 or amount == 0:
                    print("You can only withdraw an amount greater than 0$!")
                    return
                
                if amount > account.get_balance():
                    print(f"You do not have enough balance to withdraw {amount}$! \nYour current balance is: {account.get_balance()}$")
                    return
                
                else:
                    account.decrease_balance(accNum, amount)
                    print(f"You withdrew {amount}$ from account: {account.get_accountNumber()} \ncurrent balance: {account.get_balance()}$")
                    return
        print("Wrong account number!")
        
        
        
    def remove_account(self, accountNumber):
        for account in self.currentCustomer.accountList:
            if accountNumber == account.get_accountNumber():
                if account.balance > 0:
                    print(f"withdraw all your money from the account before removing the account! Current balance: {account.get_balance()}")
                    return
                else:
                    self.currentCustomer.accountList.remove(account)
                    print(f"removed account with accountnumber: {account.get_accountNumber()}")
                    return
        print(f"Account '{accountNumber}' does not exist. Can not delete")
        
        
        
    def json_file_write(self):
        file = open("json.txt", "w")
        for customer in self.customerList:
            json_string = json.dumps(customer.customer_to_dictionary())
            file.write(json_string)
            file.write("\n")
        file.close()
        for customer in self.customerList:
            customer.accountList.clear()
        self.customerList.clear()
        
        
        
    def json_file_read(self):
        file = open("json.txt", "r")
        content = file.readlines()
        if len(content) > 0:
            for line in content:
                json_string = json.loads(line)
                customer = Customer(json_string["name"], json_string["password"])
                self.customerList.append(customer)
                for account in json_string["accounts"]:
                    account_number = account["account_number"]
                    balance = int(account["balance"])
                    customer.accountList.append(Account(account_number, balance))
            
        file.close()

