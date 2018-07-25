def detect_cycle_gen(mat):
	num=len(mat)
	linktree=[]
	for x in range(num):
		tmp=[]
		for y in range(num):
			if mat[x][y]==1:
				tmp.append(y)
		linktree.append([-1,0,tmp])
	numconn=0
	conncomp=[]
	cycle=[]
	while numconn<num:
		findcomp=False
		root=-1
		for x in range(num):
			if linktree[x][1]==0:
				root=x
				break
		prelist=[root]
		curcomp=[root]
		numconn+=1
		linktree[root][1]=1
		findcycle=False
		cyclesub=[]
		while findcomp==False:
			curlist=[]
			for x in prelist:
				for y in linktree[x][2]:
					if (findcycle==False) and (y!=linktree[x][0]) and linktree[y][1]==1:
						findcycle=True
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
								cyclesub.append(leftnode)
								leftnode=linktree[leftnode][0]
						cyclesub.reverse()
						curnode=y
						while curnode!=leftnode:
							cyclesub.append(curnode)
							curnode=linktree[curnode][0]
						cyclesub.append(curnode)
					elif linktree[y][1]==0:
						linktree[y][1]=1
						curlist.append(y)
						numconn+=1
						linktree[y][0]=x
						curcomp.append(y)
			if numconn==num or curlist==[]:
				findcomp=True
			else:
				prelist=curlist
		cycle.append(cyclesub)
		conncomp.append(curcomp)
	for ind in range(len(conncomp)):
		print('The component consisting of the nodes:\n')
		print(",".join(map(str,conncomp[ind])))
		if cycle[ind]==[]:
			print('has no cycle\n')
		else:
			print('has a cycle consisting of the nodes:\n')
			print(",".join(map(str,cycle[ind])))
	return [conncomp,cycle]