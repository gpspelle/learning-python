import matplotlib.pyplot as plt
import numpy as np

# Olympic's data from 100 metres freestyle over the years
# Notes: 1900, 1904, 1916, 1940 and 1944 aren't on the set of years 
years = [1896, 1908, 1912, 1920, 1924, 1928, 1932, 1936, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016]
best_time = [82.2, 65.6, 63.4, 60.4, 59, 58.6, 58.2, 57.6, 57.3, 57.4, 55.4, 55.2, 53.4, 52.2, 51.22, 49.99, 50.40, 49.80, 48.63, 49.02, 48.74, 48.30, 48.17, 47.21, 47.52, 47.58]

order = int(input("Choose a order for your polynomial regression (2, 3, ...): "))
order += 1

# Getting coefficients
k = np.polyfit(years, best_time, order)

x = np.linspace(years[0], years[-1])

fig = plt.figure()
fig.suptitle('Polynomial regression for Olympic 100 metres freestyle', fontsize=14)
plt.plot(x, np.poly1d(k)(x))
plt.plot(years, best_time)
plt.xlabel("Year of competition")
plt.ylabel("Seconds")
plt.show()

