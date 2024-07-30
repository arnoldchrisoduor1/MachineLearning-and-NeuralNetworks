# we want to load data from preexisting sample dataset from the scikit-lean library.

from sklearn import datasets

# Loading the digits dataset.
digits = datasets.load_digits()

# Creating a feature matrix.
features = digits.data

# Creating a target vector.
target = digits.target

# Viewing the first observation.
print(features[0])