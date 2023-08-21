import utils
import os, sys
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np 
import random

def is_triangle_inequality(G):
	gm = nx.adjacency_matrix(G)
	length = dict(nx.all_pairs_dijkstra_path_length(G))
	for i in range(len(G)):
		for j in range(len(G)):
			for k in range(len(G)):
				if gm[i,j]>(length[i][k]+length[k][j]):
					return False
	return True                	

def generate_random_graph(n):
	G = nx.gnp_random_graph(n, 0.7)
	for (u, v, w) in G.edges(data=True):
		w['weight'] = round(1 + random.uniform(0,1), 1)
	valid = nx.is_connected(G) and is_triangle_inequality(G)
	while not valid:
		G = nx.gnp_random_graph(n, 0.7)
		for (u, v, w) in G.edges(data=True):
			w['weight'] = round(1 + random.uniform(0,1), 1)
		valid = nx.is_connected(G) and is_triangle_inequality(G)
	matrix = nx.to_numpy_matrix(G)
	return matrix

def main():
	path = os.getcwd()
	num_locs = [50, 100, 200]
	num_tas = [25, 50, 100]
	for i in range(3):
		num_loc = num_locs[i]
		num_ta = num_tas[i]
		file = open("%d.in" % num_loc, "w")
		file.write("%d\r\n" % num_loc)
		file.write("%d\r\n" % num_ta)
		for j in range(num_loc):
			if j == num_loc - 1:
				file.write("loc%d\r\n" % j)
			else:
				file.write("loc%d " % j)
		for k in range(num_ta):
			if k == num_ta - 1:
				file.write("loc%d\r\n" % (2*k+1))
			else:
				file.write("loc%d " % (2*k+1))
		file.write("loc%d\r\n" % 0)
		matrix = generate_random_graph(num_loc)
		for l in range(num_loc):
			for m in range(num_loc):
				if m == num_loc - 1 and l != num_loc - 1:
					if matrix[l,m] == 0:
						file.write("x\n")
					else:
						file.write(str(matrix[l,m]) + "\n")
				elif m == num_loc - 1 and l == num_loc - 1:
					if matrix[l,m] == 0:
						file.write("x")
					else:
						file.write(str(matrix[l,m]))
				else:
					if matrix[l,m] == 0:
						file.write("x ")
					else:
						file.write(str(matrix[l,m]) + " ")
		file.close()
		file1 = open("%d.out" % num_loc, "w")
		for o in range(num_loc):
			if matrix[0,o] > 0:
				break
		file1.write("loc%d " % 0)
		file1.write("loc%d " % o)
		file1.write("loc%d\r\n" % 0)
		file1.write("%d\r\n" % 1)
		file1.write("loc%d " % o)
		for p in range(num_ta):
			if p == num_ta - 1:
				file1.write("loc%d" % (2*p+1))
			else:
				file1.write("loc%d " % (2*p+1))
		file1.close()


if __name__ == "__main__":
	main()