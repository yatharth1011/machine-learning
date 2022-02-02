import matplotlib.pyplot as plt

from scipy import stats
# Import scipy and draw the line of Linear Regression.

ages = [5,7,8,7,2,17,2,9,4,11,12,9,6]
# Represents the x parameter. The ages of the cars.

speeds = [99,86,87,88,111,86,103,87,94,78,77,85,86]
# Represents the y parameter. The speeds of the cars.

# Execute a method that returns some important key values of Linear Regression:
slope, intercept, r, p, std_err = stats.linregress(ages, speeds)

# R for Relationship
# It is important to know how the relationship between the values of the x-axis and the values of the y-axis is, if there are no relationship the linear regression can not be used to predict anything.

# This relationship - the coefficient of correlation - is called r.

# The r value ranges from -1 to 1, where 0 means no relationship, and 1 (and -1) means 100% related.

# Python and the Scipy module will compute this value for you, all you have to do is feed it with the x and y values.

print("r = "+str(r))

# Note: The result -0.76 shows that there is a relationship, not perfect, but it indicates that we could use linear regression in future predictions.



# Create a function that uses the slope and intercept values to return a new value.
# This new value represents where on the y-axis the corresponding x value will be placed:
def myfunc(x):
  return slope * x + intercept

# Run each value of the x array through the function.
# This will result in a new array with new values for the y-axis:
mymodel = list(map(myfunc, ages))

# Draw the original scatter plot:
plt.scatter(ages, speeds)

# Draw the line of linear regression:
plt.plot(ages, mymodel)

# Display the diagram:
plt.show()


# Predict Future Values
# Now we can use the information we have gathered to predict future values.

# Example: Let us try to predict the speed of a 10 years old car.

# To do so, we need the same myfunc() function from the example above:

# def myfunc(x):
#   return slope * x + intercept

speed = myfunc(10)
# This predicts the speed of a 10 year old car.

print("Speed of a 10 year old car must be around "+str(speed))