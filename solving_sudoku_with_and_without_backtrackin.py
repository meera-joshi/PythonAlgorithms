def read_matrix(filename):
	with open(filename, "r") as f:
		matrix = f.readlines()
		for i,row in enumerate(matrix):
			matrix[i] = list(map(int,matrix[i].split(",")))
	return matrix

def write_matrix(filename, solved_matrix):
	with open(filename, "w") as f:
		f.writelines(','.join(str(j) for j in i) + '\n' for i in solved_matrix)
	print(filename+" for backtracking generated.")

class sudoku():
	def __init__(self, filename):
		self.matrix = read_matrix(filename)
	
	def usedinRow(self,matrix, row, num):
	    for col in range(9):
		if self.matrix[row][col]==num:
		    return True
	    return False
	    
	def usedinCol(self,matrix,col, num):
	    for row in range(9):
		if self.matrix[row][col]==num:
		    return True
	    return False
	    
	def usedinBox(self,matrix,row,col,num):
	    rowStart=row-row%3
	    colStart=col-col%3
	    for i in range(rowStart,rowStart+3):
		for j in range(colStart,colStart+3):
		    if matrix[i][j]==num:zzz
		        return True
	    return False
	 
	def isValid(self,matrix, row,col,num):
	    if not self.usedinRow(matrix,row,num) and not self.usedinCol(matrix,col,num) and not self.usedinBox(matrix,row,col,num):
		return True
	    return False
	     
	def findEmptyCell(self,matrix):
	    for col in range(9):
		for row in range(9):
		    if matrix[row][col] == 0:
		        return row,col
	    return -1,-1
	 
	def fillSudoku(self,matrix):
	    row,col=self.findEmptyCell(matrix)
	    if row==-1:
		return True
	    for n in range(1,10):
		if self.isValid(matrix, row,col,n):
		    matrix[row][col]=n
		    if fillSudoku(matrix):
		        return True
		    matrix[row][col]=0
	    return False
	 

	def solve(self):
		self.fillSudoku(matrix)

	
	def completed(self,matrix):
	    if all(matrix[i][j]!=0 for i in range(9) for j in range(9)):
		return True
	    return False
	 
	def makeList(self,helperList):
	    for row in range(9):
		for col in range(9):
		    if matrix[row][col]==0:
		        valid={} #Dict telling which values are possible for this cell { matrix[row][col]
		        values=[]#list having possible values for this cell
		        for n in range(10):
		            valid[n]=True
		        for i in range(9):
		            valid[matrix[row][i]]=False
		            valid[matrix[i][col]]=False
		        
		        size=0    
		        for value in range (1,10):
		            if valid[value]==True:
		                values.append(value)
		        size=len(values)
		        cell=[]
		        cell.append(size)
		        cell.append(row)
		        cell.append(col)
		        cell.append(values)
		        helperList.append(cell)
	    helperList.sort()
		        
		        
	def fillSudoku2(self,matrix):
	    if self.completed(matrix):
		return True
	    helperList = []#list having element lists having number of available values,row,col,list of available values    
	    
	    self.makeList(helperList)
	    
	    for num in range(helperList[0][0]):
		matrix[helperList[0][1]][helperList[0][2]]=helperList[0][3][num]
		if self.fillSudoku2(matrix):
		    return True
		matrix[helperList[1][2]]=0
		return False
		

	def solve_without_backtracking(self):
		
		fillSudoku2(matrix)

if __name__=="__main__":
	su = sudoku("data.txt")
	su.solve()
	write_matrix("sol.txt", su.matrix)
	try:
		su = sudoku("data.txt")
		su.solve_without_backtracking()
		print("Solved sudoku matrix without backtracking:")
		for i in range(9):
			print(*su.matrix[i], sep=" ")
	except Exception as e:
		print(e)


