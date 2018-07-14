# -*- coding: utf-8 -*-
import numpy as np
from sklearn import preprocessing
data = np.array([[3, -1.5, -1.9, -4.3]])
data_standardized = preprocessing.scale(data)
data_scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
data_scaled = data_scaler.fit_transform(data)
data_normalized = preprocessing.normalize(data, norm='l1')
data_binarized = preprocessing.Binarizer(threshold=1.4).transform(data)
encoder = preprocessing.OneHotEncoder()
encoder.fit([[0, 2, 1, 12], [1, 3, 5, 3], [2, 3, 2, 12], [1, 2, 4,3]])
encoded_vector = encoder.transform([[2, 3, 5, 3]]).toarray()


print(data)
print(data_standardized)
print("Mean =", data_standardized.mean(axis=0))
print("Std deviation =", data_standardized.std(axis=0))
print("\nMin max scaled data =", data_scaled)
print("\nL1 normalized data =", data_normalized)
print("\nBinarized data =", data_binarized)
print("\nEncoded vector =", encoded_vector)