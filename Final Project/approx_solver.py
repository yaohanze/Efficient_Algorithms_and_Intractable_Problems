import utils
import student_utils
import os, sys
import networkx as nx
import numpy as np
import random
import math


def solve(list_of_locations, list_of_homes, starting_car_location, adjacency_matrix, params=[]):
    """
    Write your algorithm here.
    Input:
        list_of_locations: A list of locations such that node i of the graph corresponds to name at index i of the list
        list_of_homes: A list of homes
        starting_car_location: The name of the starting location for the car
        adjacency_matrix: The adjacency matrix from the input file
    Output:
        A list of locations representing the car path
        A dictionary mapping drop-off location to a list of homes of TAs that got off at that particular location
        NOTE: both outputs should be in terms of indices not the names of the locations themselves
    """
    
	length = dict(nx.all_pairs_dijkstra_path_length(G))

	list_of_homes_index = student_utils.convert_locations_to_indices(list_of_homes, list_of_locations)
	
	# k is the prefixed number of clusters
	k = 10
	random.seed(123)

	centers = []
	centers.append(random.choice(list_of_homes_index))
	for i in range(2, k+1):
    	min_dist = []
    	for idx in list_of_homes_index:
        	min_d = math.inf
        	for center in centers:
            	min_d = min(min_d, length[center][idx])
        	min_dist.append(min_d)
    	new_center = list_of_homes_index[np.argmax(min_dist)]
    	centers.append(new_center)
	print(centers)

	
	

if __name__ == "__main__":
	main()