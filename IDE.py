import tkinter as tk
from tkinter import messagebox
from parser import parser
from validator import validate_code


def compile_code(code):
    if not validate_code(code):
        return None

    try:
        result = parser.parse(code)
        return result
    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")
        return None


class CalculatorIDE:
    def __init__(self, master):
        self.master = master
        master.title("Calculator IDE")

        self.entry = tk.Entry(master, width=40)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Create buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            tk.Button(master, text=button, width=7, height=2, command=lambda b=button: self.button_click(b)).grid(
                row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def button_click(self, value):
        current = self.entry.get()

        if value == "=":
            result = compile_code(current)
            if result is not None:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
        else:
            self.entry.insert(tk.END, value)


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorIDE(root)
    root.mainloop()
