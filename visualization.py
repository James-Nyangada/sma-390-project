import matplotlib.pyplot as plt
import seaborn as sns

def plot_expenses(df):
    plt.figure(figsize=(8, 4))
    sns.barplot(x=df["name"], y=df["amount"], hue=df["name"], palette="coolwarm", legend=False)
    plt.xlabel("Expense Category")
    plt.ylabel("Amount ($)")
    plt.title("Monthly Expenses Breakdown")
    plt.show()
