import os
import tkinter.simpledialog as box
from tkinter import *

root = Tk()
root.withdraw
dir = "/home/spenceryeager/Documents/python_bits/dir_test"
filelist = os.listdir(dir)
dirlist = []
for i in filelist:
    print(i)
    print(os.path.isdir(os.path.join(dir, i)))
    if os.path.isdir(os.path.join(dir, i)):
        dirlist.append(i)

folder_name = box.askstring("New Directory", "Enter data output folder name")  # use for gui

for i in dirlist:
    if i == folder_name:
        while folder_name == i:
            folder_name = box.askstring("Error: New Directory", "Directory already exists. Please enter a different name")

output_path = os.path.join(dir, folder_name)
os.mkdir(output_path)