# Daim BIn Khalid
# 25168775
# Lab 10

class Package:
    def __init__(self, sname, rname, saddress, raddress, scity, rcity, sstate, rstate, szip, rzip, weight, cost):
        self.sname = sname
        self.rname = rname
        self.saddress = saddress
        self.raddress = raddress
        self.scity = scity
        self.rcity = rcity
        self.sstate = sstate
        self.rstate = rstate
        self.szip = szip
        self.rzip = rzip
        self.weight = abs(weight)
        self.costperounce = abs(cost)

    def calculateCost(self):
        self.total_cost = round(float(self.weight * self.costperounce), 2)
        return self.total_cost

class TwoDayPackage(Package):
    def __init__(self, flatfee, sname, rname, saddress, raddress, scity, rcity, sstate, rstate, szip, rzip, weight, cost):
        super().__init__(sname, rname, saddress, raddress, scity, rcity, sstate, rstate, szip, rzip, weight, cost)
        self.flatfee = flatfee

    def calculateCost(self):
        self.total_cost = round(float(self.flatfee + super().calculateCost()), 2)
        return self.total_cost

class OvernightPackage(Package):
    def __init__(self, add_fee, sname, rname, saddress, raddress, scity, rcity, sstate, rstate, szip, rzip, weight, cost):
        super().__init__(sname, rname, saddress, raddress, scity, rcity, sstate, rstate, szip, rzip, weight, cost)
        self.add_fee_per_ounce = add_fee

    def calculateCost(self):
        self.total_cost = round(float((self.weight * self.add_fee_per_ounce) + super().calculateCost()), 2)
        return self.total_cost

def main():
    twodayobj = TwoDayPackage(200, 'Manal', 'Kiran', 'Cavalry', 'Shadman', 'Lahore', 'Lahore', 'Punjab', 'Punjab', 54000, 54000, 5.4, 400)
    overnobj = OvernightPackage(150, 'Daim', 'Hafsah', 'House 9', 'FCC', 'Lahore', 'Lahore', 'Punjab', 'Punjab', 54000, 54000, 3.95, 500)

    print('Calculated cost for:')
    print('Two Day Package: Rs.', twodayobj.calculateCost())
    print('Overnight Package: Rs.',overnobj.calculateCost())
main()