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

def print_degrees(mat):
	num=len(mat)
	for x in range(num):
		degree=0
		for y in range(num):
			if mat[x][y]==1:
				degree+=1
		print('Degree of Node ',x,': ',degree,'\n')

def shortest_path(mat,node1,node2):
	num=len(mat)
	nodeind=[0]*num
	nodeind[node1]=1
	prelist=[node1]
	findpath=0
	stpath=[]
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
			stpath.append(curnode)
			while count>1:
				for x in range(num):
					if nodeind[x]==(count-1) and mat[x][curnode]==1:
						print('(',x,',',curnode,'),')
						curnode=x
						stpath.append(curnode)
						break
				count=count-1
			return stpath
		elif newnodecon==0:
			print('No such path')
			findpath=-1
			return stpath
		else:
			prelist=curlist

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
	cycle=[]
	while findcycle==0:
		curlist=[]
		for x in prelist:
			for y in linktree[x][2]:
				if (y!=linktree[x][0]) and linktree[y][1]==1:
					findcycle=1
					print('Find a cycle consisting of the following edges:\n')
					rightbranch=[]
					rightnode=y
					while rightnode!=-1:
						rightbranch.append(rightnode)
						rightnode=linktree[rightnode][0]
					leftnode=x
					while leftnode!=-1:
						if leftnode in rightbranch:
							break
						else:
							cycle.append(leftnode)
							print('(',linktree[leftnode][0],',',leftnode,')\n')
							leftnode=linktree[leftnode][0]
					cycle.reverse()
					print('(',x,',',y,')\n')
					curnode=y
					while curnode!=leftnode:
						cycle.append(curnode)
						print('(',curnode,',',linktree[curnode][0],')\n')
						curnode=linktree[curnode][0]
					cycle.append(curnode)
					return cycle
				elif linktree[y][1]==0:
					linktree[y][1]=1
					curlist.append(y)
					linktree[y][0]=x
		if curlist==[]:
			findcycle=-1
			print('No cycle in the graph')
			return cycle
		else:
			prelist=curlist