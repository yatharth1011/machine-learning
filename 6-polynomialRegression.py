# If your data points clearly will not fit a linear regression (a straight line through all data points), it might be ideal for polynomial regression.

# Polynomial regression, like linear regression, uses the relationship between the variables x and y to find the best way to draw a line through the data points.


# In the example below, we have registered 18 cars as they were passing a certain tollbooth.

# We have registered the car's speed, and the time of day (hour) the passing occurred.

# The x-axis represents the hours of the day and the y-axis represents the speed:


import matplotlib.pyplot as plt
import numpy
from sklearn.metrics import r2_score

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
# Hour of the day

y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
# Speed of the car

# NumPy has a method that lets us make a polynomial model:
mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

# Then specify how the line will display, we start at position 1, and end at position 22:
myline = numpy.linspace(1, 22, 100)

# Draw the original scatter plot:
plt.scatter(x, y)

# Draw the line of polynomial regression:
plt.plot(myline, mymodel(myline))

# Display the diagram:
plt.show()



# R-Squared
# It is important to know how well the relationship between the values of the x- and y-axis is, if there are no relationship the polynomial regression can not be used to predict anything.

# The relationship is measured with a value called the r-squared.

# The r-squared value ranges from 0 to 1, where 0 means no relationship, and 1 means 100% related.

# Python and the Sklearn module will compute this value for you, all you have to do is feed it with the x and y arrays:

r2 = r2_score(y, mymodel(x))
if round(r2) == 1:
	print("Data is good to go for polynomial regression.")
else:
	print("Data incompatible for polynomial regression.")



# Predict Future Values
# Now we can use the information we have gathered to predict future values.

# Example: Let us try to predict the speed of a car that passes the tollbooth at around 17 P.M:

# To do so, we need the same mymodel array from the example above:

# mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

speed = mymodel(17)
print("The predicted speed of a car that passes the tollbooth at around 17 P.M: "+str(speed))