import tkinter as tk
from tkinter import filedialog

import messagebox as messagebox

from parser import parser
from validator import validate_code


class TextEditor:
    def __init__(self, master):
        self.master = master
        master.title("Group 4")

        self.text = tk.Text(master, wrap="word", undo=True)
        self.text.pack(expand="yes", fill="both")

        # Create menu bar
        self.menu_bar = tk.Menu(master)
        self.master.config(menu=self.menu_bar)

        # File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As...", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_program)

        # Edit menu
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Cut", command=self.cut_text)
        self.edit_menu.add_command(label="Copy", command=self.copy_text)
        self.edit_menu.add_command(label="Paste", command=self.paste_text)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Undo", command=self.text.edit_undo)
        self.edit_menu.add_command(label="Redo", command=self.text.edit_redo)

        # Run menu
        self.run_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Run", menu=self.run_menu)
        self.run_menu.add_command(label="Parse and Validate", command=self.parse_and_validate)

    def new_file(self):
        self.text.delete(1.0, tk.END)
        self.master.title("Text Editor")

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                               filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text.delete(1.0, tk.END)
                self.text.insert(tk.END, content)
                self.master.title(f"Text Editor - {file_path}")

    def save_file(self):
        if self.master.title() == "Text Editor":
            self.save_as_file()
        else:
            file_path = self.master.title()[len("Text Editor - "):]
            with open(file_path, "w") as file:
                file.write(self.text.get(1.0, tk.END))

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text.get(1.0, tk.END))
            self.master.title(f"Text Editor - {file_path}")

    def exit_program(self):
        self.master.destroy()

    def cut_text(self):
        self.text.event_generate("<<Cut>>")

    def copy_text(self):
        self.text.event_generate("<<Copy>>")

    def paste_text(self):
        self.text.event_generate("<<Paste>>")

    def parse_and_validate(self):
        code = self.text.get(1.0, tk.END)
        if validate_code(code):
            try:
                result = parser.parse(code)
                result_str = str(result)
                self.text.insert(tk.END, "\n\nParser Result:\n")
                self.text.insert(tk.END, result_str)
            except Exception as e:
                error_message = f"Parser Error: {e}"
                messagebox.showerror("Parser Error", error_message)
                self.text.insert(tk.END, f"\n\n{error_message}")
            else:
                self.text.insert(tk.END, "\n\nInvalid Code: Please check your code.")


if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.geometry("800x600")
    root.mainloop()
