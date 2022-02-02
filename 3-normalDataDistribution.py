import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 100000)
# We use the array from the numpy.random.normal() method, with 100000 values.

# We specify that the mean value is 5.0, and the standard deviation is 1.0.

# Meaning that the values should be concentrated around 5.0, and rarely further away than 1.0 from the mean.

plt.hist(x, 100)
# Draw a histogram with 100 bars.

plt.show()

mean = numpy.mean(x);
std = numpy.std(x);

print("Mean = "+str(round(mean)))
print("Standard Deviation = "+str(round(std)))