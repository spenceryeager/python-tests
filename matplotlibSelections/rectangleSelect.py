from matplotlib.widgets import RectangleSelector
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# following this tutorial from matplotlib documentation:
# https://matplotlib.org/stable/gallery/widgets/rectangle_selector.html

def line_select_callback(eclick, erelease):
    """
    Callback for line selection.

    *eclick* and *erelease* are the press and release events.
    """
    x1, y1 = eclick.xdata, eclick.ydata
    x2, y2 = erelease.xdata, erelease.ydata
    print(f"({x1:3.2f}, {y1:3.2f}) --> ({x2:3.2f}, {y2:3.2f})")
    print(f" The buttons you used were: {eclick.button} {erelease.button}")


def toggle_selector(event):
    print(' Key pressed.')
    if event.key == 't':
        if toggle_selector.RS.active:
            print(' RectangleSelector deactivated.')
            toggle_selector.RS.set_active(False)
        else:
            print(' RectangleSelector activated.')
            toggle_selector.RS.set_active(True)

def rowskip(file):  # cleans up all the extra stuff in the header
    file = open(workingfile, 'r')
    count1 = 0
    for line in file:
        if line.strip() == "Potential/V, Current/A":
            row = count1
        count1 += 1
    return row

workingfile = "/home/spenceryeager/Documents/python_bits/sample_data/cv/pf6.csv"
row = rowskip(workingfile)

cvdf = pd.read_csv(workingfile, skiprows=row)

print(cvdf)

fig, ax = plt.subplots()

ax.plot(cvdf['Potential/V'], cvdf[' Current/A'])  # plot something
ax.set_title(
    "Click and drag to draw a rectangle.\n"
    "Press 't' to toggle the selector on and off.")

plt.ylim((min(cvdf[' Current/A']), max(cvdf[' Current/A'])))
# drawtype is 'box' or 'line' or 'none'
toggle_selector.RS = RectangleSelector(ax, line_select_callback,
                                       drawtype='box', useblit=True,
                                       button=[1, 3],  # disable middle button
                                       minspanx=5, minspany=5,
                                       spancoords='pixels',
                                       interactive=True)
fig.canvas.mpl_connect('key_press_event', toggle_selector)
plt.show()
