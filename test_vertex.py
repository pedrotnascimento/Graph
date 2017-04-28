# -*- coding: utf-8 -*-
# FILOSOFIA:
# teste não é para ver está funcionando,
# é pra permitir que funcionar UMA VERSÃO MELHOR
# ou seja, não é só pra ver se está correto
# é pra quando FOR ADICIONAR UMA NOVA FEATURE
# VER SE NÃO QUEBROU O QUE JÁ TINHA ANTES

Vertex.is_vertex(V[0]) == True
Vertex.is_vertex(otan_list) == False
Vertex.all(V) == True
Vertex.all(otan_list) == False
Vertex.all(V + otan_list) == False
v = V[0]
v1 = Vertex(1)
v2 = Vertex(2)
v.add_edges(v1) == True
v.outdeg == 1
v1.indeg == 1
v.add_edges(v2) == True
v.outdeg == 2
v2.indeg == 1
v.indeg == 0
v1.outdeg == 0
v2.outdeg == 0
v.remove_edges(v1) == True
v.outdeg == 1
v1.indeg== 0
v.indeg == 0
v1.outdeg == 0
v2.outdeg == 0
v2.indeg == 1
v.add_edges(V) == True
[i.indeg for i in V] == [1, 1, 1]
v.add_edges(V[1:]) == True
[i.indeg for i in V] == [1, 2, 2]
v.remove_edges(V)
[i.indeg for i in V] ==> [0, 1, 1]
v.remove_edges(V) == True
[i.indeg for i in V] ==> [0, 0, 0]
g1 = Graph()
g1.conn(V[0], V[1]) == True
V[0].adj[0].weight == 1
g1.conn(V[0], V[1], 3) == True
V[0].adj[1].weight == 3
g1.conn(V[0], V[1], "banana") == True
V[0].adj[2].weight == "banana"
g1.conn(V[0], [V[1],V[2]], "banana") == False
g1.conn(V[0], [V[1],V[2]], ["fromage","apple"]) == True
V[0].adj[3].weight == "fromage"
V[0].adj[4].weight == "apple"
g1.disconn(V[0], V[2]) == True
g1.disconn(V[0], V[2]) == False
g1.disconn(V[0], V[1]) == True
g1.disconn(V[0], V[1]) == True
g1.disconn(V[0], V[0]) == False
g2 = Graph()
g2.conn(V2[0], [V2[1], V2[2]])
V2[0].adj[0].weight == 1
V2[0].adj[1].weight == 1
g2.remove_vertex(V2[0])
(V2[0].indeg, V2[0].outdeg) == (0,0)
(V2[1].indeg, V2[1].outdeg) == (0,0)
(V2[2].indeg, V2[2].outdeg) == (0,0)
g2 = Graph()
g2.conn(V2[0], [V2[1], V2[2]])
g2.conn(V2[1], [V2[0], V2[2]])
g2.conn(V2[2], [V2[0], V2[1]])
g2.remove_vertex(V2[0])
(V2[0].indeg, V2[0].outdeg) == (0,0)
(V2[1].indeg, V2[1].outdeg) == (1,1)
(V2[2].indeg, V2[2].outdeg) == (1,1)

a.add(V[0])
a.add(V[1])
a.add(V[2])
V[0].add(V[1])
g1= Graph(edges=[[V[2],V[1]]],vertexes=[a,V[0]])
g1.print_adj()