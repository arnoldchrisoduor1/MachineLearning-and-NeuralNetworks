# when we need to generate a dataset of simulated data.

# Creating a dataset designed to be used with linear regression.
from sklearn.datasets import make_regression

features, target, coefficient = make_regression(n_samples = 100,
                                                n_features = 3,
                                                n_informative = 3,
                                                n_targets = 1,
                                                noise = 0.0,
                                                coef = True,
                                                random_state=1)

# We can view out feature and target matrix.
print('Feature matrix\n', features[:3])
print('Target matrix\n', target[:3])