import tkinter as tk
from tkinter import filedialog
import os
 
def open_file():
    filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if filename:
        display_text(filename)
 
def display_text(filename):
    window = tk.Toplevel(root)
    window.geometry('400x300')
 
    with open(filename, 'r') as file:
        text = file.read()
 
    text_widget = tk.Text(window)
    text_widget.insert(tk.END, text)
    text_widget.pack(expand=True, fill=tk.BOTH)
 
root = tk.Tk()
root.resizable(False, False)
root.geometry('200x100')
 
open_button = tk.Button(root, text="Open File", command=open_file)
open_button.pack(expand=True)
 
root.mainloop()
