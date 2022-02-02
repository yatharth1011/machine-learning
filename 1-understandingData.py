import numpy
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed)
y = numpy.median(speed)
z = stats.mode(speed).mode[0]
w = numpy.std(speed)
v = numpy.var(speed)
u = numpy.percentile(speed, 75)

print("Mean = "+str(x))
print("Median = "+str(y))
print("Mode = "+str(z))
print("Standard Deviation = "+str(w))
print("Variation = "+str(v))
print("75% are "+str(u)+" or less.")