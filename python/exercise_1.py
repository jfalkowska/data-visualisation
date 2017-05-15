import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = np.arange(-5, 6)
y = x ** 2
plt.xlabel('axis x')
plt.ylabel('axis y')
plt.plot(x, y, c='blue', label='Data')

plt.xlim([-6,6])
plt.axvline(x=0, c = 'black')
plt.axhline(y=0, c = 'black', xmin=0.25, xmax=0.75)
plt.title('Sample title')
plt.legend()

plt.plot(x, x+1, color="red", linewidth=0.25)
plt.plot(x, x+2, color="red", linewidth=0.50)
plt.plot(x, x+3, color="red", linewidth=1.00)
plt.plot(x, x+4, color="red", linewidth=2.00)

plt.plot(x, x+6, color="green", lw=3, linestyle='-')
plt.plot(x, x+7, color="green", lw=3, ls='-.')
plt.plot(x, x+8, color="green", lw=3, ls=':')

plt.plot(x, x+ 10, color="blue", lw=3, ls='-', marker='+')
plt.plot(x, x+12, color="blue", lw=3, ls='--', marker='o')
plt.plot(x, x+14, color="blue", lw=3, ls='-', marker='s')

plt.plot(x, x+16, color="purple", lw=1, ls='-', marker='o', markersize=2)
plt.plot(x, x+18, color="purple", lw=1, ls='-', marker='o', markersize=4)
plt.plot(x, x+20, color="purple", lw=1, ls='-', marker='o', markersize=8, markerfacecolor="yellow")
plt.plot(x, x+22, color="purple", lw=1, ls='-', marker='s', markersize=8,
        markerfacecolor="yellow", markeredgewidth=3, markeredgecolor="green");

plt.show()
