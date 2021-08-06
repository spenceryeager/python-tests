import os
from tkinter import *
import tkinter.filedialog as gui
import tkinter.simpledialog as box
import tkinter.messagebox as msgb

root = Tk()
root.withdraw

name = box.askstring("New Directory", "Enter directory name, or cancel to quit program")
if (name == None):
    quit()

raw


