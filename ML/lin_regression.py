import matplotlib.pyplot as plt
import numpy as np

# Olympic's data from 100 metres freestyle over the years
# Notes: 1900, 1904, 1916, 1940 and 1944 aren't on the set of years 
years = [1896, 1908, 1912, 1920, 1924, 1928, 1932, 1936, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016]
best_time = [82.2, 65.6, 63.4, 60.4, 59, 58.6, 58.2, 57.6, 57.3, 57.4, 55.4, 55.2, 53.4, 52.2, 51.22, 49.99, 50.40, 49.80, 48.63, 49.02, 48.74, 48.30, 48.17, 47.21, 47.52, 47.58]

# Least Square method
xt_med = 0
x_sqr_med = 0
x_med = sum(years)/float(len(years)) 
t_med = sum(best_time)/float(len(best_time))

for i in range(0, len(best_time)):
	xt_med += best_time[i] * years[i]
	x_sqr_med += years[i] ** 2

xt_med /= float(len(years))
x_sqr_med /= float(len(years))	

angular_coef = (xt_med - x_med*t_med) / (x_sqr_med - x_med ** 2)
linear_coef = t_med - angular_coef * x_med

x = np.linspace(years[0], years[-1])
y = angular_coef * x + linear_coef

fig = plt.figure()
fig.suptitle('Linear regression for Olympic 100 metres freestyle', fontsize=14)
plt.plot(x, y)
plt.plot(years, best_time)
plt.xlabel("Year of competition")
plt.ylabel("Seconds")
plt.show()

