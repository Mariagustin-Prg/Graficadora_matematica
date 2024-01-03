import matplotlib.pyplot as plt
import numpy as np
import random

serie_x = np.linspace(0, 101, 1000)
serie_y = [x ** 2 for x in serie_x]

plt.figure(figsize=(8, 6))
plt.plot(serie_x, serie_y, color='r')

plt.show()
