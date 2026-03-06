import numpy as np
import matplotlib.pyplot as plt

t = [70, 72, 74, 76, 78, 80]
per = [12.3, 9.5, 7.7, 6.1, 4.3, 2.3]
y = []

#x = np.arange(30, 150, 1)
for i in t:
    yval = -0.93 * i + 77
    y.append(yval)

plt.scatter(t, per)
plt.xlabel('Temperatue (F)')
plt.ylabel('Percentage of damaged leaves')
plt.plot(t, y)
plt.show()
