# -*- coding: utf-8 -*-
#!/usr/bin/env python

def to_list(elem):
    if hasattr(elem, "__iter__"):
        return elem
    return [elem]

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
        Otan.id += 1
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
    # TODO implementar get_neighbors, para nao ficar pegando da adj
    def __init__(self, struct, weight=1, id_param=None, func=None):
        Node.__init__(self, struct, id_param)
        """
        WIKI:
        Fiz esse erro e nao sei o por que dele:
        super(Node, self).__init__(struct, id_param)
        TypeError: must be type, not classobj
        """
        if type(struct) in (int,float,str):
            self.id = struct
        elif not hasattr(self, "id"):
            # TODO exception, cancelar criacao da classe
            print "classe precisa ter identificação"


        self.weight = weight
        self.apply = func
        self.outdeg = 0
        self.indeg = 0
        self.adj = []

    def degrees(self):
        return self.outdeg + self.indeg

    @staticmethod
    def is_vertex(v):
        return isinstance(v, Vertex)

    @staticmethod
    def all(vertexes):
        # any(map(Vertex.is_vertex, vertex))
        if type(vertexes) is not list:
            print "Expected a Vertex or list of Vertex\n" \
                "received ", type(vertexes)
            return None
        n = len(vertexes)
        for v, i in zip(vertexes, range(n)):
            if not Vertex.is_vertex(v):
                print "Expected only Vertex in the list\n", \
                    "pos: ", i, "is ", v
                return False
        return True

    def has_adjacent(self, vertex):
        n = len(self.adj)
        for e, i in zip(self.adj, range(n)):
            if e.v is vertex:
                return i
        return -1

    def add(self, v, weight=1):
        e = Edge(v, weight=weight)
        self.adj.append(e)
        self.outdeg += 1
        v.indeg += 1
        return True

    def remove(self, v):
        for e, i in zip(self.adj, range(len(self.adj))):
            if e.v is v:
                self.adj.remove(e)
                self.outdeg -= 1
                v.indeg -= 1
                return True
        print "vertice", v, "nao eh adjcente a", self
        return False

V = [Vertex(i) for i in otan_list]
V2 = [Vertex(i) for i in otan_list]
V3 = [Vertex(i) for i in otan_list]
a = Vertex(1)

class Edge:
    def __init__(self, adj_v, struct=None, weight=1):
        self.struct = struct
        self.v = adj_v
        self.weight = weight if weight is not None else 1

    @staticmethod
    def get_weight(v1, v2):
        print v1.adj
        for e in v1.adj:
            print e.v, v2
            if e.v is v2:
                print e.weight
                return e.weight if e.weight!=0 else "0"
        return False

    @staticmethod
    # map is function which will set the weight according to the function
    def setWeigth(v1, v2, weight, map=None):
        for e in v1.adj:
            if e.v is v2:
                e.weight = weight
                return True
        return False

class Graph():
    def __init__(self, edges=[], vertexes=[], oriented=True, matrix=False, matrix_tam=None):
        # TODO: check if they all exists first
        self.oriented = oriented
        self.vertexes = set(vertexes)
        for v in vertexes:
            self.vertexes |= set(map(lambda x: x.v, v.adj))
        for e in edges:
            self.conn(e[0], e[1])
            if not self.oriented:
                self.conn(e[1], e[0])

        if matrix:
            print "create matrix TAM", matrix_tam
            pass


    def conn(self, vertex, vertexes, weights=None):
        # TODO: minimizar código em relação a #pesos e #vertice
        vertexes = to_list(vertexes)
        # TODO tratamento meio merda, será que não melhora?
        if weights is not None:
            weights = to_list(weights)
            if len(weights) != len(vertexes):
                # print "pesos e vertexes precisam ter o mesmo tamanho"
                return False
        else:
            weights = [None]*len(vertexes)

        if Vertex.all(vertexes):
            for v, w in zip(vertexes, weights):
                vertex.add(v,w)
                self.vertexes |= {vertex, v}
                if not self.oriented:
                    self.conn(v, vertex, w)
            return True
        return False

    def disconn(self, vertex, vertexes, id_param=None, filter=lambda x: True, *args):
        vertexes = to_list(vertexes)
        removed = False
        if Vertex.all(vertexes):
            n = len(vertexes)
            for v, i in zip(vertexes, range(n)):
                if vertex.has_adjacent(v) != -1 and \
                        filter(args):
                    removed = vertex.remove(v)
                    if not self.oriented:
                        self.disconn(v, vertex)
                else:
                    pass
                    # print "Vertex", v, "is not a neighbour", "pos:", i
            # print "all CONTAINED vertex removed"
            return removed
        return False

    def remove_vertex(self, vertex):
        # TODO: melhorar, tem muita redundância
        # ou não pois está bem simples e reusável assism
        while(vertex.adj):
            v = vertex.adj[0].v
            self.disconn(vertex, v)
            self.disconn(v, vertex)
        self.vertexes -= {vertex}
        return True

    def print_adj(self):
        for v in self.vertexes:
            print v.id, "->",
            for e,i in zip(v.adj, range(len(v.adj))):
                print e.v.id,
                if len(v.adj)-1 > i:
                    print ",",
            print "\n" #parece que esse código faz flush, não é isso?
        return True

    # inverse the edges between two vertices
    def inverse_edges(self, v1, v2):
        w1 = w2 = False
        if v1.has_adjacent(v2) !=-1:
            print "hey", v1.adj
            w1 = Edge.get_weight(v1,v2)
            self.disconn(v1,v2)
        if v2.has_adjacent(v1) != -1:
            w2 = Edge.get_weight(v2,v1)
            self.disconn(v2,v1)
        if w1:
            w1 = 0 if w1 == "0" else w1
            self.conn(v2, v1, w1)
        if w2:
            w2 = 0 if w2 == "0" else w2
            self.conn(v1, v2, w2)
        return True

    # inverse the in/out edges of an vertex
    def inverse_degree(self, vertex):
        temp = list(vertex.adj)
        for e in temp:
            self.inverse_edges(vertex, e.v)
        return True

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

    # invertice all edges for all vertices NÃO
    def inverseAll(self):
        # implementar dfs primeiro
        pass

    # gera grafo onde todas os sentidos tendem a um vertice
    # árvore com o sentido apontado sempre pro pai
    def concentrate(self):
        pass

    # gera grafo onde todos os sentidos sao repelidos do vertice
    # árvore com o sentido apontado para o filho
    def dispersate(self):
        pass

    def update_weights(self, map):
        # print atualiza todos os pesos de acordo com a função map
        pass
