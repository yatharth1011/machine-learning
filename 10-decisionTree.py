import warnings
warnings.filterwarnings("ignore")
# Suppress warnings.

import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

df = pandas.read_csv("shows.csv")


# To make a decision tree, all data has to be numerical.

# We have to convert the non numerical columns 'Nationality' and 'Go' into numerical values.

# Pandas has a map() method that takes a dictionary with information on how to convert the values.

# {'UK': 0, 'USA': 1, 'N': 2}

# Means convert the values 'UK' to 0, 'USA' to 1, and 'N' to 2.

d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)


# Then we have to separate the feature columns from the target column.

# The feature columns are the columns that we try to predict from, and the target column is the column with the values we try to predict.

features = ['Age', 'Experience', 'Rank', 'Nationality']

# X is the feature columns, y is the target column:

X = df[features]
y = df['Go']

# Now we can create the actual decision tree, fit it with our details, and save a .png file on the computer:

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)


# Predict Values
# We can use the Decision Tree to predict new values.

# Example: Should I go see a show starring a 64 years old American comedian, with 40 years of experience, and a comedy ranking of 4?

if dtree.predict([[64, 40, 4, 2]]) == 0:
	print("No, don't go.")
else:
	print("Yes, you should go.")