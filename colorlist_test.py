import matplotlib.pyplot as plt
import numpy as np


xval = np.array([1, 2, 3, 4])

y1 = xval**1
y2 = xval**2
y3 = xval**3
y4 = xval**4
ylist = np.array([y1, y2, y3, y4])

print(len(ylist))


colors = plt.cm.Purples(np.linspace(0, 1, len(ylist)*2))
colors =colors[len(ylist):]
print(type(colors))

count = 0

while count < len(ylist):
    plt.plot(xval, ylist[count], color=colors[count])
    count += 1

plt.show()