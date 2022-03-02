class Bankaccount:
    def _init_(self):
        self.accno=10253515421
        self.name="Anju"
        self.acctype="savings"
        self.balance=0
    def deposit(self):
        amount=int(input("enter the amount to be deposited: "))
        self.balance+=amount
        print("Amount succsfully deposited")
    def withdraw(self):
        amount=int(input("enter the amount to withdraw: "))
        if self.balance>=amount:
            self.balance-=amount
            print("succesfully withdrawn")
        else:
            print("insufficient balance")
    def display(self):
        print("Account number=",self.accno,"\nName=",self.name,"\nAccount type=",self.acctype,"\nAvailable balance=",self.balance)
ob=Bankaccount()
ob.deposit()
ob.withdraw()
ob.display()
