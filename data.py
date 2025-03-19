import pandas as pd

def collect_expenses():
    bills = []  # List to store expenses

    print("\nEnter your monthly bills (Type 'done' when finished):")
    
    while True:
        name = input("Enter bill name (e.g., Rent, Internet): ")
        if name.lower() == 'done':
            break
        try:
            amount = float(input("Enter amount: "))
            importance = input("Enter importance level (1=Essential, 2=Half-important, 3=Not important): ")
            
            if importance not in ["1", "2", "3"]:
                print("Invalid input. Please enter 1, 2, or 3.")
                continue

            # Convert importance to numeric multiplier
            importance_multiplier = {"1": 1.0, "2": 0.5, "3": 0.2}[importance]
            
            bills.append({"name": name, "amount": amount, "importance": importance_multiplier})

        except ValueError:
            print("Invalid input. Please enter a number for the amount.")

    df = pd.DataFrame(bills)
    df.to_csv("bills.csv", index=False)
    print("\nExpenses saved to bills.csv!\n")

    return df

def load_expenses():
    try:
        df = pd.read_csv("bills.csv")
        return df
    except FileNotFoundError:
        print("No previous expenses found. Please enter new bills.")
        return collect_expenses()
