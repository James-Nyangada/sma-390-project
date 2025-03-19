import data
import clustering
import optimization
import prediction
import visualization

def main():
    print("Welcome to the Monthly Bill Optimizer!\n")
    
    # Step 1: Collect user expenses
    df = data.load_expenses()
    
    # Step 2: Cluster expenses
    df = clustering.cluster_expenses(df)
    
    # Step 3: Get user income & optimize budget
    income = float(input("\nEnter your total monthly income: $"))
    optimized_budget = optimization.optimize_budget(df, income)

    # Step 4: Predict next month's bills
    predictions = prediction.predict_expenses(df)
    
    # Step 5: Visualize results
    visualization.plot_expenses(df)

if __name__ == "__main__":
    main()
