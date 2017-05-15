import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

x = np.arange(-5, 6)
y = np.arange(-5, 6)

plt.subplot(2,2,1)
plt.plot(x, y, 'r')

plt.xlabel('x')
plt.ylabel('y')
plt.plot(x, y, c='yellow', label='data')
plt.xlim([-6,6])
plt.axvline(x=0, c = 'black')
plt.axhline(y=0, c = 'black')
plt.title('Yellow')
plt.legend()

plt.subplot(2,2,2)
plt.plot(y, x, 'g')

plt.xlabel('x')
plt.ylabel('y')
plt.plot(x, y, c='blue', label='data')
plt.xlim([-6,6])
plt.axvline(x=0, c = 'black')
plt.axhline(y=0, c = 'black')
plt.title('Blue')
plt.legend()

plt.subplot(2,2,3)
plt.plot(x, y, 'b')

plt.xlabel('x')
plt.ylabel('y')
plt.plot(x, y, c='red', label='data')
plt.xlim([-6,6])
plt.axvline(x=0, c = 'black')
plt.axhline(y=0, c = 'black')
plt.title('Red')
plt.legend()

plt.subplot(2,2,4)
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
