# k-Means-Classification
Implementation of k-Means Clustering Algorithm. 

Rahul Shrestha

Phase: beta development phase. 

File Structure: readme.txt, k-Means.py and Contains few test and output files!

Language: Python

Development Environment: Developed in PyCharm

Usage: My program is compatible with Python 3.x. There will be some issues running it on 2.x versions.

K-means (MacQueen, 1967) is one of the simplest unsupervised learning algorithms that solve the well known clustering problem. 
The procedure follows a simple and easy way to classify a given data set through a certain number of clusters (assume k clusters) 
fixed a priori. The main idea is to define k centroids, one for each cluster. These centroids shoud be placed in a cunning way because of
different location causes different result.

K-Means is relatively an efficient method. However, we need to specify the number of clusters, in advance and the final results are sensitive to initialization and often terminates at a local optimum. Unfortunately there is no global theoretical method to find the optimal number of clusters. A practical approach is to compare the outcomes of multiple runs with different k and choose the best one based on a predefined criterion. In general, a large k probably decreases the error but increases the risk of overfitting.

Algorithm

Place K points into the space represented by the objects that are being clustered. These points represent initial group centroids.
Assign each object to the group that has the closest centroid.
When all objects have been assigned, recalculate the positions of the K centroids.
Repeat Steps 2 and 3 until the centroids no longer move. This produces a separation of the objects into groups from which the metric to be minimized can be calculated.

