from sklearn import preprocessing

label_encoder = preprocessing.LabelEncoder()
imput_classes = ['python', 'php', 'c++', 'c#']
label_encoder.fit(imput_classes)

for number, name in enumerate(label_encoder.classes_):
    print("\n Number {}; Name: {}".format(number, name))