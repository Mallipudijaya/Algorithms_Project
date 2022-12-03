import vertex as vtx
import graph as gp
import kruskal_heap as nh
def print_path(d,mat,s,t):
	path = []
	i = t
	max_bw = 100000000000000000
	path.append(i)
	while (i!=s ):
		u=int(i)
		path.append(int(d[i]))
		i = int(d[i])
		v=i
		if(mat[u][v]<max_bw):
			max_bw=mat[u][v]
	ret = ''
	for i in range(len(path)):
		ret = ret + str(path[len(path)-i-1]) + ' -> '
	val =[ret,max_bw]
	return val

def dij(g,s,t):
	adj_list  = g[0]
	edge_wts = g[1]
	
	no_of_vertices = len(adj_list)
	bw=[0]*no_of_vertices
	dad =[0]*no_of_vertices
	status = []

	for i in range(no_of_vertices):
		status.append(-1) # -1 for unseen
	status[s] = 1 # 1 for in-tree

	bw[s] = 100000000000000000 # +inf

	for i in range(len(adj_list[s])):
		w =  adj_list[s][i]

		status[w] = 0 #fringe

		bw[w] = edge_wts[s][w]
		dad[w]=s
	
	while (status[t] != 1): #while t is not in-tree
		# pick a fringe of the max bw
		m = -1
		max_bw_index = -1
		for i in range(len(status)):
			if(status[i] == 0): 
				if(bw[i]>m):
					m = bw[i]
					max_bw_index = i


		v = max_bw_index
		status[v] = 1
		for i in range(len(adj_list[v])):
			w =  adj_list[v][i]
			if(status[w] == -1):#if unseen
				status[w] = 0 #make fringe
				bw[w] = min(bw[v], edge_wts[v][w])
				dad[w] = v
			else:
				if(status[w] == 0 and bw[w]< min(bw[v], edge_wts[v][w])):# if fringe
					bw[w] = min(bw[v], edge_wts[v][w])
					dad[w] = v
	
	max_bw_path = print_path(dad,edge_wts,s,t)
	print ('Using Dijkstras algo without heap')
	print ('max bw path in g from', s, 'to', t, 'is', ':', max_bw_path[0] )
	print ('max bw = ', max_bw_path[1])
	return dad

import heap as hp

def dij_heap(g,s,t):
	adj_list  = g[0]
	edge_wts = g[1]
	
	no_of_vertices = len(adj_list)
	dad = [0]*no_of_vertices
	status = []
	bw = [0]*no_of_vertices

	#max heap for maintaining fringes
	fringeHeap = hp.maxHeap()


	for i in range(no_of_vertices):
		status.append(-1) # -1 for unseen
	status[s] = 1 # 1 for in-tree

	
	bw[s] = 100000000000000000 # +inf
	fringeHeap.Insert(s, bw[s])


	# updating source node's neighbors
	fringeHeap.Delete(1)

	for i in range(len(adj_list[s])):
		w =  adj_list[s][i]
		status[w] = 0 #fringe
		bw[w] = edge_wts[s][w]
		fringeHeap.Insert(w, bw[w])
		dad[w]=s
	
	while (status[t] != 1): #while t is not in-tree
		flag = 1
		v = fringeHeap.Maximum();
		fringeHeap.Delete(1)
		status[v] = 1

		for i in range(len(adj_list[v])):
			w =  adj_list[v][i]
			# w = w-1
			if(status[w] == -1):#if unseen
				status[w] = 0 #make fringe
				bw[w] = min(bw[v], edge_wts[v][w])
				fringeHeap.Insert(w, bw[w])
				dad[w] = v
			else:
				if(status[w] == 0 and bw[w]< min(bw[v], edge_wts[v][w])):#if fringe
					bw[w] = min(bw[v], edge_wts[v][w])
					fringeHeap.Insert(w, bw[w])#update it not insert
					dad[w] = v
	
	max_bw_path = print_path(dad,edge_wts,s,t)
	print ('Using Dijkstras algo using heap')
	print ('max bw path in g from', s, 'to', t, 'is', ':', max_bw_path[0] )
	print ('max bw = ', max_bw_path[1])

def kruskal(g,s,t,heap_arr):
	
	adjlist  = g[0]
	mat = g[1]
	
	no_of_vertices = len(adjlist)
	

	arr=nh.heapsort(heap_arr)
	
	
	vertices=[]
	V_list=[]
	p=[]
	rank = []
	dad = [0]*no_of_vertices
	
	for i in range(no_of_vertices):
		vertices.append(vtx.Vertex(i))
		V_list.append(i)
		p.append(-1)
		rank.append(0)
	
	#Makeset
	MST=gp.Graph(no_of_vertices)
	MST.add_vertices(V_list[0:])

	
	def Find(v):
		w=v
		s=[]
		while(p[w]!=-1):
			w=p[w];
			s.append(w)
		while(len(s)!=0):
			x=s.pop()
			dad[x]=w

		return w
	def Union(r1,r2):

		if(rank[r1] < rank[r2]):
			p[r1]=r2
		elif(rank[r1] > rank[r2]):
			p[r2]=r1
		else:
			p[r1]=r2
			rank[r2]+=1

	
	count=0
	for index in range(0,len(arr)-1,1):
		u=arr[index].u
		v=arr[index].v

		root_u=Find(u)
		root_v=Find(v)
		if(count==no_of_vertices-1):
			break;
		if( root_u != root_v ):
		
			MST.add_edge_mst(vertices[u],vertices[v])
			count=+1
			Union(root_u,root_v)
	

	
	mst_adj_list = (MST.adjacencyList_mst())
    
	curr = s
	queue = []
	status = [0]*no_of_vertices#un-visited

	status[s] = 1#in-tree
	queue.append(s)

	path =[]
	dad = [0]*no_of_vertices
	
	
	while(curr != t and len(queue)>0):
		
		curr = queue.pop(0)
		path.append(curr)
		for i in range(len(mst_adj_list[curr]) ):
			nxt  = mst_adj_list[curr][i]
			
			if(status[nxt] == 0):
				queue.append(nxt)
				status[nxt] = 1
				dad[nxt] = curr

	max_bw_path = print_path(dad,mat,s,t)
	
	print ('Using Kruskals algo')
	print ('max bw path in g from', s, 'to', t, 'is', ':', max_bw_path[0] )
	print ('max bw = ', max_bw_path[1])
