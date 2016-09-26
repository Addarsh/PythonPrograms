#Implementation to check if two vertices are connected or not
#The method must be implemente in O(1) time

import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../Graph/")
from graph import Graph

class connected:
	def __init__(self,g):
		self.numVertices = g.V()
		self.marked = [False for i in range(self.numVertices)]
		self.id = [-1 for i in range(self.numVertices)]
		self.currid = 0
		for i in range(self.numVertices):
			if self.id[i] != -1:continue
			self.dfs(g,i)
			self.currid += 1

	def dfs(self,g,s):
		self.marked[s] = True
		self.id[s] = self.currid
		for v in g.adj(s):
			if not self.marked[v]:
				self.id[v] = self.currid
				self.dfs(g,v)	

	def isConnected(self,v,w):
		return self.id[v] == self.id[w]	

if __name__ == "__main__":
	g = Graph(6)
	g.addEdge(0,1)
	g.addEdge(1,3)
	g.addEdge(2,4)
	g.addEdge(2,5)

	cc = connected(g)
	print cc.isConnected(0,3)
	print cc.isConnected(0,2)
	print cc.isConnected(5,4)
