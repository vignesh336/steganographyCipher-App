import os
import shutil
import tkinter as tk
import glob
from pathlib import Path
from tkinter import filedialog
from tkinter.messagebox import *

window = tk.Tk()
window.title('STEGO')
window.geometry("480x360")

# +++++ Title Label +++++

label1=tk.Label(text="STEGANOGRAPHY WITH CIPHER")
label1.pack()


# ++++++ Browse Button Function ++++++

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    global filename
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    
def quit_prompt():
	if askquestion(title="Quit?", message="you wanna quit?") =='yes':
		window.quit()
		exit()
def enter_folder_dir():
	showwarning(title="Error", message="STEGANOGRAPHY & CRYPTOGRAPHY")


# +++++ Browse Button GUI elements +++++

folder_path = tk.StringVar()
lbl1 = tk.Label(master=window,textvariable=folder_path)
lbl1.pack()




def empty_folder():
    os.system('encode.py')
button2 = tk.Button(text="encode", command=empty_folder)
button2.pack()


def organise():
    os.system('decode.py')
button2 = tk.Button(text="decode", command=organise)
button2.pack()

