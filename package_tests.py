import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
import tkinter.messagebox as mb
root = Tk()
root.withdraw()

mb.askyesno(title="test", message="Hit yes or no")

x = np.array([2,3,4])
y = np.array([6,7,8])

blank_df = pd.DataFrame(columns=['Test'])
print(blank_df)
plt.plot(x, y)
plt.show()
