import tkinter as tk
from tkinter import filedialog, messagebox
#from optimizer import load_data, optimize_bills
#from visualization import plot_expenses, plot_optimized_expenses

class BillOptimizerApp:
    #the heading

    def __init__(self, root):
        self.root = root
        self.root.title("Monthly Bill Optimizer")

        #the textbox
        
        self.label = tk.Label(root, text="Enter your budget:")
        self.label.pack()
        
        self.budget_entry = tk.Entry(root)
        self.budget_entry.pack()
        
        #buttons

        self.load_button = tk.Button(root, text="Load Bills", command=self.load_bills)
        self.load_button.pack()
        
        self.optimize_button = tk.Button(root, text="Optimize Bills", command=self.optimize_bills)
        self.optimize_button.pack()
        
        self.plot_button = tk.Button(root, text="Plot Expenses", command=self.plot_expenses)
        self.plot_button.pack()
        
        self.plot_optimized_button = tk.Button(root, text="Plot Optimized Expenses", command=self.plot_optimized_expenses)
        self.plot_optimized_button.pack()
        
        self.df = None
        self.optimized_df = None

    def load_bills(self):
        file_path = filedialog.askopenfilename()
        try:
            self.df = load_data(file_path)
            messagebox.showinfo("Success", "Bills loaded successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def optimize_bills(self):
        try:
            budget = float(self.budget_entry.get())
            self.optimized_df = optimize_bill(self.df, budget)
            messagebox.showinfo("Success", "Bills optimized successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def plot_expenses(self):
        if self.df is not None:
            plot_expense(self.df)
        else:
            messagebox.showerror("Error", "No bills data loaded.")

    def plot_optimized_expenses(self):
        if self.optimized_df is not None:
            plot_optimized_expense(self.optimized_df)
        else:
            messagebox.showerror("Error", "No optimized bills data available.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BillOptimizerApp(root)
    root.mainloop()