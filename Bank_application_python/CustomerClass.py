#!/usr/bin/env python
# coding: utf-8

# In[3]:


from AccountClass import Account
class Customer:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.accountList = []
        self.used_numbers = []
                       
    def get_customer_name(self):
        return self.name
    
    def get_customer_password(self):
        return self.password
    
    def get_accountlist_dict(self):
        for account in self.accountList:
            print(account.__dict__)
            
    def customer_to_dictionary(self):
        return {
            "name": self.name,
            "password": self.password,
            "accounts": [
                {"account_number": account.accountNumber, "balance": account.balance}
                for account in self.accountList
            ],
        }

