import algorithm as algos
import time
import graph_generation as graph
import random
import graph as gp
choice = int(input('\n Input 1 to test on a random sparse graph or \n Input 2 to test on a random dense graph : '))


if(choice == 1):
	no_of_vertices = int(input('Enter no_of_vertices for random graph generation: '))
	g = graph.sparse_graph(no_of_vertices)

if(choice == 2):
	no_of_vertices = int(input('Enter no_of_vertices for random graph generation: '))
	g = graph.dense_graph(no_of_vertices)

if(choice == 1 or choice ==2):
	time1 = 0
	time2 = 0
	time3 = 0
	temp = ''
	print ('Random graph testing starts')
	for i in range(5):
		
		s1 = random.randint(0,no_of_vertices-1)
		t1 = s1
		while (t1 == s1):
			t1 = random.randint(0,no_of_vertices-1)
	
		start = time.time()
		algos.dij(g,s1,t1)
		time1 = time1 +  time.time()-start
		temp = temp + str(time.time()-start) + ' '	

		start = time.time()
		algos.dij_heap(g,s1,t1)
		time2 = time2 +  time.time()-start
		temp = temp + str(time.time()-start) + ' '
		
		adjlist=g[0]
		mat=g[1]
		heap_arr=[]
		arr=[]
		for i in range(len(adjlist)):
			for j in range(len(adjlist[i])):
				
				u = i
				v = adjlist[i][j] 
				wt = mat[i][adjlist[i][j]]
				if(u<v):
					heap_arr.append(gp.edge(u,v,wt))
		start = time.time()
		algos.kruskal(g,s1,t1,heap_arr)
		time3 = time3 +  time.time()-start
		temp = temp + str(time.time()-start) +'\n'
		
	print ('The algorithm running times are:')
	print (temp) 
	print('average running times of algorithms')
	print('Dijkstras:',time1/5)
	print('Dijkstras with heap:',time2/5)
	print('Kruskals:',time3/5,'\n')