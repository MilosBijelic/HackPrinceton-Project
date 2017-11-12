###########################################
# Description: Takes the csv input from mySQL and changes it into a dictionary 
# 	           Takes that dictionary and runs linear regression on it to find the 
#              weights associated with each habit. This allows you to see how each 
#              habit correlates to the persons mood. 
#
#              Version: 0.1.0	-	Initial release, prototype 
###########################################
import numpy as np 
import pandas as pd 
# import scipy.stats as stats
# import matplotlib.pyplot as plt 
# import sklearn 
# import csv 
# import pprint
# import sys

# Extracts the data from the CSV file and puts it into a useful form'[[]

features = ["Study", "Coffee", "Exercise", "Good Meal", "Shopping", "Date", "Movies", "Gaming", "Mood"]

def get_feature_num(features):
	size = len(features)
	# print("Array is %d long" % size)
	return size

def create_data_frame(features, num_of_features):
	data_frame = {}

	data = np.readcsv("example_data_set.csv", delimiter=',')
	data["Study"]
	# while num_of_features > 0:
	# 	i = 0
	# 	habits = [[]] * get_feature_num(features)

	# 	num_of_features= num_of_features - 1
	# 	i += 1
	# return data_frame

if __name__ == '__main__':
    get_feature_num(features)
    create_data_frame(features, get_feature_num(features))
