class Account():

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, sum):
        self.balance += sum
    def witgraw(self, sum):
        if self.balance < sum:
            print("No enough Money")
        else:
            self.balance -=sum

a = Account("Adi", 5000)
a.deposit(100)
a.witgraw(200)
print(a.balance)


