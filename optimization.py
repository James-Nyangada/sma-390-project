from pulp import LpMaximize, LpProblem, LpVariable, lpSum

def optimize_budget(df, income):
    model = LpProblem("Budget Optimization", LpMaximize)

    # Define variables for each bill with constraints based on importance
    variables = {
        row["name"]: LpVariable(row["name"], lowBound=row["amount"] * row["importance"], upBound=row["amount"], cat="Continuous")
        for _, row in df.iterrows()
    }

    # Define savings as a variable
    savings = LpVariable("Savings", lowBound=0, cat="Continuous")

    # Objective Function: Maximize Savings
    model += savings, "Maximize Savings"

    # Constraint: Total budget must equal the income
    model += lpSum(variables.values()) + savings == income, "Total Budget"

    # Solve the problem
    model.solve()

    # Store the optimized allocation
    optimized_allocation = {name: var.varValue for name, var in variables.items()}
    optimized_allocation["Savings"] = savings.varValue

    print("\nOptimized Budget Allocation:")
    for key, value in optimized_allocation.items():
        print(f"{key}: ${value:.2f}")

    return optimized_allocation
