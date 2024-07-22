import tkinter as tk
from tkinter import ttk, messagebox

class FinanceManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Manager")

        self.transactions = []

        self.setup_ui()

    def setup_ui(self):
        self.tree = ttk.Treeview(self.root, columns=("Date", "Description", "Amount", "Category"), show="headings")
        self.tree.heading("Date", text="Date")
        self.tree.heading("Description", text="Description")
        self.tree.heading("Amount", text="Amount")
        self.tree.heading("Category", text="Category")
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.add_transaction_button = tk.Button(self.root, text="Add Transaction", command=self.add_transaction)
        self.add_transaction_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.remove_transaction_button = tk.Button(self.root, text="Remove Transaction", command=self.remove_transaction)
        self.remove_transaction_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.view_report_button = tk.Button(self.root, text="View Report", command=self.view_report)
        self.view_report_button.pack(side=tk.LEFT, padx=10, pady=10)

    def add_transaction(self):
        self.transaction_window = tk.Toplevel(self.root)
        self.transaction_window.title("Add Transaction")

        tk.Label(self.transaction_window, text="Date (YYYY-MM-DD):").grid(row=0, column=0, padx=10, pady=10)
        self.date_entry = tk.Entry(self.transaction_window)
        self.date_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.transaction_window, text="Description:").grid(row=1, column=0, padx=10, pady=10)
        self.description_entry = tk.Entry(self.transaction_window)
        self.description_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.transaction_window, text="Amount:").grid(row=2, column=0, padx=10, pady=10)
        self.amount_entry = tk.Entry(self.transaction_window)
        self.amount_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(self.transaction_window, text="Category:").grid(row=3, column=0, padx=10, pady=10)
        self.category_entry = tk.Entry(self.transaction_window)
        self.category_entry.grid(row=3, column=1, padx=10, pady=10)

        tk.Button(self.transaction_window, text="Save", command=self.save_transaction).grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def save_transaction(self):
        date = self.date_entry.get()
        description = self.description_entry.get()
        amount = self.amount_entry.get()
        category = self.category_entry.get()

        self.transactions.append((date, description, amount, category))
        self.tree.insert("", tk.END, values=(date, description, amount, category))

        self.transaction_window.destroy()

    def remove_transaction(self):
        selected_item = self.tree.selection()
        if selected_item:
            self.tree.delete(selected_item)
            index = self.tree.index(selected_item)
            self.transactions.pop(index)
        else:
            messagebox.showwarning("Warning", "No transaction selected")

    def view_report(self):
        report_window = tk.Toplevel(self.root)
        report_window.title("Report")

        total_income = sum(float(t[2]) for t in self.transactions if float(t[2]) > 0)
        total_expenses = sum(float(t[2]) for t in self.transactions if float(t[2]) < 0)
        net_balance = total_income + total_expenses

        tk.Label(report_window, text=f"Total Income: ${total_income:.2f}").pack(pady=10)
        tk.Label(report_window, text=f"Total Expenses: ${total_expenses:.2f}").pack(pady=10)
        tk.Label(report_window, text=f"Net Balance: ${net_balance:.2f}").pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = FinanceManager(root)
    root.mainloop()