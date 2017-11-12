###########################################
# Description: Takes the csv input from mySQL and changes it into a dictionary 
# 	           Takes that dictionary and runs linear regression on it to find the 
#              weights associated with each habit. This allows you to see how each 
#              habit correlates to the persons mood. 
#
#              By: Milos Bijelic 
#
#              Version: 0.1.0	-	Initial release, prototype 
###########################################
import numpy as np 
import pandas as pd 
import scipy.stats as stats
import matplotlib.pyplot as plt 
import sklearn 
import csv 
import pprint
import sys

def csv_dict_list(file):
    reader = csv.DictReader(open('format_ex.csv', 'r'))
    dict_list = []

    for line in reader: 
        dict_list.append(line)
    return dict_list;

device_values = csv_dict_list(sys.argv[1])
pprint.pprint(device_values)