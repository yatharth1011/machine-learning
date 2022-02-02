import warnings
warnings.filterwarnings("ignore")
# Suppress warnings.


import pandas
# In Python we have modules that will do the work for us. Start by importing the Pandas module.


# We will use some methods from the sklearn module, so we will have to import that module as well:
from sklearn import linear_model

df = pandas.read_csv("cars.csv")
# The Pandas module allows us to read csv files and return a DataFrame object.



# Then make a list of the independent values and call this variable X.

# Put the dependent values in a variable called y.

X = df[['Weight', 'Volume']]
y = df['CO2']
# It is common to name the list of independent values with a upper case X, and the list of dependent values with a lower case y.



# From the sklearn module we will use the LinearRegression() method to create a linear regression object.

# This object has a method called fit() that takes the independent and dependent values as parameters and fills the regression object with data that describes the relationship:

regr = linear_model.LinearRegression()
regr.fit(X, y)

# Now we have a regression object that are ready to predict CO2 values based on a car's weight and volume:

#predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2 = regr.predict([[2300, 1300]])

# We have predicted that a car with 1.3 liter engine, and a weight of 2300 kg, will release approximately 107 grams of CO2 for every kilometer it drives.
print(predictedCO2);



# Coefficient
# The coefficient is a factor that describes the relationship with an unknown variable.

# Example: if x is a variable, then 2x is x two times. x is the unknown variable, and the number 2 is the coefficient.

# In this case, we can ask for the coefficient value of weight against CO2, and for volume against CO2. The answer(s) we get tells us what would happen if we increase, or decrease, one of the independent values.

print("Coeffecients = "+str(regr.coef_))

# The result array represents the coefficient values of weight and volume.

# Weight: 0.00755095
# Volume: 0.00780526

# These values tell us that if the weight increase by 1kg, the CO2 emission increases by 0.00755095g.

# And if the engine size (Volume) increases by 1 cm3, the CO2 emission increases by 0.00780526 g.