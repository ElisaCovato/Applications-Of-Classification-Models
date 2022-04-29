'''
    Here we use K-NN classifier to identify whether a
    car should go fast or slow according to the type of terrain.
'''

import matplotlib.pyplot as plt
import sys
from time import time
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
sys.path.append("../../pre_process/")
from prep_terrain_data import make_terrain_data
from vis_terrain_data import pretty_picture

print("Creating terrain dataset and split into test/train.")
features_train, labels_train, features_test, labels_test = make_terrain_data()

# The training data (features_train, labels_train) have both "fast" and "slow"
# points mixed together. Separate them so we can give them different colors
# in the scatterplot and identify them visually.
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii] == 0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii] == 0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii] == 1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii] == 1]

# Initial visualization
print("Initial visualization of training data.")
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color="b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color="r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show(block=False)





print("Constructing K-NN classifier.")
# Construct K-NN Classifier
clf = KNeighborsClassifier(n_neighbors=10)

print("Training the model.")
t0 = time()
clf.fit(features_train, labels_train)
print("Training time:", round(time()-t0, 3), "s")

print("Making predictions.")
t0 = time()
pred = clf.predict(features_test)
print("Prediction time:", round(time()-t0, 3), "s")


print("Model prediction accuracy: ", round(accuracy_score(labels_test, pred) * 100, 2),'%')

print("Creating k-NN model prediction visualisation.")
pretty_picture(clf, features_test, labels_test)


