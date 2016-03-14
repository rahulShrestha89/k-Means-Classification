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
import math


# create a dictionary of coordinates i.e. keys with multiple values
# dict = {"A":[X-Coordinate,Y-Coordinate'], "B":[X-Coordinate,Y-Coordinate]}
def parse_examples():

    # stores the examples in a dictionary
    # key: [rest of the integer values]
    coordinates = {}
    for values in all_examples:
        split_list = values.split(',')
        coordinates[split_list[0]] = [float(val.rstrip()) for val in split_list[1:]]

    return coordinates


# centroids are the center of the clusters,
# so the total number of centroids will be equal to the
# total number of clusters
def initial_centroids():

    # a dictionary to hold the centroids based on the number of clusters
    centroids = {}

    # select (number of clusters) centroids from the text file (dictionary is unordered)
    for values in all_examples[:number_of_clusters]:
        split_list = values.split(',')
        centroids[split_list[0]] = [float(val.rstrip()) for val in split_list[1:]]

    return centroids


# calculate Euclidean distance between data sets
# and a cluster center (centroid)
def calculate_euclidean_distance(example, centroid):

    distance = 0

    # make sure that list size is equal
    if len(example) != len(centroid):
        print("Not the same Dimensions")
    else:
        for i in range(len(example)):
            distance += (example[i]-centroid[i]) ** 2
    return math.sqrt(distance)


# Assign objects(examples) to their closest cluster center (centroids)
# according to the Euclidean distance function
def make_clusters():

    examples = parse_examples()     # stores parsed examples from text file
    centroids = initial_centroids()     # stores initial centroids

    # stores the clusters as list of dictionaries
    # where each dictionary is a cluster and consists of examples(data sets)
    clusters_list = []

    # stores distance between a data set and all other centroids
    # as {"centroid_key" : distance between data and centroid}
    distance_dict = {}

    # get the cluster centers
    # and append to the list
    clusters_list = [{k: v} for k, v in centroids.items()]
    print(clusters_list)

    # loop through all the examples
    for i_key in examples:
        # loop through both of the centroids i.e. cluster centers
        for j_key in centroids:
            distance_dict[j_key] = calculate_euclidean_distance(examples[i_key], centroids[j_key])

        # Consider two cluster centers with two different data set.
        # And, If data_A is closer to cluster_A than cluster_B
        # then cluster_A contains data_A

        # find key with the minimum distance value
        cluster = min(distance_dict, key=distance_dict.get)
        # print(cluster)

        # holds the clusters dict and appends to the list
        cluster_dict = {}

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

        make_clusters()

