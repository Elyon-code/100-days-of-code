print("Welcome to the python tip calculator!")

total = float(input("How much is the total bill? $ "))
tip = int(input("How much percent tip would you like to give? 10, 12, 15? "))

total_tip = (tip * 0.01) * total
total_bill = total + total_tip

number_of_people = int(input("How many people will like to split the bill? "))

individual_price = total_bill / number_of_people

print(f"Each person should pay ${individual_price:.2f}")
