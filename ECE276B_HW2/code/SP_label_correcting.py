import numpy as np 

start = 1
end = 5
parent = np.arange(1,6) # intialize parent of i as i
edges = [[1,2,2], [1,3,1], [2,3,1], [3,2,1], [2,4,1], [3,4,3], [2,5,0], [4,5,0]] # i to j with cost(ij)
d = np.full((5, 1), np.inf)
d[start-1,0] = 0
OPEN = [start] # last in first out, start node = 1
while len(OPEN) is not 0:
	i = OPEN.pop()
	for edge in edges:
		if edge[0] == i:
			j = edge[1] # j is child of i
			if d[i-1] + edge[2] < d[j-1] and d[i-1] + edge[2] < d[end-1]:
				d[j-1] = d[i-1] + edge[2]
				parent[j-1] = i
				if j is not end:
					OPEN.append(j)

print(parent)
print(d)

