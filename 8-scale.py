# Scale Features
# When your data has different values, and even different measurement units, it can be difficult to compare them. What is kilograms compared to meters? Or altitude compared to time?

# The answer to this problem is scaling. We can scale data into new values that are easier to compare.

import warnings
warnings.filterwarnings("ignore")
# Suppress warnings.

import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

df = pandas.read_csv("cars2.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']


# The standardization method uses this formula:

# z = (x - u) / s

# Where z is the new value, x is the original value, u is the mean and s is the standard deviation.


scaledX = scale.fit_transform(X)


regr = linear_model.LinearRegression()
regr.fit(scaledX, y)

# Predict the CO2 emission from a 1.3 liter car that weighs 2300 kilograms:
scaled = scale.transform([[2300, 1.3]])

predictedCO2 = regr.predict([scaled[0]])
print("The CO2 emission from a 1.3 liter car that weighs 2300 kilograms: "+str(predictedCO2))