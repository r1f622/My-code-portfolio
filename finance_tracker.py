# Simple Personal Finance Tracker

print("--- Personal Finance Tracker ---")

expenses = {}

while True:
    item = input("\nEnter item name (or 'done' to finish): ")
    
    # check if user wants to stop
    if item.lower() == 'done':
        break
        
    amount_input = input(f"How much did {item} cost? ")
    
    # basic error checking so it doesn't crash
    if not amount_input.replace('.', '', 1).isdigit():
        print("Invalid amount. Please enter a number.")
        continue
        
    amount = float(amount_input)
    
    # add to dictionary (if already there, add to total)
    if item in expenses:
        expenses[item] = expenses[item] + amount
    else:
        expenses[item] = amount

print("\n--- Total Spending Summary ---")
total = 0

for item in expenses:
    amount = expenses[item]
    print(item + ": $" + str(round(amount, 2)))
    total = total + amount

print("-----------------------------")
print("TOTAL EXPENDITURE: $" + str(round(total, 2)))
