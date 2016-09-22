#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
#print len(enron_data.itervalues().next().keys())
#print len(enron_data)
#print enron_data.keys()
#print enron_data.itervalues().next()['poi']
count = 0.0
for key, value in enron_data.iteritems():
	if enron_data[key]['poi'] == 1:
	 	count = count + 1.0

print count

total_no = float(len(enron_data))
print total_no
print count/total_no

# no_of_features = len(enron_data[enron_data.keys()[0]])
# print no_of_features
# print len(enron_data)

# print 125.0/146
# print enron_data['PRENTICE JAMES']['total_stock_value']
# print enron_data['SKILLING JEFFREY K']['total_payments']
# print enron_data['LAY KENNETH L']['total_payments']
# print enron_data['FASTOW ANDREW S']['total_payments']

# print enron_data['COLWELL WESLEY']
# print enron_data.len()
