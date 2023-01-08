# https://www.youtube.com/watch?v=0sQE8zKhad0&list=PLkZYeFmDuaN2-KUIv-mvbjfKszIGJ4FaY&index=9&


# GRAPH USING OBJECTS

graph= {
    1:[2,3],
    2:[1,3,4],
    3:[1,2,4,5],
    4:[3,2,5],
    5:[3,4]
}

def printGraph(graph):
    for vtx in graph.keys():
        print(f"el vértice {vtx} está conectado a : {graph[vtx]}")

def getGraphEdges(graph):
    edges = []
    for vtx in graph.keys():
        for cvtx in graph[vtx]:
            edges.append((vtx,cvtx))
    return edges
def updateGraph(newEdge,values):
    graph[newEdge] = values
    for vl in values:
        graph[vl].append(newEdge)

printGraph(graph)
print(getGraphEdges(graph))
updateGraph(6,[3,5,1])
print(getGraphEdges(graph))


# GRAPH USING CLASSES

class Node():
    def __init__(self,id,conn):
        self.conn = conn
        self.id = id


class Graph():
    def __init__(self):
        self.nodes = []

    def printGraph(self):
        links = []
        for node in self.nodes:
            for cn in node.conn:
                links.append((node.id,cn))
        return links

    def find(self,id):
        for vtx in self.nodes:
            if vtx.id == id:
                return vtx
            else:
                continue

    def addNode(self,node_id,node_connections):
        new_node = Node(node_id,node_connections)
        self.nodes.append(new_node)
        for cn in node_connections:
            self.find(cn).conn.append(node_id)


myGraph = Graph()
myGraph.addNode(1,[])
myGraph.addNode(2,[1])
myGraph.addNode(3,[1,2])
print(myGraph.printGraph())