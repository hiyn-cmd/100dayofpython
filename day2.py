print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
bill_with_tip = bill*(tip/100) + bill
pay = bill_with_tip/people
pay_rounded = round(pay,2)
print(f"Each person should pay: {pay_rounded}")

