#!/usr/bin/python3.6

# Graph Theory easy exercises for Social Networks module
# LACC 2018

#*************************************
# This is where you write your code
#
# matrix_load()
#
# Loads an adjacency matrix for a graph from a file
#
# input: none
# output: matrix containing each node 
# 
# Note: You can open a file using open(filename)
# 
# You can get a list containing each line with file.readlines()
#
#*************************************
def matrix_load(filename):
	file=open(filename)
	a=file.readlines()
	num=len(a)
	mat=[]
	for x in range(num):
		tmp=[]
		for y in range (num):
			if a[x][y]=='1':
				tmp.append(1)
			else:
				tmp.append(0)
		mat.append(tmp)
	file.close()
	return mat
#*************************************
# This is where you write your code
#
# print_degrees(mat)
#
# Prints the degrees of all nodes in a graph given an adj. matrix 
#
# input: the adjacency matrix of the graph
# output: none
# 
# Note: You don't need to return anything. 
#
# Effectively, you'll need to count the number of 1s in each row 
# (or each column) and print this. Use a nested loop (for or while)
#*************************************

def print_degrees(mat):
	num=len(mat)
	for x in range(num):
		degree=0
		for y in range(num):
			if mat[x][y]==1:
				degree+=1
		print('Degree of Node ',x,': ',degree,'\n')
#*************************************
# This is where you write your code
#
# shortest_path(mat,node1,node2)
#
# Find the shortest path from node1 to node2 of all nodes in a graph given an adj. matrix 
#
# input: the adjacency matrix of the graph,node1,node2
# output: 'The path is: ' appended with all edges on the path if there is one, otherwise print out 'No such path'
# 
# Note: You don't need to return anything. 
#
#*************************************

def shortest_path(mat,node1,node2):
	num=len(mat)
	nodeind=[0]*num
	nodeind[node1]=1
	prelist=[node1]
	findpath=0
	while findpath==0:
		newnodecon=0
		curlist=[]
		for x in prelist:
			for y in range(num):
				if nodeind[y]==0 and mat[x][y]==1:
					newnodecon+=1
					curlist.append(y)
					nodeind[y]=nodeind[x]+1
		if node2 in curlist:
			findpath=1
			print('The path is: ')
			count=nodeind[node2]
			curnode=node2
			while count>1:
				for x in range(num):
					if nodeind[x]==(count-1) and mat[x][curnode]==1:
						print('(',x,',',curnode,'),')
						curnode=x
						break
				count=count-1
		elif newnodecon==0:
			print('No such path')
			findpath=-1
		else:
			prelist=curlist

#*************************************
# This is where you write your code
#
# detect_cycle(mat)
#
# Detect the in a graph given an adj. matrix 
#
# input: the adjacency matrix of the graph
# output: 'Find a cycle, the first edge is: ' appended with an arbitrary edge on the cycle if there is one, otherwise print out 'No cycle in the graph'
# 
# Note: You don't need to return anything. 
#
#*************************************

def detect_cycle(mat):
	num=len(mat)
	linktree=[]
	for x in range(num):
		tmp=[]
		for y in range(num):
			if mat[x][y]==1:
				tmp.append(y)
		linktree.append([-1,0,tmp])#parent,flag,neighbor
	prelist=[0]
	linktree[0][1]=1
	findcycle=0;

	while findcycle==0:
		curlist=[]
		for x in prelist:
			for y in linktree[x][2]:
				if (y!=linktree[x][0]) and linktree[y][1]==1:
					findcycle=1
					print('Find a cycle, the first edge is: (',x,',',y,')')
					return findcycle
				elif linktree[y][1]==0:
					linktree[y][1]=1
					curlist.append(y)
					linktree[y][0]=x
					#print(y,'\n')
		if curlist==[]:
			findcycle=-1
			print('No cycle in the graph')
			return findcycle
		else:
			prelist=curlist


