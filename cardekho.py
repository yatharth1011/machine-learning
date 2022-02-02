import warnings
warnings.filterwarnings("ignore")

import pandas
from scipy import stats
from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy

df = pandas.read_csv("cardekho.csv")

d1 = {'CNG': 0, 'Diesel': 1, 'Electric': 2, 'LPG': 3, 'Petrol': 4}
df['fuel'] = df['fuel'].map(d1)
d2 = {'Dealer': 0, 'Individual': 1, 'Trustmark Dealer': 2}
df['seller_type'] = df['seller_type'].map(d2)
d3 = {'Manual': 0, 'Automatic': 1}
df['transmission'] = df['transmission'].map(d3)
d4 = {'First Owner': 0, 'Second Owner': 1, 'Third Owner': 2, 'Fourth & Above Owner': 3, 'Test Drive Car': 4}
df['owner'] = df['owner'].map(d4)

features = ['year', 'km_driven', 'fuel', 'seller_type', 'transmission', 'owner']

X = df[features]
y = df['selling_price']

regr = linear_model.LinearRegression()
regr.fit(X, y)

# 2014, 120000, 'Petrol', 'Individual', 'Automatic', 'First Owner'
predictedSellingPrice = regr.predict([[2014, 120000, 4, 1, 1, 0]])

print("An Automatic car purchased in 2014 with 120000 kms driven by its First Owner should be sold at ₹{:,}".format(round(predictedSellingPrice[0])))

input_year = input("Year? ")
input_km_driven = input("kms driven? ")
input_fuel = input("Fuel type? CNG - 0, Diesel - 1, Electric - 2, LPG - 3, Petrol - 4: ")
input_seller_type = input("Seller Type? Dealer - 0, Individual - 1, Trustmark Dealer - 2: ")
input_transmission = input("Manual or Automatic? Manual - 0, Automatic - 1: ")
input_owner = input("First Owner - 0/Second Owner - 1/Third Owner - 2/Fourth & Above Owner - 3/Test Drive Car? - 4: ")

predictedSellingPrice = regr.predict([[
	input_year, 
	input_km_driven, 
	input_fuel, 
	input_seller_type, 
	input_transmission, 
	input_owner
]])

print("Selling Price should be ₹{:,}".format(abs(round(predictedSellingPrice[0]))))