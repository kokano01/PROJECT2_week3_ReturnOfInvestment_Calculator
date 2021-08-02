from typing import TextIO


class Roi():
    def __init__(self):
        self.totalincome = 0
        self.totalexpenses = 0
        self.totalcashflow = 0
        self.lstroi = []

    def income(self):
        print("\n==================== \nPart 1: INCOME \n====================")
        try:
            rent = int(input("How much is your monthly RENTAL income? "))
            laundry = int(input("How much is your monthly LAUNDRY income? "))
            storage = int(input("How much is your monthly STORAGE income? "))
            self.totalincome = rent+laundry+storage
            print("--Your total monthly income is: $", self.totalincome)
            self.expenses()
        except:
            print("Invalid input.. Please enter a number. ")
            self.income()
        

    def expenses(self):
        print("\n==================== \nPart 2: EXPENSES \n====================")
        try:
            tax = int(input("How much do you pay in monthly TAXES? "))
            insurance = int(input("How much do you pay in monthly INSURANCE? "))
            util = int(input("How much do you pay in monthly UTILITIES? "))
            hoa = int(input("How much do you pay in monthly HOMEOWNER'S ASSOCIATION fees? "))
            care = int(input("How much do you pay in monthly LAWN / SNOW care? "))
            vacancy = int(input("How much do you set aside monthly for VACANCY? "))
            repairs = int(input("How much do you pay in monthly REPAIRS? "))
            capex = int(input("How much do you pay in monthly CAPITAL EXPENDITURE? "))
            propmanage = int(input("How much do you pay in monthly PROPERTY MANAGEMENT? "))
            mortgage = int(input("How much do you pay for monthly MORTGAGE payments? "))
            self.totalexpenses = tax+insurance+util+hoa+care+vacancy+repairs+capex+propmanage+mortgage
            print("--Your total monthly expense is: $", self.totalexpenses)
            self.cashflow() 
        except:
            print("Invalid input.. Please enter a number. ")
            self.expenses()
        
    def cashflow(self):
        print("\n==================== \nPart3: Cash Flow \n====================")
        self.totalcashflow = self.totalincome - self.totalexpenses
        print("Total income - Total expenses")
        print("--Your total monthly cash flow is: $", self.totalcashflow)
        self.concroi()

    def concroi(self):
        print("\n==================== \nPart 4: Cash on Cash Return of Investement \n====================")
        try:
            dwn = int(input("How much did you pay for DOWN PAYMENT? "))
            close = int(input("How much were the CLOSING COSTS? (payment to title company/attorney, appraisal for loan documents, loan fees, etc.) "))
            rehab = int(input("How much was the REHAB? (cost for makeover/repaint) "))
            misc = int(input("Any other investment costs: "))
            totalinvest = dwn+close+rehab+misc
            print("--Your total investment on this property is: $", totalinvest)
            annualcashflow = self.totalcashflow * 12
            myconcroi = round(annualcashflow / totalinvest * 100, 2)
            self.lstroi.append(myconcroi)
            print("--Your Cash on Cash ROI is: ", myconcroi, "%")
            return
        except:
            print("Invalid input.. Please enter a number. ")
            self.concroi()
        


    def showROI(self):
        print("\nHere is a list of the ROI's of your property(s):   (in %'s)")
        print(self.lstroi)

    def clear(self):
        try:
            delete = int(input("\nWhich property ROI should I remove?  (Please enter a number) "))
            del self.lstroi[delete-1]
            print(self.lstroi)
        except:
            print("Invalid input.. Please enter a number. ")
            self.clear()
        
        

    def runSimulation(self):
        print('\nThis is a Return of Investment calculator"')
        while True:
            answer=input('\nWould you like to get started?: (yes/no/list/clear) ').lower()
            if answer == "yes":
                print("\nThere will be 4 parts to this calculator: Income / Expenses / Cash Flow / Cash on Cash ROI")
                self.income()
            
            elif answer == "no":
                break
            elif answer == "list":
                self.showROI()

            elif answer == "clear":
                self.clear()
            

            else:
                print('Invalid input: Please enter one of the options.')

myroi = Roi()
myroi.runSimulation()