
def CalculateDebt():
    print("Credit Card Calculator - Asad Alli 2024")
    totalChecking = input("Checkings total amount: ")

    TDCardMax = 6000.00
    TDCardCreditLeft = input("Input total available TD credit: ")

    totalTDOwed = TDCardMax - float(TDCardCreditLeft)
    totalTDOwed = round(totalTDOwed, 2)

    AmexCardMax = 10000.00
    AmexCardCreditLeft = input("Input total available Amex credit: ")

    totalAmexOwed = AmexCardMax - float(AmexCardCreditLeft)
    totalAmexOwed = round(totalAmexOwed, 2)

    print("\n\nTotal TD Debt: " + str(totalTDOwed))
    print("Total AMEX owed: " + str(totalAmexOwed))

    totalOwed = float(totalTDOwed) + float(totalAmexOwed)
    totalOwed = round(totalOwed, 2)
    print("Total credit due: " + str(totalOwed))

    newCheckingAmount = float(totalChecking) - totalOwed
    newCheckingAmount = round(newCheckingAmount, 2)
    print("Total checking amount after credit debt: " + str(newCheckingAmount))

CalculateDebt()