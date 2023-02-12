#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Account:
    def __init__(self, accountNumber, balance): #constructor
        self.accountNumber = accountNumber  #self är instancen eller objektet. self.accountNumber är alltså accountNumber som du passar som parameter vid instance
        self.balance = balance #self är instancen eller objektet. self.balance är alltså balance som du passar som parameter vid instance
                
    def increase_balance(self, accountNumber, amount): #WORKS
        self.balance += amount
                
    def decrease_balance(self, accountNumber, amount): #works
        self.balance -= amount
    
    def get_balance(self): #WORKS
        return self.balance
    
    def get_accountNumber(self): #WORKS
        return self.accountNumber
    

