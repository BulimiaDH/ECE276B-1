import heapq
import numpy as np 


class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]


def dijkstra_search(edge_list, start, goal):
	frontier = PriorityQueue()
	frontier.put(start, 0)
	came_from = {}
	cost_so_far = {}
	came_from[start] = None
	cost_so_far[start] = 0
	count = 0

	while not frontier.empty():
		current = frontier.get()
		count += 1
		if current == goal:
			break

		for edge in edge_list[current]:
			next, cost = edge[0], edge[1]
			new_cost = cost_so_far[current] + cost
			if next not in cost_so_far or new_cost < cost_so_far[next]:
				cost_so_far[next] = new_cost
				priority = new_cost
				frontier.put(next, priority)
				came_from[next] = current
    
	return came_from, cost_so_far, count

def euclidean_dist(i, j, coords):
	return (coords[i-1,0]-coords[j-1,0])**2 + (coords[i-1,1]-coords[j-1,1])**2

def a_star_search(edge_list, start, goal, e, coords):
	frontier = PriorityQueue()
	frontier.put(start, 0)
	came_from = {}
	cost_so_far = {}
	came_from[start] = None
	cost_so_far[start] = 0
	count = 0
	while not frontier.empty():
		current = frontier.get()
		count += 1
		if current == goal:
			break

		for edge in edge_list[current]:
			next, cost = edge[0], edge[1]
			new_cost = cost_so_far[current] + cost
			if next not in cost_so_far or new_cost < cost_so_far[next]:
				cost_so_far[next] = new_cost
				priority = new_cost + e*euclidean_dist(next, end, coords)
				frontier.put(next, priority)
				came_from[next] = current
    
	return came_from, cost_so_far, count


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

	came_from, cost_so_far, count = a_star_search(edge_list, start, end, 1, coords)
	print(cost_so_far[end], count)
