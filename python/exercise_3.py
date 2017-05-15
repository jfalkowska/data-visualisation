import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

x = np.arange(-5, 6)
y = x ** 2

plt.plot(x, y + 10, 'r')

plt.xlabel('x')
plt.ylabel('y')
plt.plot(x, y, c='red', label='data')
plt.xlim([-6,6])
plt.axvline(x=0, c = 'black')
plt.axhline(y=0, c = 'black')
plt.legend()

plt.plot(y + 10, x, 'g')

plt.xlabel('x')
plt.ylabel('y')
plt.plot(x, y, c='yellow', label='data')
plt.xlim([-6,6])
plt.axvline(x=0, c = 'black')
plt.axhline(y=0, c = 'black')
plt.legend()

plt.plot(x, y, 'b')

plt.xlabel('x')
plt.ylabel('y')
plt.plot(x, y, c='blue', label='data')
plt.xlim([-6,6])
plt.axvline(x=0, c = 'black')
plt.axhline(y=0, c = 'black')
plt.title('Blue')
plt.legend()

plt.plot(y, x, 'y')

plt.xlabel('x')
plt.ylabel('y')
plt.plot(x, y, c='green', label='data')
plt.xlim([-6,6])
plt.axvline(x=0, c = 'black')
plt.axhline(y=0, c = 'black')
plt.title('Green')
plt.legend()

plt.show()
