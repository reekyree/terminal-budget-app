# Budget Application for the terminal.

print('#############\n')
print('BUDGET FRIEND\n')
print('#############\n')


def getNetIncome():

    netIncome = int(input("Enter your net income: "))

    print(f"Your net income is ${netIncome}.")
    print("We'll use this to start creating a budget.")
    return netIncome

def getRentCost():
    
    print("Next, let's get your rent.\n")
    rentCost = int(input("Next, enter the cost of rent per month: "))
    return rentCost 

income = getNetIncome()
rent = getRentCost()

percentage = rent / income
oneThird = 0.33 


if percentage == oneThird:
    print("Your rent is 1/3 of your total income. That's great!")
else:
    print(f"Your rent is {percentage:.2f}% of your budget. That's not great.")
