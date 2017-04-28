# -*- coding: utf-8 -*-
#!/usr/bin/env python

data =[
    {
        "name":"ALPHA",
        "code":"A"
    },
    {
        "name":"UNIFORME",
        "code":"U"
    },
    {
        "name":"ZULU",
        "code":"Z"
    }
]


class Otan(object):
    id = 1

    def __init__(self, name, code):
        self.id = Otan.id
        self.name = name
        self.code = code

    def __getitem__(self, item):
        return getattr(self, item)
otan_list = [Otan(i["name"], i["code"]) for i in data]


class Node:
    """
    id_param: str: nome identificador do node
    """
    def __init__(self, struct, id_param=None, **kwargs):
        self.data = struct
        if id_param is not None:
            self.id = self.data[id_param]
        elif hasattr(struct, "id"):
            self.id = self.data["id"]

        for key, values in kwargs.items():
            self[key] = kwargs[values]
node_list = [Node(i, "code") for i in otan_list]

case1 = otan_list[0]
case1.id = "xyz"
test1 = Node(case1)
print "teste node com entrada que tem atributo id", test1.__dict__


class Vertex(Node):
    """
    func: function: funcao que o vertex pode aplicar
    """
    def __init__(self, struct, weight=1, id_param=None, func=None):
        Node.__init__(self, struct, id_param)
        """
        WIKI:
        Fiz esse erro e nao sei o por que dele:
        super(Node, self).__init__(struct, id_param)
        TypeError: must be type, not classobj
        """
        self.weight = weight
        self.apply = func
        self.outdeg = 0
        self.indeg = 0
        self.edges = []

    def degrees(self):
        return self.outdeg + self.indeg

    @staticmethod
    def is_vertex(v):
        return isinstance(v, Vertex)

    @staticmethod
    def all_vertex(vertexes):
        # any(map(Vertex.is_vertex, vertex))
        if type(vertexes) is not list:
            print "Expected a Vertex or list of Vertex\n" \
                "received ", type(vertexes)
            return None
        n = len(vertexes)
        for v, i in zip(vertexes, range(n)):
            if not Vertex.is_vertex(v):
                print "Expected only Vertex in the list\n", \
                    "pos: ", i, "is ", type(v)
                return False
        return True

    def add_edges(self, vertexes):
        if Vertex.is_vertex(vertexes):
            self.edges.append(vertexes)
            self.outdeg += 1
            vertexes.indeg += 1
            return True
        elif Vertex.all_vertex(vertexes):
            self.edges += vertexes
            self.outdeg += len(vertexes)
            for v in vertexes:
                v.indeg += 1
            return True
        return False

    def remove_edges(self, vertexes, id_param=None):
        if Vertex.is_vertex(vertexes) and vertexes in self.edges:
            self.edges.remove(vertexes)
            self.outdeg -= 1
            vertexes.indeg -= 1
            return True
        elif Vertex.all_vertex(vertexes):
            n = len(vertexes)
            for v, i in zip(vertexes, range(n)):
                if v in self.edges:
                    self.edges.remove(v)
                    self.outdeg -= 1
                    v.indeg -= 1
                else:
                    print "Vertex ", v, "is not a neighbour", "pos: ", i
            print "all CONTAINED vertex removed"
            return True
        return False

V = [Vertex(i) for i in otan_list]

class Graph():
    def __init__(self, struct, *args, **kwargs):
        # TODO: check if they all exists first
        matrix = kwargs.matrix
        matrix_tam = kwargs.matrix_tam
        self.oriented = kwargs.oriented
        vertex2 = kwargs.vertex2
        if matrix:
            print "create matrix TAM", matrix_tam
            pass
        if self.oriented:
            print "create oriented graph relating the vertex1 sending to vertex2"
        if vertex2:
            print "relate vertex1 to vertex 2, observing the orientation"

    def connectVertex(self, vertex1,vertex2, weigth=1, bidirectional=True,*args):
        bidirectional = bidirectional if self.oriented else True
        print("faz grafo de ", vertex1, "para", vertex2 )
        # TODO verificar se os argumentos são estruturas ou são grafos
        if self.oriented:
            print "ligação orientada"
        else:
            print "ligação não orientada"


    def disconnectVertex(self):
        pass

    def removeVertice(self):
        pass

    # inverse the edges between two vertices
    def inverseVertices(self):
        pass

    # inverse the in/out edges
    def inverseDegree(self):
        pass

    # invertice all edges for all vertices
    def inverseAll(self):
        pass

    # map is function which will set the weight according to the function
    def setWeigth(self, vertex1, vertex2, weigth, map=None):
        pass

    # map apply the function to the dfs, still not clear how it will do that
    def deep_first_search(self, vertex, map=None):
        pass
    dfs = deep_first_search

    # map apply the function to the dfs, still not clear how it will do that
    def breadth_first_search(self, vertex, map=None):
        pass
    bfs = breadth_first_search

    def hasCycle(self):
        print "checa o próprio grafo em busca de ciclo"

    def isBipartite(self):
        print "retorna pra ver se grafo é um grafo bipartido"

    def returnTree(self, vertex, ordered=0):
        print "retorna árvore a partir do vertex, "
        # ordered = 0 significa buscar na ordem que está
        # ordered = 1 significa buscar na ordem crescente do peso das arestas
        # ordered = -1 significa buscar na ordem decrescente do peso das arestas

    # dkistra é o menor caminho de pesos?
    def Dkistra(self):
        pass

    def update_weights(self, map):
        # print atualiza todos os pesos de acordo com a função map
        pass

    def get_in_degree(self, vertex):
        print "obtém grau de entrada"

    def get_out_degree(self, vertex):
        print "obtém grau de saída"

