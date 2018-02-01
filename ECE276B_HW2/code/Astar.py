import numpy as np 
import heapq


# Use heapq/priority queue as open list
class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]


def dijkstra(edges_list, start, end, total_nodes):
	# Dijkstra's algorithm to find shortest path between two nodes in a graph
	OPEN = PriorityQueue()
	OPEN.put(start,0) # put start node in priority queue
	distToStart = np.full((total_nodes,1),np.inf)
	distToStart[start-1] = 0 # initialize distance of all nodes to start as inf
	parent = np.arange(1, total_nodes+1) # initialize parent of each node as itself
	count = 0

	while not OPEN.empty():
		i = OPEN.get()
		count += 1
		for edge in edge_list[i]:
			j, cost = edge[0], edge[1]
			if distToStart[i-1]+cost < distToStart[j-1] and distToStart[i-1]+cost < distToStart[end-1]:
				distToStart[j-1] = distToStart[i-1]+cost
				parent[j-1] = i
				if j != end:
					OPEN.put(j, distToStart[j-1])
	return distToStart, parent, count

def euclidean_dist(i, j, coords):
	return (coords[i-1,0]-coords[j-1,0])**2 + (coords[i-1,1]-coords[j-1,1])**2


def astar(edge_list, start, end, total_nodes, coords):
	# Astar algorithm to find shortest path between two nodes in a graph
	CLOSED = []
	OPEN = PriorityQueue()
	OPEN.put(start,0) # put start node in priority queue
	distToStart = np.full((total_nodes,1),np.inf)
	distToStart[start-1] = 0 # initialize distance of all nodes to start as inf
	parent = np.arange(1, total_nodes+1) # initialize parent of each node as itself
	count = 0

	while not OPEN.empty():
		i = OPEN.get()
		CLOSED.append(i)
		count += 1
		for edge in edge_list[i]:
			j, cost = edge[0], edge[1]
			if not (j in CLOSED):
				if distToStart[i-1]+cost < distToStart[j-1]:
					distToStart[j-1] = distToStart[i-1]+cost
					parent[j-1] = i
					OPEN.put(j, distToStart[j-1]+euclidean_dist(j,end, coords))
	return distToStart, parent, count



if __name__ == '__main__':
	input_folder = '/Users/tianyu/Documents/UCSD/Winter 2018/ECE276B/HW/ECE276B_HW2/Problem4/input/input_1.txt'
	coords_folder = '/Users/tianyu/Documents/UCSD/Winter 2018/ECE276B/HW/ECE276B_HW2/Problem4/input/coords_1.txt'
	with open(input_folder, 'r') as f:
		total_nodes = np.int(f.readline())
		start = np.int(f.readline())
		end = np.int(f.readline())

	edges  = np.genfromtxt(input_folder,skip_header=3)
	coords = np.loadtxt(coords_folder)

	edge_list = {}
	for edge in edges:
		i, j, cost = np.int(edge[0]), np.int(edge[1]), edge[2]
		if i in edge_list:
			edge_list[i].append([j, cost])
		else:
			edge_list[i] = [[j, cost]]

	distance, parent, count = astar(edge_list, start, end, total_nodes, coords)
	print(distance[end-1,0], count)

