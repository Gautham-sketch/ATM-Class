class ATM :
    def __init__(self,cardno,pinno):
        self.cardno = cardno
        self.pinno = pinno
    def balanceEnquiry(self):
        print("You have $100000 as balance in the bank")
    def moneyTransaction(self):
        print("Transaction successfull !")
    def withdrawal(self):
        money = input("Enter the amount you want to take :- ")
        print("Money recieved !")
User = ATM(123456789,987)
User.withdrawal()