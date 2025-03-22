import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_expenses(df):
    df["month"] = pd.to_datetime(df["month"])  # Convert month column to datetime

    plt.figure(figsize=(10, 5))

    # 📊 Bar Chart: Total spending per category
    plt.subplot(1, 2, 1)
    sns.barplot(x=df["name"], y=df["amount"], hue=df["month"].dt.strftime('%Y-%m'), palette="coolwarm")
    plt.xlabel("Expense Category")
    plt.ylabel("Amount ($)")
    plt.title("Expense Breakdown by Category")

    # 📈 Line Chart: Monthly spending trends
    plt.subplot(1, 2, 2)
    monthly_totals = df.groupby("month")["amount"].sum().reset_index()
    sns.lineplot(x=monthly_totals["month"], y=monthly_totals["amount"], marker="o", color="b", label="Total Spending")
    plt.xlabel("Month")
    plt.ylabel("Total Amount ($)")
    plt.title("Monthly Spending Trend")

    plt.tight_layout()
    plt.show()
