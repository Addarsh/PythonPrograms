#Implementation of the basic graph API
#Here each vertex is represented by an integer
#which connects another set of vertices
#This is the adjacecy list representation of graphs

class Graph:
	
	def __init__(self,vertices):
		self.numvertices = vertices
		self.bagArray = [[] for i in range(self.numvertices)]
		self.numEdges = 0

	def addEdge(self,v,w):
		self.bagArray[v].append(w)
		self.bagArray[w].append(v)
		self.numEdges += 1

	def V(self):
		return self.numvertices

	def E(self):
		return self.numEdges

	def adj(self,v):
		return self.bagArray[v]
	

if __name__ == "__main__":
	g = Graph(5)
	g.addEdge(0,1)
	g.addEdge(3,2)
	g.addEdge(1,4)

	print g.adj(1)
