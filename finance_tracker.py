# Simple Personal Finance Tracker
def main():
    expenses = {}
    print("--- Personal Finance Tracker ---")
    
    while True:
        item = input("\nEnter item name (or 'done' to finish): ")
        if item.lower() == 'done':
            break
        try:
            amount = float(input(f"How much did {item} cost? "))
            expenses[item] = expenses.get(item, 0) + amount
        except ValueError:
            print("Invalid amount. Please enter a number.")

    print("\n--- Total Spending Summary ---")
    total = 0
    for item, amount in expenses.items():
        print(f"{item}: ${amount:.2f}")
        total += amount
    print(f"-----------------------------")
    print(f"TOTAL EXPENDITURE: ${total:.2f}")

if __name__ == "__main__":
    main()
