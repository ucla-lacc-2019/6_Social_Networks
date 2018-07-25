def is_connect(mat):
	num=len(mat)
	linktree=[]
	for x in range(num):
		tmp=[]
		for y in range(num):
			if mat[x][y]==1:
				tmp.append(y)
		linktree.append([0,tmp])
	prelist=[0]
	linktree[0][0]=1
	findcomp=False;
	numconn=1;
	while findcomp==False:
		curlist=[]
		for x in prelist:
			for y in linktree[x][1]:
				if linktree[y][0]==0:
					linktree[y][0]=1
					curlist.append(y)
					numconn+=1
		if numconn==num:
			print('The graph is connected')
			findcomp=True
		elif curlist==[]:
			print('The graph is not connected')
			findcomp=True
		else:
			prelist=curlist


def find_component(mat):
	num=len(mat)
	linktree=[]
	for x in range(num):
		tmp=[]
		for y in range(num):
			if mat[x][y]==1:
				tmp.append(y)
		linktree.append([0,tmp])
	numconn=0
	conncomp=[]
	while numconn<num:
		findcomp=False
		root=-1
		for x in range(num):
			if linktree[x][0]==0:
				root=x
				break
		prelist=[root]
		curcomp=[root]
		numconn+=1
		linktree[root][0]=1
		while findcomp==False:
			curlist=[]
			for x in prelist:
				for y in linktree[x][1]:
					if linktree[y][0]==0:
						linktree[y][0]=1
						curlist.append(y)
						numconn+=1
						curcomp.append(y)
			if numconn==num or curlist==[]:
				findcomp=True
			else:
				prelist=curlist
		conncomp.append(curcomp)

	for cmp in conncomp:
		print(",".join(map(str,cmp)))
	return conncomp
