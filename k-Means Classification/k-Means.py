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


# create a dictionary of coordinates i.e. keys with multiple values
# dict = {"A":'X-Coordinate,Y-Coordinate', "B":'X-Coordinate,Y-Coordinate'}
def parse_examples():

    # stores the examples in a dictionary
    # key: [rest of the integer values]
    coordinates = {}
    for values in all_examples:
        split_list = values.split(',')
        coordinates[split_list[0]] = [int(val.rstrip()) for val in split_list[1:]]

    return coordinates


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

        print(parse_examples())
