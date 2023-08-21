import os
import sys
sys.path.append('..')
sys.path.append('../..')
import argparse
import utils
import random
import math

from student_utils import *
"""
======================================================================
  Complete the following function.
======================================================================
"""

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
    list_of_homes_index = convert_locations_to_indices(list_of_homes, list_of_locations)
    starting_location_index = convert_locations_to_indices([starting_car_location], list_of_locations)

    list_of_locations, list_of_homes, starting_car_location, adjacency_matrix
    G, message = adjacency_matrix_to_graph(adjacency_matrix)
    length = dict(nx.all_pairs_dijkstra_path_length(G))

    list_of_homes_index = convert_locations_to_indices(list_of_homes, list_of_locations)
    if len(list_of_homes) == 1:
        dist = [length[starting_location_index[0]][k] for k in list_of_homes_index]
        next_location = list_of_homes_index[np.argmin(dist)]
        full_path = nx.dijkstra_path(G, starting_location_index[0], next_location)+nx.dijkstra_path(G, next_location, starting_location_index[0])[1:]
        dropoff_mapping = {}
        dropoff_mapping[next_location] = list_of_homes_index
        return full_path, dropoff_mapping
    costs = []
    for k in range(1, len(list_of_homes), 8):
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

        # add starting point to the k centers
        #centers.append(starting_location_index[0])
    
        dropoff_mapping = {}
        for k in centers:
            dropoff_mapping[k] = []

        for i in list_of_homes_index:
            dist = [length[i][k] for k in centers]
            center = centers[np.argmin(dist)]
            dropoff_mapping[center].append(i)           


        # greedily find a circle
        path = []
        path.append(starting_location_index[0])
        current = starting_location_index[0]
        while len(centers)>0:
            dist = [length[current][k] for k in centers]
            next_location = centers[np.argmin(dist)]
            path.append(next_location)
            centers.remove(next_location)
            current = next_location
        path.append(starting_location_index[0])

        full_path = []
        for i in range(len(path)-1):
            full_path += nx.dijkstra_path(G, path[i], path[i+1])
            full_path.pop()
        full_path.append(starting_location_index[0])
        #optimize over range of number of ceners

        costs.append(cost_of_solution(G, full_path, dropoff_mapping)[0])
    k = np.argmin(costs)
    k = list(range(1, len(list_of_homes), 8))[k]
    #print(k)
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
    #print(centers)

    # add starting point to the k centers
    #centers.append(starting_location_index[0])


    dropoff_mapping = {}
    for k in centers:
        dropoff_mapping[k] = []

    #print(starting_car_location)
    for i in list_of_homes_index:
        dist = [length[i][k] for k in centers]
        center = centers[np.argmin(dist)]
        dropoff_mapping[center].append(i)            

    #print(dropoff_mapping)


    # greedily find a circle
    path = []
    path.append(starting_location_index[0])
    current = starting_location_index[0]
    while len(centers)>0:
        dist = [length[current][k] for k in centers]
        next_location = centers[np.argmin(dist)]
        path.append(next_location)
        centers.remove(next_location)
        current = next_location
    path.append(starting_location_index[0])
    #print(path)

    full_path = []
    for i in range(len(path)-1):
        full_path += nx.dijkstra_path(G, path[i], path[i+1])
        full_path.pop()
    full_path.append(starting_location_index[0])
    #print(full_path)
    return full_path, dropoff_mapping

"""
======================================================================
   No need to change any code below this line
======================================================================
"""

"""
Convert solution with path and dropoff_mapping in terms of indices
and write solution output in terms of names to path_to_file + file_number + '.out'
"""
def convertToFile(path, dropoff_mapping, path_to_file, list_locs):
    string = ''
    for node in path:
        string += list_locs[node] + ' '
    string = string.strip()
    string += '\n'

    dropoffNumber = len(dropoff_mapping.keys())
    string += str(dropoffNumber) + '\n'
    for dropoff in dropoff_mapping.keys():
        strDrop = list_locs[dropoff] + ' '
        for node in dropoff_mapping[dropoff]:
            strDrop += list_locs[node] + ' '
        strDrop = strDrop.strip()
        strDrop += '\n'
        string += strDrop
    utils.write_to_file(path_to_file, string)

def solve_from_file(input_file, output_directory, params=[]):
    print('Processing', input_file)

    input_data = utils.read_file(input_file)
    num_of_locations, num_houses, list_locations, list_houses, starting_car_location, adjacency_matrix = data_parser(input_data)
    car_path, drop_offs = solve(list_locations, list_houses, starting_car_location, adjacency_matrix, params=params)

    basename, filename = os.path.split(input_file)
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    output_file = utils.input_to_output(input_file, output_directory)

    convertToFile(car_path, drop_offs, output_file, list_locations)


def solve_all(input_directory, output_directory, params=[]):
    input_files = utils.get_files_with_extension(input_directory, 'in')

    for input_file in input_files:
        solve_from_file(input_file, output_directory, params=params)


if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Parsing arguments')
    parser.add_argument('--all', action='store_true', help='If specified, the solver is run on all files in the input directory. Else, it is run on just the given input file')
    parser.add_argument('input', type=str, help='The path to the input file or directory')
    parser.add_argument('output_directory', type=str, nargs='?', default='.', help='The path to the directory where the output should be written')
    parser.add_argument('params', nargs=argparse.REMAINDER, help='Extra arguments passed in')
    args = parser.parse_args()
    output_directory = args.output_directory
    if args.all:
        input_directory = args.input
        solve_all(input_directory, output_directory, params=args.params)
    else:
        input_file = args.input
        solve_from_file(input_file, output_directory, params=args.params)
