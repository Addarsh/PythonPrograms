#Implement isCyclic for a graph
#this has to be a O(V+E) implementation
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../Graphs/Graph/")
from graph import Graph

class Cyclic:

	def __init__(self,g):
		self.g = g
		self.edgeTo = [-1]*self.g.V()	
		self.marked = [False]*self.g.V()

		self.edgeTo[0]  = 0
		self.cycle = False
		self.dfs(0)

	def dfs(self,s):
		self.marked[s]	= True
		for v in self.g.adj(s):
			if self.cycle: return
			if not self.marked[v]:
				self.edgeTo[v] = s
				self.dfs(v)
			elif self.edgeTo[s] != v:
				self.cycle = True
				return

	def isCyclic(self):
		return self.cycle

if __name__ == "__main__":
	g = Graph(4)
	g.addEdge(0,1)
	g.addEdge(1,2)
	g.addEdge(2,0)
	g.addEdge(2,3)
	
	cycle = Cyclic(g)
	print cycle.isCyclic()	
	
