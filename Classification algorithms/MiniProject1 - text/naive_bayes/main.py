'''
    Here we use Naive Bayes Classifier to identify emails
    by their authors.

    Authors and labels:
        - Sara has label 0
        - Chris has label 1
'''
import sys
from time import time
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
sys.path.append("../../pre_process/")
from create_training_testing_array import preprocess


features_train, features_test, labels_train, labels_test = preprocess()

print("Constructing NB classifier.")
# Construct Naive Bayes Classifier
clf = GaussianNB()

print("Training the model.")
t0 = time()
clf.fit(features_train, labels_train)
print("Training time:", round(time()-t0, 3), "s")

print("Making predictions.")
t0 = time()
pred = clf.predict(features_test)
print("Prediction time:", round(time()-t0, 3), "s")


print("Model prediction accuracy: ", round(accuracy_score(labels_test, pred) * 100, 2),'%')
