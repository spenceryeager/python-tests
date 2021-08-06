#!/usr/bin/env python3.9
import matplotlib.pyplot as plt
import tkinter.messagebox as mb 
import numpy as np

# this is a comment

mb.showinfo(title="Attention", message="This is a github test. I like VSCodium so far!")

x = np.linspace(1, 10, 100)
y = np.sqrt(x)

plt.plot(x, y)
plt.show()