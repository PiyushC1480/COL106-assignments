"""creating a graph class which has all the main funcitons"""
class Graph:
	def __init__(self, vertices,ed_list):
		self.V = vertices # No. of vertices goven 
		self.graph = ed_list # the edge list given 
		self.adj_dic= {} # adjacenccy list maintained for the maximum spanning tree
		self.cause = [] # this contains the parent of a vertex in the tree. for example parent if ith vertex will be stroed at cause[i]
		self.path = [] # final path 
		self.max_pac=None # maximum packet t be tranferred

	# A function to find set of  element i
	def set_of_i(self, parent, i):
		if parent[i] != i:
		# Reassign node's parent to root node as
			parent[i] = self.set_of_i(parent, parent[i])
		return parent[i]

	# function to do the union of two sets by their rank
	def union(self, parent, rank, x, y):
		if rank[x] < rank[y]:
			parent[x] = y
		elif rank[x] > rank[y]:
			parent[y] = x
		# If ranks are same, then make one as root
		# and increment its rank by one
		else:
			parent[y] = x
			rank[x] += 1

	# insert an edge in the adjacency list.
	def insert_edge(self,u,v,x):#O(1) operation using dictionary
		try :
			self.adj_dic[u].append((v,x))
			
		except KeyError:# u doesn't exist in list
			self.adj_dic[u] = []
			self.adj_dic[u].append((v,x))
			
		try:
			self.adj_dic[v].append((u,x))
			
		except KeyError:# v doesn't exist in list
			self.adj_dic[v]=[]
			self.adj_dic[v].append((u,x))
			

	# function to set_of_i maximum splanning tree using kruskal algorithm
	def max_span_tree(self):
		i = 0
		e = 0
		# sorting the edges in descending order of their weight 
		self.graph = sorted(self.graph,key=lambda item: item[2],reverse=True)# O(mlogm)
		parent = [] 
		rank = []
		# init of parent and rank lists 
		for node in range(self.V):#O(n)
			parent.append(node)
			rank.append(0)
		# Number of edges to be taken is equal to V-1
		while e < self.V -1: #iterate over the sorted list 
			u, v, w = self.graph[i]
			i += 1
			x = self.set_of_i(parent, u)# find parent of u
			y = self.set_of_i(parent, v)# find parent of v
			if x != y:# to check whetehr they form a cycle in graph or not 
				e += 1
				self.insert_edge(u,v,w)
				self.union(parent, rank, x, y)
	# time complex : O(mlogm +n) ==> O(mlogm)
	# recursive function for dfs on the maximum spanning tree 
	def DFSUtil(self, v, visited):
		visited[v] = True# make the vertex to be visited 
		for i in self.adj_dic[v]:# visit its neighbour 
			if visited[i[0]]==False:
				self.cause[i[0]] = v# mark v to be parent 
				self.prev_ed_packet[i[0]] = i[1]# packet teans width 
				self.DFSUtil(i[0],visited)# recurse 
	# function to do DFS traversal
	def DFS(self,start):
		V = len(self.adj_dic) #total vertices
		# init of visited , parent and prev packet list 
		visited =[False]*(V)
		self.cause = [None]*V
		self.prev_ed_packet = [None]*V# this store the MAX value of packet which the node i and parent of i can have 
		# start dfs 
		if visited[start] == False:
			self.DFSUtil(start,visited)
	#time O(m+n)
	def path_find(self,start,stop):# recurse back from the stop vertex to the start vertex and check for the maximum packet and maintain the path length
		self.path.append(stop)
		h = self.prev_ed_packet[stop]
		if self.max_pac==None:
				self.max_pac = h
		elif self.max_pac>h:
				self.max_pac = h
		if self.cause[stop] == start:
			self.path.append(start)
		else:
			self.path_find(start,self.cause[stop])
	#time O(m)
	
"""main function. this will call the graph, make the max spanning tree, call dfs on it, set_of_i the path from stop to start, then reverse it """
def findMaxCapacity(n1,l1,star,sto):
	gr = Graph(n1,l1)
	gr.max_span_tree()
	gr.DFS(star)
	gr.path_find(star,sto)
	gr.path.reverse()# O(len of path ) ==> O(m) 
	return(gr.max_pac,gr.path)
# total complex O(mlogm+m+n)==> O(mlogm) 