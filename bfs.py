class Vertex:
    #CONSTRUCTOR -  INITIALIZES VALUES FOR NAME OF THE VERTEX, DISTANCE AND COLOR FOR
    def __init__(self, name):
        self.name = name #NAME OF THE VERTEX
        self.neighbours = [] #LIST OF NEIGHBOURS
        self.dist = 9999 #INITIALIZED DISTANCE TO A HIGH NUMBER
        self.color = 'black'  #NOT VISITED VERTEX
        return

    #ADD NEIGHBOURS TO VERTEX IF NOT YET ADDED
    def add_neighbour(self, vertex):
        if vertex not in self.neighbours:
            self.neighbours.append(vertex)
            self.neighbours.sort()
        return

class Graph:
    #SET OF VERTICES ADDDED TO THE GRAPH
    vertices = {}
    #ADD A VERTEX TO GRAPH
    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices: #CHECK IF IT IS AN OBJCT OF VERTEX CLASS OR NOT AND ALSO IF IT IS PRESENT IN VERTICES OR NOT
            self.vertices[vertex.name] = vertex #IF NOT PRESENT APPEND TO VERTICES ELSE RETURN
            return vertex.name
        else:
            return False
    #ADD AN EDGE TO VERTICES
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices: #CHECK IF IT IS VERTICES
            for key, value in self.vertices.items():
                if key == vertex1: #ADD NEIGHBOUR TO VERTEX TO CREATE AN EDGE
                    value.add_neighbour(vertex2)
                if key == vertex2:
                    value.add_neighbour(vertex1)
            return True
        else:
            return False
    #DISPLAY THE GRAPH VERTEX, ITS NEIGHBOURS AND THE ORDER
    def display_graph(self):
        print("VERTEX[NEIGHBOURS]LEVEL")
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbours) + " " + str(self.vertices[key].dist))
        return
    #BFS
    def breadth_first_search(self, start_vertex):
        q = [] #CREATE A QUEUE, HERE CHOOSING AN EMPTY LIST
        start_vertex.dist = 0 #INITIALIZING START VERTEX DISTANCE TO ITSELF AS 0
        start_vertex.color = 'red' #SET COLOR OF TRAVERESED VERTEX TO RED
        order = [start_vertex.name]
        #CHECK FOR NEIGHBOURS OF STARTING VERTEX AND APPEND IT TO QUEUE (ENQUEUE)
        for v in start_vertex.neighbours:
            self.vertices[v].dist = start_vertex.dist + 1
            q.append(v)
            order.append(v)
        #UNTIL QUEUE IS EMPTY, LOOK FOR FIRST ELEMENT IN Q, TRAVERSE IT AND LOOK FOR ITS NEIGHBOURS
        while len(q)>0:
            print('QUEUE NOW IS {0}'.format(q))
            vertex1 = q.pop(0)
            print('REMOVING FROM Q VERTEX:{0}'.format(vertex1))
            node_vertex1 = self.vertices[vertex1]
            node_vertex1.color = 'red' #SET COLOR OF TRAVERSED VERTEX TO RED
            #LOOK FOR NEIGHBOURS OF TRAVERSED VERTEX
            for v in node_vertex1.neighbours:
                if v not in q:
                    node_vertex2 = self.vertices[v]
                    if node_vertex2.color == 'black': #CHECK IF NEIGHBOUR IS TRAVERSED OR NOT, IF NOT APPEND TO Q
                        q.append(v)
                        if node_vertex2.dist > node_vertex1.dist + 1:
                            node_vertex2.dist = node_vertex1.dist + 1
                            order.append(v)
        print("TRAVERSAL ORDER IS {0}".format(order))
        return



print("--------------------#TESTCASE-----------------")
gp = Graph() #INSTANTIATE GRAPH
# GET THE NUMBER OF VERTICES IN THE GRAPH
print("Enter Number of Vertices:")
num_vertices = int(input())
_vertices = []
print('Enter the starting Vertex')
k = Vertex(input()) #INSTANTIATE FIRST VERTEX
_vertices.append(gp.add_vertex(k)) #ADD FIRST VERTEX TO GRAPH
for l in range(num_vertices-1):
    print("Enter Name of {0} vertex (other vertex)".format(l+1))
    _vertices.append(gp.add_vertex((Vertex(input())))) #ADD OTHER VERTICES

#ADD THE EDGES TO THE ABOVE VERTICES BY TAKING THE NEIGHBOURS/NEAR VERTICES OF THE VERTEX
_edges = []
for vertex in _vertices:
    num_neigh = 0
    print('Enter the number of neighbours of vertex {0}'.format(vertex))
    num_neigh = int(input())
    for j in range(num_neigh):
        print("Enter Name of neighbour of {0}".format(vertex))
        z = input()
        #COMMENT THE BELOW GIVEN CONDITION FOR A DIRECTED GRAPH
        if z+vertex not in _edges and vertex+z not in _edges: #CHECK IF THE VERTEX IS REPEATED OR NOT
            _edges.append(vertex+z)
        else:
            print('Edge already present!')

print("THE FORMED EDGES ARE: {0}".format(_edges))

#ADD THE EDGES TO THE GRAPH
for edge in _edges:
    gp.add_edge(edge[:1], edge[1:])
#DO THE BREADTH FIRST SEARCH
gp.breadth_first_search(k)
#DISPLAY THE OUTPUT
gp.display_graph()


'''
#UNCOMMENT THE SECTION BELOW TO CHECK FOR THE PROVIDED GRAPH
g = Graph() #INSTANTIATE GRAPH
#ADD VERTEX
a = Vertex('A')
g.add_vertex(a)

g.add_vertex(Vertex('B'))
#ADD MORE VERTICES
for i in range(ord('A'), ord('K')):
    g.add_vertex((Vertex(chr(i))))
#ADD EDGES
edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
    g.add_edge(edge[:1], edge[1:])
#DO THE BFS
g.breadth_first_search(a)
#DISPLAY THE GRAPH
g.display_graph()
#TEST CASE 2
'''
