import numpy as np 
from matplotlib import pyplot as plt 


def cost(x):
	return np.linalg.norm(x)**2

U1 = np.array([[0.5, -1],
			   [1, 0.5]])
U2 = np.array([[1, 0.5],
			   [0.5, 0.5]])

J4 = np.zeros((21,21)) 
i = 0
for x1 in np.arange(-1, 1.1, 0.1):
	j = 0
	for x2 in np.arange(-1, 1.1, 0.1):
		J4[i,j] = x1**2+x2**2
		j += 1
	i += 1

J3 = np.zeros((21,21))
policy3 = np.zeros((21,21),dtype=np.uint8)
cost_to_go3 = np.zeros((21,21,2))
i = 0
for x1 in np.arange(-1, 1.1, 0.1):
	j = 0
	for x2 in np.arange(-1, 1.1, 0.1):
		x = np.array([[x1],[x2]])
		cost_to_go3[i,j,0] = cost(x)+cost(np.dot(U1,x))
		cost_to_go3[i,j,1] = cost(x)+cost(np.dot(U2,x))
		J3[i,j] = np.amin(cost_to_go3[i,j,:])
		policy3[i,j] = np.argmin(cost_to_go3[i,j,:])
		j += 1
	i += 1
print(J3)
print(policy3)


J2 = np.zeros((21,21))
policy2 = np.zeros((21,21),dtype=np.uint8)
cost_to_go2 = np.zeros((21,21,2))
i = 0
for x1 in np.arange(-1, 1.1, 0.1):
	j = 0
	for x2 in np.arange(-1, 1.1, 0.1):
		x = np.array([[x1],[x2]])

		next_x = np.dot(U1,x)
		cost_to_go2[i,j,0] = cost(x)+cost(next_x)+np.minimum(cost(np.dot(U1,next_x)), cost(np.dot(U2,next_x)))

		next_x = np.dot(U2,x)
		cost_to_go2[i,j,1] = cost(x)+cost(next_x)+np.minimum(cost(np.dot(U1,next_x)), cost(np.dot(U2,next_x)))
		
		J2[i,j] = np.amin(cost_to_go2[i,j,:])
		policy2[i,j] = np.argmin(cost_to_go2[i,j,:])
		j += 1
	i += 1
print(J2)
print(policy2)
plt.imshow(policy2)
plt.show()
plt.imshow(policy3)
plt.show()

