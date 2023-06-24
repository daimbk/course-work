# Lab 9
# Daim Bin Khalid
# 251686775

class Payment:
    def __init__(self, amount):
        self.amount = amount

    def paymentDetails(self):
        print('Payment Amount: ', self.amount)
        print()

class CashPayment(Payment):
    def __init__(self, sender_name, receiver_name, amount):
        super().__init__(amount)
        self.sender_name = sender_name
        self.receiver_name = receiver_name

    def paymentDetails(self):
        print('Payment Means: Cash\nAmount: Rs.', self.amount)
        print('Sender: ' + self.sender_name + '\nReceiver: ' + self.receiver_name)
        print()

class CreditPayment(Payment):
    def __init__(self, receiver_name, amount, card_obj):
        super().__init__(amount)
        self.receiver_name = receiver_name
        self.card = card_obj   #associative object

    def setCardDetails(self):
        self.card.setDetails()  #association method
        print()

    def paymentDetails(self):
        print('Payment Means: Credit Card\nAmount: Rs.', self.amount)
        self.card.showInfo()   #association method
        print('Receiver: ' + self.receiver_name)
        print()

class CreditCards:
    def __init__(self):
        self.name = ''
        self.exp_date = 0
        self.card_num = 0

    def setDetails(self):
        self.name = input('Enter name on credit card: ')
        self.exp_date = input('Enter expiration date (MM/YY): ')
        self.card_num = int(input('Enter credit card number: '))

    def showInfo(self):
        print('Card holder: ', self.name)
        print('Expiration Date: ' + self.exp_date[0:2] + '/' + self.exp_date[2:4])
        print('Card Number: ', self.card_num)

def main():
    paymentlist = []

    paynum = int(input('How many cash payments to be made?: ')) #Number of CashPayment objects to be created
    for i in range(paynum):
        print('For cash payment: ')
        sendername = input('Enter sender name: ')
        receivername = input('Enter receiver name: ')
        amount = float(input('Enter amount to pay: '))
        payment = CashPayment(sendername, receivername, amount)
        paymentlist.append(payment)
        print()

    paynum = int(input('How many credit card payments to be made?: ')) #Number of CreditPayment objects to be created
    for i in range(paynum):
        credcard = CreditCards()
        receivername = input('Enter receiver name: ')
        amount = float(input('Enter amount to pay: '))
        payment = CreditPayment(receivername, amount, credcard)
        payment.setCardDetails()
        paymentlist.append(payment)
        print()

    for i in paymentlist:
        i.paymentDetails()    #Polymorphism as same method is called from different classes
main()