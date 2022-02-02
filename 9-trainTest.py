import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
# The x axis represents the number of minutes before making a purchase.

y = numpy.random.normal(150, 40, 100) / x
# The y axis represents the amount of money spent on the purchase.



# The training set should be a random selection of 80% of the original data.

# The testing set should be the remaining 20%.

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

# Display the same scatter plot with the training set:

# plt.scatter(train_x, train_y)
# plt.show()

# Display the Testing Set:

# plt.scatter(test_x, test_y)
# plt.show()


# Let us draw a line of polynomial regression.


# Training
mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

myline = numpy.linspace(0, 6, 100)

plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
# plt.show()


# Testing
test_r2 = r2_score(test_y, mymodel(test_x))
if round(test_r2) == 1:
	print("Your model can be used to predict future values.")
else:
	print("Testing Data incompatible for polynomial regression.")

# Prediction
# How much money will a buying customer spend, if she or he stays in the shop for 5 minutes?
print("The customer should spend "+str(mymodel(5))+", if she or he stays in the shop for 5 minutes.")