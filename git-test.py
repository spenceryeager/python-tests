#!/usr/bin/env python3.9
import matplotlib.pyplot as plt
import tkinter.messagebox as mb 
from tkinter import *
import numpy as np

root = Tk()
root.withdraw()

# this is a comment

#this is going to test autopep8. Lets do it

mb.showinfo(title="Attention", message="This is a github test. I like VSCodium so far!")

x = np.linspace(1, 10, 100)
y = np.sqrt(x)

plt.plot(x, y)
plt.show()