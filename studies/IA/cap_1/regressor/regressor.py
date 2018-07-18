# -*- coding: utf-8 -*-
import sys
import numpy as np
filename = sys.argv[1]
X = []
Y = []
with open(filename, 'r') as f:
    for line in f.readlines():
        xt, yt = [float(i) for i in line.split(',')]
        X.append(xt)
        Y.append(yt)

num_training = int(0.8 * len(X))
print('num_training: ', num_training)
num_test = len(X) - num_training
print('num_test: ', num_training)

# Training data
X_train = np.array(X[:num_training]).reshape((num_training, 1))
print('X_train: \n', X_train)
Y_train = np.array(Y[:num_training])
print('Y_train: \n', Y_train)
# Test data
X_test = np.array(X[num_training:]).reshape((num_test,1))
print('X_test: \n', X_test)
Y_test = np.array(Y[num_training:])
print('Y_test: \n', Y_test)
from sklearn import linear_model

# Create linear regression object
linear_regressor = linear_model.LinearRegression()

# Train the model using the training
linear_regressor.fit(X_train, Y_train)

import matplotlib.pyplot as plt

y_train_pred = linear_regressor.predict(X_train)
print('y_train_pred: \n', y_train_pred)
plt.scatter(X_train, Y_train, color='green')
plt.plot(X_train, y_train_pred, color='black', linewidth=4)
plt.title('Training data')
plt.show()





