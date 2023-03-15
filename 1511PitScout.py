from PIL import Image
from pytesseract import pytesseract
from tkinter import *
import tkinter as tk 

root = Tk()
test_frame = tk.Frame(root, padx=10, pady=10)
test_frame.grid()
button = tk.Button(test_frame, text="hello").grid(row=0, column=0)


root.mainloop()