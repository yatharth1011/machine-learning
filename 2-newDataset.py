import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 100000)
# Random dataset with 100000 float values between 0 and 5

plt.hist(x, 100)
# Plotting histogram with 100 bars

plt.show()