#Extra Exercise for detecting cycles in a graph containing multiple components
#Input: adj. matrix
def detect_cycle_gen(mat):
	conncomp=[]
	cycle=[]
	#############################
	#Add your codes here
	#You should compute the values of two variables
	#Suppose the graph contains k connected components G1,...,Gk
	#conncomp is a list, where the i-th component is a list containing all the nodes in Gi
	#cycle is a list, where the i-th component is [] if there is no cycle in Gi,
	#	otherwise it should be a list containing the nodes on an arbitrary cycle in Gi
	############################
	for ind in range(len(conncomp)):
		print('The component consisting of the nodes:\n')
		print(",".join(map(str,conncomp[ind])))
		if cycle[ind]==[]:
			print('has no cycle\n')
		else:
			print('has a cycle consisting of the nodes:\n')
			print(",".join(map(str,cycle[ind])))
	return [conncomp,cycle]