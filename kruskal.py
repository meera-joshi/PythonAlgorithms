def root(a, id):
	while(id[a]!=a):
		id[a]=id[id[a]]   # by accessing id[id[a]], we move to grandparent of the node reduce the time to half
		a=id[a]
	return a

def sort3(val):
	return val[2]

def kruskal(edges, vertices):
	id=list(range(vertices+1))
	size=[1]*(vertices+1)
	mst=[]
	minweight=0
	edges.sort(key=sort3)
	for edge in edges:
		p=root(edge[0],id)
		q=root(edge[1],id)
		if p==q:
			continue
		mst.append(edge)
		minweight+=edge[2]
		if size[edge[0]]>size[edge[1]]:
			swap(p,q)
		id[q]=id[p]
		size[p]+=size[q]

	return (mst,minweight)

n = int(input()) 
lst=[]
for i in range(0, n): 
    ele =  list(map(int,input().strip().split()))[:n] 
    lst.append(ele) 
(mst,mw)=kruskal(lst,3)
print(mst)
print(mw)






