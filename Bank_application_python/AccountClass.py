#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Account:
    def __init__(self, accountNumber, balance):
        self.accountNumber = accountNumber
        self.balance = balance
                
    def increase_balance(self, accountNumber, amount):
        self.balance += amount
                
    def decrease_balance(self, accountNumber, amount):
        self.balance -= amount
    
    def get_balance(self):
        return self.balance
    
    def get_accountNumber(self):
        return self.accountNumber
    

