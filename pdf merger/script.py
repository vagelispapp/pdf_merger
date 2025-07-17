from pypdf  import PdfMerger
import os
from tkinter import *
from tkinter import messagebox 
import tkinter as tk

user_text = "" 
forb_characters  = ['<', '>', ':', '*', '?', '"', '/', '\\', '|', '#']

def get_input():
    global user_text
    global forb_characters
    user_text = entry.get()
    
    #file name validation
    if any(c in forb_characters for c in user_text):
        message = tk.messagebox.showerror("Error", "Invalid name")
    else:        
        if not user_text.endswith(".pdf"):
            user_text = user_text + ".pdf"
        root.destroy()

root = tk.Tk()
root.title("Pdf Merger")

window_width = 300
window_height = 150

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate position x and y coordinates
# for the window to appear in the middle of the screen
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Set the geometry
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

lab = tk.Label(root, text="Enter the output file name")
lab.pack(expand=True)

entry = tk.Entry(root)
entry.pack(expand=True)

btn = tk.Button(root, text="Submit", command=get_input)
btn.pack(expand=True)

cwd = os.getcwd()
dir_list = os.listdir(cwd)

pdf_list = []

merger = PdfMerger()       
for file in dir_list:
    if file.endswith(".pdf"):
        merger.append(file)
        
root.mainloop()
merger.write(user_text)
merger.close()