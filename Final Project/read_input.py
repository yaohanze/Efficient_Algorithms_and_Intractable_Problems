import utils
import student_utils
import os, sys
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def main():
	#The following code is an sample code for extracting data from 50.in, 100.in, 200.in
	path = os.getcwd()
	files = utils.get_files_with_extension(path, '.in')
	number_of_locations_list = []
	number_of_houses_list = []
	list_of_locations_list = []
	list_of_houses_list = []
	starting_location_list = []
	adjacency_matrix_list = []
	list_of_houses_list_index = []
	starting_location_list_index = []
	i = 0
	for i in range(len(files)):
		data = utils.read_file(files[i])
		number_of_locations, number_of_houses, list_of_locations, list_of_houses, starting_location, adjacency_matrix = student_utils.data_parser(data)
		number_of_locations_list.append(number_of_locations)
		number_of_houses_list.append(number_of_houses)
		list_of_locations_list.append(list_of_locations)
		list_of_houses_list.append(list_of_houses)
		starting_location_list.append(starting_location)
		adjacency_matrix_list.append(adjacency_matrix)
		list_of_houses_index = student_utils.convert_locations_to_indices(list_of_houses, list_of_locations)
		starting_location_index = student_utils.convert_locations_to_indices([starting_location], list_of_locations)
		list_of_houses_list_index.append(list_of_houses_index)
		starting_location_list_index += starting_location_index
	

if __name__ == "__main__":
	main()