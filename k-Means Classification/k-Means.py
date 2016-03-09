# Main Class
# Rahul Shrestha
# CMPS 470-Spring 2016
# Dr. John W. Burris
# https://github.com/rahulShrestha89/k-Means-Classification

# This program implements the k-Means clustering algorithm.

# Input Description:
#   First	line:	(N)	Number	of	examples
#   Second	line:	(X)	Number	of	attributes
#   Third	line:	(k)	Number	of	clusters	to	be	created
#   Following	N	lines	contain	X+1 values	containing	the	data	set,	separated	by	comma

import os


# create a dictionary of coordinates i.e. list with dictionaries of data set based on axis
# list = { [A:'X-Coordinate', B:'X-Coordinate'],[A:'Y-Coordinate', B:'Y-Coordinate'] }
def parse_coordinates():

    list_of_coordinate = list()

    list_value = [x.split(",") for x in all_examples]
    for col in range(1, len(list_value[0])):
        list_of_coordinate.append({l[0]: int(l[col]) for l in list_value})
    print(list_of_coordinate)

    return list_of_coordinate


def initial_centroids():

    # a dictionary to hold the centroids based on the number of clusters
    centroids = {}

    for i in range(number_of_clusters):
        centroids[i+1] = 1

    return 0

# get the file name from the user
file_name = input("Enter the input file name: ")

# look for file in the directory
try:
    fo = open(file_name, "r")
except IOError:
    print("Error: can\'t find file or read data.")
else:
    print("File found.")

    # check if the file is empty
    if os.stat(file_name).st_size <= 0:
        print("Not enough data in the input file.")
    else:
        # read and stores the number of examples, attributes, clusters.
        # as well as the examples
        with open(file_name, 'r') as file:

            number_of_examples = int(file.readline())
            number_of_attributes = int(file.readline())
            number_of_clusters = int(file.readline())

            # store all the unfiltered examples as list
            all_examples = file.readlines()

        examples = parse_coordinates()
        print(type(examples))

