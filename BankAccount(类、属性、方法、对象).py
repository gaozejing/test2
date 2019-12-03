class BankAccount:
    #属性账户名、账户号、账户余额
    def __init__(self):
        self.account_name = "name"
        self.account_num = "000000"
        self.account_balance = 0
    def __str__(self):
        msg1 = "Your account name: " + self.account_name
        msg2 = "Your account number: " + self.account_num
        msg3 = "Your account balance: " +str(self.account_balance)
        msg = msg1 +'\n'+ msg2+ '\n' + msg3+ '\n'
        return msg
    #计算余额
    def banlance(self,cost):
        self.account_balance = self.account_balance + cost
        return self.account_balance

    #存钱
    def save(self,cost):
       return cost
    #取钱
    def draw(self,cost):
        cost = -cost
        return cost
#子类包含利率
class InterestAccount(BankAccount):
    def __init__(self):
        BankAccount.__init__(self)
        self.interest = 0
    #计算算上利率后的余额
    def addInterest(self,addinterest):
        self.interest = addinterest
        self.account_balance = self.account_balance*(1+self.interest)
        print(self.account_balance)


myAccount = BankAccount()
print(myAccount)
myAccount.account_name = "Vicky"
myAccount.account_num = "123456"
myAccount.account_balance = 1000
print(myAccount)
cost1 = myAccount.save(100)
print(myAccount.banlance(cost1))
cost2 = myAccount.draw(200)
print(myAccount.banlance(cost2))
print(myAccount)

myAccount = InterestAccount()
cost1 = myAccount.save(100)
print(myAccount.banlance(cost1))
myAccount.addInterest(0.1)
print(myAccount)
