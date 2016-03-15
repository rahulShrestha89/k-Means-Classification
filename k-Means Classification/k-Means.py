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
import statistics


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

    if first_loop:
        examples = parse_examples()
        centroids = initial_centroids()

        # stores the clusters as list of dictionaries
        # where each dictionary is a cluster and consists of examples(data sets)
        # First: get the cluster centers and append to the list
        clusters_list = [{ki: v} for ki, v in centroids.items()]

        # stores distance between a data set and all other centroids
        # as {"centroid_key" : distance between data and centroid}
        distance_dict = {}

        # loop through all the examples
        for i_key in examples:
            # loop through both of the centroids i.e. cluster centers
            for j_key in centroids:
                distance_dict[j_key] = calculate_euclidean_distance(examples[i_key], centroids[j_key])

            # find key with the minimum distance value
            cluster_key = min(distance_dict, key=distance_dict.get)

            # find the dictionary in the cluster_list
            # that contains cluster_key, and append example to
            # that dictionary
            for index, values in enumerate(clusters_list):
                if cluster_key in values:    # finds the dictionary with cluster_key
                    values[i_key] = examples[i_key]

        print(clusters_list)
        return clusters_list

    else:
        examples = initial_clusters
        centroids = recalculate_centroids()

        next_clusters_list = [{ki: v} for ki, v in centroids.items()]

        next_distance_dict = {}

        for index, dictionary in enumerate(examples):
            for i_key in dictionary:
                for j_key in centroids:
                    next_distance_dict[j_key] = calculate_euclidean_distance(dictionary[i_key], centroids[j_key])

                # find key with the minimum distance value
                cluster_key = min(next_distance_dict, key=next_distance_dict.get)

                for ind, values in enumerate(next_clusters_list):
                    if cluster_key in values:    # finds the dictionary with cluster_key
                        values[i_key] = dictionary[i_key]

        # remove the cluster centers from the cluster
        for key_i in centroids:
            for index, dic in enumerate(next_clusters_list):
                if key_i in dic:
                    dic.pop(key_i)

        print(next_clusters_list)
        return next_clusters_list


# get the average of the clusters and
# assign different other k number of cluster centroids
# keep doing until the cluster centers are stable(fixed)
def recalculate_centroids():

    clusters = initial_clusters

    # stores new cluster centers in a dictionary
    centroids = {}

    for index, dictionary in enumerate(clusters):        # loop through cluster list
        centroids[index] = find_average(dictionary)

    return centroids


# calculates the average of the cluster dimension points
def find_average(dictionary):

    return tuple(statistics.mean(dictionary[key][i] for key in dictionary) for i in range(number_of_attributes))


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

        first_loop = True
        looking = True

        # for no attributes or clusters
        if number_of_attributes == 0 or number_of_clusters == 0:
            print("\nNot enough information for clustering.")

        # for equal number of examples and clusters
        elif number_of_examples == number_of_clusters:
            inc = 1
            for k, value in parse_examples().items():
                print("\nCluster {} :>".format(inc))
                print("{} = {}\n".format(k, value))
                inc += 1

        # for clusters greater than examples
        elif number_of_clusters > number_of_examples:
            print("\nClusters cannot be greater than examples.")

        # other cases
        else:
            initial_clusters = make_clusters()

            while looking:
                if first_loop:
                    previous_centroids = recalculate_centroids()
                    if initial_centroids() == previous_centroids:
                        looking = False
                    first_loop = False

                else:
                    old_centroids = previous_centroids
                    initial_clusters = make_clusters()
                    updated_centroids = recalculate_centroids()
                    if old_centroids != updated_centroids:
                        looking = False




