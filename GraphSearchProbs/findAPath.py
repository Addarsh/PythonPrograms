#Given a 2D mae with entrance and exit points,
#find a graph connecting the entrance to exit, if possible

class findAPath:

	def __init__(self,maze,entrance,exit):
		self.rows = len(maze)
		self.columns = len(maze[0])
		self.mymaze = [row[:] for row in maze]
		self.marked = [[False]*self.columns for i in range(self.rows)]
		self.path = []
		self.marked[entrance[0]][entrance[1]] = True
		self.entrance = entrance
		self.exit = (exit[0],exit[1])
		self.edgeTo = [[(-1,-1)]*self.columns for i in range(self.rows)]	
		self.edgeTo[entrance[0]][entrance[1]] = entrance

		self.pathNotFound = True
		self.dfs(entrance)

	def markIt(self,cell):
		self.marked[cell[0]][cell[1]] = True
	
	def isUnMarked(self,cell):
		return self.marked[cell[0]][cell[1]] == False

	def getneighbors(self,cell):
		r = cell[0]
		c = cell[1]
		neighbours = []
	 	if r-1 >= 0 and c >= 0 and r-1 < self.rows and c < self.columns:
			neighbours.append((r-1,c))
		if r+1 >= 0 and c >= 0 and r+1 < self.rows and c < self.columns:
			neighbours.append((r+1,c))
		if r >= 0 and c-1 >= 0 and r < self.rows and c-1 < self.columns:
			neighbours.append((r,c-1))
		if r >= 0 and c+1 >= 0 and r < self.rows and c+1 < self.columns:
			neighbours.append((r,c+1))
	
		return neighbours

	def isClear(self,cell):
		return self.mymaze[cell[0]][cell[1]] == "C"

	def addFather(self,cell,fathercell):
		self.edgeTo[cell[0]][cell[1]] = fathercell	

	def areCellsEqual(self,one,two):
		return one == two
	
	def dfs(self,source):
		self.markIt(source)
		myneighbors = self.getneighbors(source)
		if myneighbors:
			for neighbor in myneighbors:
				if self.isClear(neighbor) and self.isUnMarked(neighbor) and self.pathNotFound:
					self.addFather(neighbor,source)
					if self.areCellsEqual(neighbor,self.exit): 
						self.pathNotFound = False
						return
					self.dfs(neighbor)

	def getFather(self,cell):
		return self.edgeTo[cell[0]][cell[1]]					

	def getPath(self):
		if self.pathNotFound: return []
		mypath =  []
		currCell = self.exit
		while	not self.areCellsEqual(currCell,self.entrance):
			mypath.append(currCell)
			currCell = self.getFather(currCell)

		mypath.append(self.entrance)
		return mypath

if __name__ == "__main__":
	maze = [["B","B","C"],["B","C","C"],["C","C","B"]]
	entrance = (0,2)
	exit = (2,0)
	fPath = findAPath(maze,entrance,exit)
	finalPath = fPath.getPath()
	if finalPath:
		print "My Path from entrance to exit is:"
		print finalPath
