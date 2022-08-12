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
    """
    def openAccount(self,name,mobile,address,idproof):
        self.name = name
        self.mobile = mobile
        self.address = address
        self.idproof=idproof
        self.balance = 0
        self.accountnumber = self.accountnumber+1
        return self.accountnumber
    """
    """
    Constructor __init__
    """
    def __init__(self, name, mobile, address, idproof):
        self.name = name
        self.mobile = mobile
        self.address = address
        self.idproof = idproof
        self.balance = 0
        self.accountnumber = self.accountnumber + 1


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

"""
Object
"""

#act1 = Account() without constructor
act1 = Account("Ravi",9845547471,"Magadi","aadhar number 393933993")
#actno1 = act1.openAccount("Ravi",9845547471,"Magadi","aadhar number 393933993")
actno1 =act1.accountnumber
print("Your account number is -1 ",actno1)
balance1= act1.deposit(actno1,10000)
print("Your balance after deposit of 10k ",balance1)
balance1= act1.deposit(actno1,15000)
print("Your balance after deposit of 15k ",balance1)
balance1= act1.withdraw(actno1,5000)
print("Your balance after withdraw of 5k ",balance1)
info1= act1.info()
print("account info ",info1)






