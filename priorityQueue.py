class Priority_queue():
	def __init__(self):
		self.pq=[]
	def __str__(self): 
		return ' '.join([str(i) for i in self.pq]) 

	def insert(self, data):
		self.pq.append(data)

	def isEmpty(self):
		return self.pq==[]

	def top(self):
		try:
			maximum=self.pq[0]
			for item in self.pq:
				if maximum<item:
					maximum=item
			return maximum
		except:
			print("Priority Queue is empty")
			return -1

	def pop(self):
		if self.pq==[]:
			print("Priority Queue is empty")
		else:
			item=self.top()
			self.pq.remove(item)

if __name__ == '__main__': 
	pqueue = Priority_queue() 
	n=(int)(input())
	for i in range(n):
		pqueue.insert((int)(input()))				 
	print(pqueue.top())
	pqueue.pop()
	print(pqueue.top())


