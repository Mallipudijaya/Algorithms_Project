import graph as gp
import vertex as vtx
import random
import time

def sparse_graph(no_of_vertices):
	V = []
	adj_l=[]
	for i in range(no_of_vertices):
		adj_l.append(vtx.Vertex(i))

	for i in range(no_of_vertices):
		V.append(i)

	g = gp.Graph(no_of_vertices)
	 
	g.add_vertices(V[0:])

	edge_count = 0
	for i in range(no_of_vertices-1):
		g.add_edge(adj_l[i],adj_l[i+1],i,i+1)
		edge_count = edge_count +1
		
	g.add_edge(adj_l[no_of_vertices-1],adj_l[0],no_of_vertices-1,0)
	edge_count = edge_count +1

	#Sparse graph
	avg_vertex_degree = 6
	no_of_edges = (avg_vertex_degree//2) * no_of_vertices
	start = time.time()

	def non_adjacent_vertices(index):
		p =[]
		if(index != no_of_vertices-1 and index !=0):
			p= V[index+2:]
		if(index == 0):
			p= V[index+2:-1]
		return p

	non_adj_V = []
	#non_adj_V.append([])

	for i in range(no_of_vertices):
		non_adj_V.append( non_adjacent_vertices(i))
	
	combinations=[]
	for i in range(len(non_adj_V)):
		for j in range(len(non_adj_V[i])):
			combinations.append([i,non_adj_V[i][j]])

	ee =  random.sample(combinations, int(no_of_edges-no_of_vertices))
	
	for i in range(len(ee)):
		g.add_edge(adj_l[ee[i][0]],adj_l[ee[i][1]],ee[i][0],ee[i][1])
		edge_count = edge_count +1
	adj_list = g.adjacencyList() 
	adj_mat = g.adjacency_matrix
	

	print ('Sparse graph generated with an edge_count =', edge_count)
	print ('Graph generation took =', time.time()-start)
	res = [adj_list,adj_mat]
	return res

def dense_graph(no_of_vertices):
	V = []
	adj_l=[]

	for i in range(no_of_vertices):
		adj_l.append(vtx.Vertex(i))

	for i in range(no_of_vertices):
		V.append(i)

	g = gp.Graph(no_of_vertices)
	 
	g.add_vertices(V[0:])

	edge_count = 0
	for i in range(no_of_vertices-1):
		g.add_edge(adj_l[i],adj_l[i+1],i,i+1)
		edge_count = edge_count +1
		
	g.add_edge(adj_l[no_of_vertices-1],adj_l[0],no_of_vertices-1,0)
	edge_count = edge_count +1

	#Dense graph
	start = time.time()

	for i in range(no_of_vertices):
		for j in range(i+2, no_of_vertices):
			probab = random.randint(0,100)
			if(i==0 and j== no_of_vertices-1):
				continue
			if(probab <= 20):
				g.add_edge(adj_l[i],adj_l[j],i,j)
				edge_count = edge_count +1
			  
	adj_list = g.adjacencyList() 
	adj_mat = g.adjacency_matrix

	print ('Dense graph generated with an edge_count =', edge_count)
	print ('Graph generation took =', time.time()-start)
	res = [adj_list,adj_mat]
	return res

