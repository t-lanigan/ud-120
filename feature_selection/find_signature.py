#!/usr/bin/python

import pickle
import numpy
from time import time
numpy.random.seed(42)


### The words (features) and authors (labels), already largely processed.
### These files should have been created from the previous (Lesson 10)
### mini-project.
words_file = "../text_learning/your_word_data.pkl" 
authors_file = "../text_learning/your_email_authors.pkl"
word_data = pickle.load( open(words_file, "r"))
authors = pickle.load( open(authors_file, "r") )



### test_size is the percentage of events assigned to the test set (the
### remainder go into training)
### feature matrices changed to dense representations for compatibility with
### classifier functions in versions 0.15.2 and earlier
from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(word_data, authors, test_size=0.1, random_state=42)

from sklearn.feature_extraction.text import TfidfVectorizer

print "performing tfidf vectorization..."
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             stop_words='english')
features_train = vectorizer.fit_transform(features_train)
features_test  = vectorizer.transform(features_test).toarray()


### a classic way to overfit is to use a small number
### of data points and a large number of features;
### train on only 150 events to put ourselves in this regime

print 'training using 150 emails..'
features_train150 = features_train[:150].toarray()
labels_train150   = labels_train[:150]

from sklearn import tree
from sklearn.metrics import accuracy_score

clf = tree.DecisionTreeClassifier()
t0 = time()
clf.fit(features_train150, labels_train150)
print "training time:", round(time()-t0, 3), "s"

t1 = time()
pred = clf.predict(features_test)
print "predicting time:", round(time()-t1, 3), "s"

print accuracy_score(pred,labels_test)

#assign feature importances so it's not calculated each time in for loop.
feature_importances = clf.feature_importances_

#print the feature number that has a large importance value above the threshold
threshold = 0.2
for i in range(len(feature_importances)):
	if feature_importances[i] > threshold:
		print feature_importances[i]
		print i
		print 'signature word: ' + vectorizer.get_feature_names()[i]





