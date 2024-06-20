import tkinter as tk
from tkinter import filedialog, messagebox

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.text_area = tk.Text(self.root)
        self.menu = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.edit_menu = tk.Menu(self.menu, tearoff=0)
        self.root.config(menu=self.menu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Delete", command=self.delete_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)
        self.edit_menu.add_command(label="Cut", command=self.cut)
        self.edit_menu.add_command(label="Copy", command=self.copy)
        self.edit_menu.add_command(label="Paste", command=self.paste)
        self.edit_menu.add_command(label="Delete", command=self.delete)
        self.text_area.pack()
        self.file_path = ""

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.file_path = ""
        self.root.title("Text Editor - Untitled")

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                self.text_area.insert(1.0, file.read())
                self.file_path = file_path
                self.root.title(f"Text Editor - {file_path}")

    def save_file(self):
        if self.file_path:
            with open(self.file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
        else:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
            if file_path:
                with open(file_path, "w") as file:
                    file.write(self.text_area.get(1.0, tk.END))
                self.file_path = file_path
                self.root.title(f"Text Editor - {file_path}")

    def delete_file(self):
        if self.file_path:
            if messagebox.askyesno("Delete File", "Are you sure you want to delete this file?"):
                import os
                os.remove(self.file_path)
                self.file_path = ""
                self.text_area.delete(1.0, tk.END)
                self.root.title("Text Editor - Untitled")

    def cut(self):
        self.text_area.clipboard_clear()
        self.text_area.clipboard_append(self.text_area.selection_get())
        self.text_area.delete("sel.first", "sel.last")

    def copy(self):
        self.text_area.clipboard_clear()
        self.text_area.clipboard_append(self.text_area.selection_get())

    def paste(self):
        self.text_area.insert("insert", self.text_area.clipboard_get())

    def delete(self):
        self.text_area.delete("sel.first", "sel.last")

root = tk.Tk()
text_editor = TextEditor(root)
root.mainloop()