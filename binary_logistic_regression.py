import numpy as np

class LogisticRegression:
    def __init__(self, learning_rate = 0.001, n_inters=1000):
        self.lr = learning_rate
        self.n_iters = n_inters
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape

        #init parameters
        self.weights = np.zeros(n_features)
        self.bias = 0

        #gradient descent

        for _ in range(self.n_iters):
            #approximating value of y with linear combination of weights and x, plus bias.
            linear_model = np.dot(X, self.weights) +self.bias
            #applying sigmoid function to the answer.