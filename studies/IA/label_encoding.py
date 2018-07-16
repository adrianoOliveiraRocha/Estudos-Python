# -*- coding: utf-8 -*-
from sklearn import preprocessing

label_encoder = preprocessing.LabelEncoder()
imput_class = ['audi', 'ford', 'audi', 'toyota', 'ford', 'bmw']
label_encoder.fit(imput_class)
for number, name in enumerate(label_encoder.classes_):
    print(name, '-->', number)

labels = ['toyota', 'ford', 'audi']
encoded_labels = label_encoder.transform(labels)
print("\nLabels = ", labels)
print("Encoded labels =", list(encoded_labels))
