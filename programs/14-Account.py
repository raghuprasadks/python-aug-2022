""""
Account class
with openAccount,deposit,withdraw,checkBalance
as methods
"""
class Account():
    """
    properties
    """
    name=""
    mobile=0;
    address=""
    idproof=""
    balance=0
    accountnumber = 0
    """
    methods
    """
    def openAccount(self,name,mobile,address,idproof):
        self.name = name
        self.mobile = mobile
        self.address = address
        self.idproof=idproof
        self.balance = 0
        self.accountnumber = self.accountnumber+1

    def deposit(self,accountnumber,amttodeposit):
        self.accountnumber=accountnumber
        self.balance = self.balance+amttodeposit
        return self.balance

    def withdraw(self, accountnumber, amttowithdraw):
        self.accountnumber = accountnumber
        self.balance = self.balance - amttowithdraw
        return self.balance

    def checkBalance(self,accountnumber):
        return self.balance

    def info(self):
        return "Name : ",self.name, "Account Number ",self.accountnumber," Balance ",self.balance
