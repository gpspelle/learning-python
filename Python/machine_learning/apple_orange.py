# Importing libs
from sklearn import tree

# data test
features = [[140, 1], [130, 1], [150, 0], [170, 0]]
labels = [0, 0, 1, 1]

# declaring a tree classifier
classifier = tree.DecisionTreeClassifier()

# training my classifier
classifier = classifier.fit(features, labels)

# predict if a entry is an orange or an apple
print classifier.predict([[139, 0]])
