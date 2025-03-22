import pandas as pd
import os

CSV_FILE = "bills.csv"

def collect_expenses():
    bills = []
    print("\nEnter your monthly bills (Type 'done' when finished):")

    month = input("Enter the month (format: YYYY-MM): ")

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
            importance_multiplier = {"1": 1.0, "2": 0.5, "3": 0.2}[importance]

            bills.append({"month": month, "name": name, "amount": amount, "importance": importance_multiplier})

        except ValueError:
            print("Invalid input. Please enter a number for the amount.")

    return pd.DataFrame(bills)

def load_expenses():
    """ Loads previous expenses and allows the user to add new ones """
    # Check if the file exists
    if os.path.exists(CSV_FILE):
        df = pd.read_csv(CSV_FILE)
        print("\nPrevious expenses found.")
        
        # Ask the user if they want to add new monthly bills
        choice = input("Do you want to enter new monthly bills? (yes/no): ").strip().lower()
        if choice == "yes":
            new_df = collect_expenses()
            df = pd.concat([df, new_df], ignore_index=True)
            df.to_csv(CSV_FILE, index=False)
            print("\nExpenses updated and saved to bills.csv!")
        else:
            print("\nUsing previous expense data.")

    else:
        print("\nNo previous expenses found. Please enter new bills.")
        df = collect_expenses()
        df.to_csv(CSV_FILE, index=False)
        print("\nExpenses saved to bills.csv!")

    return df
