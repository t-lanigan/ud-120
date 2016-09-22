#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
import numpy as np



### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#reduce size to increase speed
features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]

### create classifier
from sklearn.svm import SVC
clf = SVC(kernel="rbf", C=10000)
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)


#prettyPicture(clf,features_test,labels_test)

### use the trained classifier to predict labels for the test features
from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)

print "accuracy: ", acc




