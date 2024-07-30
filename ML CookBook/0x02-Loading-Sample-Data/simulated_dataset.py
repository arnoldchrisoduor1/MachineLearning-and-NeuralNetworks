# when we need to generate a dataset of simulated data.

# Creating a dataset designed to be used with linear regression.
from sklearn.datasets import make_regression
from sklearn.datasets import make_classification
from sklearn.datasets import make_blobs

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

# Generate features matrix and target vector
features, target = make_classification(n_samples = 100,
                                        n_features = 3,
                                        n_informative = 3,
                                        n_redundant = 0,
                                        n_classes = 2,
                                        weights = [.25, .75],
                                        random_state = 1)
# View feature matrix and target vector
print('Feature Matrix\n', features[:3])
print('Target Vector\n', target[:3])

# Generate features matrix and target vector
features, target = make_blobs(n_samples = 100,
                                n_features = 2,
                                centers = 3,
                                cluster_std = 0.5,
                                shuffle = True,
                                random_state = 1)
# View feature matrix and target vector
print('Feature Matrix\n', features[:3])
print('Target Vector\n', target[:3])
