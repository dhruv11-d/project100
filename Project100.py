class Atm():
    def __init__(self, cardNumber, pinNumber, currentBalance):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
        self.currentBalance = currentBalance
    def printCardNumber(self):
        print("Your Card number Is " + str(self.cardNumber))
    def printPinNumber(self):
        print("Your Pin Number Is: " + str(self.pinNumber))
    def printCurrentBalance(self):
        print("Your Current Balance Is " + str(self.currentBalance))
card = Atm(2900,16000,100000)

card.printCardNumber()
card.printPinNumber()
card.printCurrentBalance()