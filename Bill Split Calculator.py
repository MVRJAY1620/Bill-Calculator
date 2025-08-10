# Bill Split Calculator
# This script calculates the total bill amount including tip and splits it among a specified number of people
print("Vandana's Python Bill Split Calculator")

# Input the total bill amount and tip percentage
Bill_amount = float(input("Enter the total bill amount: "))
Tip_percentage = float(input("Enter the tip percentage: "))

# Calculate the total amount including tip and the amount per person
Tip_amount = (Tip_percentage / 100) * Bill_amount
Total_amount = Bill_amount + Tip_amount

#prints the total amount
print(f"Total amount including tip: {Total_amount:.2f}")

# Input the number of people to split the bill and calculate the amount per person
Number_of_people_splitting = int(input("Enter the number of people to split the bill: "))
Amount_per_person = Total_amount / Number_of_people_splitting

#prints the amount per person
print(f"Total amount per person: {Amount_per_person:.2f}")
