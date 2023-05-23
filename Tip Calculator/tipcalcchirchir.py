# asks for the food charge amount
food_charge = float(input("Charge for food = $"))

# Calculate the tip amount (18% of the food charge)
tip_amount = 0.18 * food_charge

# Calculate the sales tax amount (7% of the food charge)
tax_amount = 0.07 * food_charge

# Calculate the grand total (food charge + tip + sales tax)
grand_total = food_charge + tip_amount + tax_amount

# Display the tip amount, sales tax amount, and grand total
print("Tip = $" + format(tip_amount, ".2f"))
print("Sales tax = $" + format(tax_amount, ".2f"))
print("Grand total = $" + format(grand_total, ".2f"))
