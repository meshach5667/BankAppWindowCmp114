import tkinter as tk


class BankApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Bank App")

        self.selection_label = tk.Label(window, text="Select an account type:")
        self.selection_label.pack()

        self.saving_button = tk.Button(window, text="Saving Account", command=self.select_account_saving)
        self.saving_button.pack()

        self.current_button = tk.Button(window, text="Current Account", command=self.select_account_current)
        self.current_button.pack()

    def select_account_saving(self):
        self.create_account_window("Saving Account")

    def select_account_current(self):
        self.create_account_window("Current Account")

    def create_account_window(self, account_type):
        self.selection_label.destroy()
        self.saving_button.destroy()
        self.current_button.destroy()

        self.account_type_label = tk.Label(self.window, text=f"Selected Account: {account_type}")
        self.account_type_label.pack()

        self.balance_button = tk.Button(self.window, text="Check Balance", command=self.check_balance)
        self.balance_button.pack()

        self.deposit_button = tk.Button(self.window, text="Deposit Money", command=self.deposit_money)
        self.deposit_button.pack()

        self.withdraw_button = tk.Button(self.window, text="Withdraw Money", command=self.withdraw_money)
        self.withdraw_button.pack()



    def check_balance(self):
        print("Checking account balance")

    def deposit_money(self):
        print("Depositing money")

    def withdraw_money(self):
        print("Withdrawing money")

window = tk.Tk()
bank_app = BankApp(window)
window.mainloop()
