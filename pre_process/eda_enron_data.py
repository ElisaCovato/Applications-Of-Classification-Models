'''
    Below we run some exploratory data analysis on the enron_finances dataset
    to better understand the data.
'''

import pickle
import pandas as pd

enron_data = pickle.load(open("../data/enron_finances.pkl", "rb"))

print("\n There are %d executives in the Enron Finance Dataset:" % (len(enron_data.keys())))
print(list(enron_data.keys()))

print("\n Each executives entry has %d features:" % (len(enron_data["METTS MARK"].keys())))
print(list(enron_data["METTS MARK"].keys()))

total_poi = 0
for k, v in enron_data.items():
    if enron_data[k]['poi'] == True:
        total_poi += 1
print("\n There are %d POI - person of interest" % total_poi)

execs = [s for s in enron_data.keys() if ("SKILLING" in s) or ("LAY" in s) or ("FASTOW" in s) ]
print([(enron_data[person]['total_payments'],person) for person in execs] )