# Lab 9
# Daim Bin Khalid
# 251686775

from abc import abstractmethod
class Payment:
    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def paymentDetails(self, *args):   #abstract method
        print('Payment Amount: ', self.amount)
        print()
        pass

class CashPayment(Payment):
    def __init__(self, sender_name, receiver_name, amount):
        super().__init__(amount)
        self.sender_name = sender_name
        self.receiver_name = receiver_name

    def paymentDetails(self, *args):
        print('Payment Means: Cash\nAmount: Rs.', self.amount)
        print('Sender: ' + self.sender_name + '\nReceiver: ' + self.receiver_name)
        print()

class CreditPayment(Payment):
    def __init__(self, receiver_name, amount):
        super().__init__(amount)
        self.receiver_name = receiver_name

    def paymentDetails(self, credcard):
        print('Payment Means: Credit Card\nAmount: Rs.', self.amount)
        credcard.showInfo()   #association method
        print('Receiver: ' + self.receiver_name)
        print()

class CreditCards:
    def __init__(self, name, exp, cardnum):
        self.name = name
        self.exp_date = exp
        self.card_num = cardnum

    def showInfo(self):
        print('Card holder: ', self.name)
        print('Expiration Date: ' + self.exp_date[0:2] + '/' + self.exp_date[2:])
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

    print('Enter credit card info: ')
    name = input('Card holder name: ')
    exp = input('Expiry Date: (MMYY): ')
    cardnum = int(input('Credit Card Number: '))
    credcard = CreditCards(name, exp, cardnum)
    more = 'y'
    while (more == 'y'):
        paynum = int(input('How many payments to be made with this card?: ')) #Number of CreditPayment objects to be created
        for i in range(paynum):
            receivername = input('Enter receiver name: ')
            amount = float(input('Enter amount to pay: '))
            payment = CreditPayment(receivername, amount)
            paymentlist.append(payment)
            print()
        more = input('Do you want to make more payments? (y or n): ')
        print()

    for i in paymentlist:
        i.paymentDetails(credcard)    #Polymorphism as same method is called from different classes
main()