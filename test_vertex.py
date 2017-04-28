
# Vertex.is_vertex(V[0]) == True
# Vertex.is_vertex(otan_list) == False
# Vertex.all_vertex(V) == True
# Vertex.all_vertex(otan_list) == False
# Vertex.all_vertex(V + otan_list) == False
# v = V[0]
# v1 = Vertex(1)
# v2 = Vertex(2)
# v.add_edges(v1) == True
# v.outdeg == 1
# v1.indeg == 1
# v.add_edges(v2) == True
# v.outdeg == 2
# v2.indeg == 1
# v.indeg == 0
# v1.outdeg == 0
# v2.outdeg == 0
# v.remove_edges(v1) == True
# v.outdeg == 1
# v1.indeg== 0
# v.indeg == 0
# v1.outdeg == 0
# v2.outdeg == 0
# v2.indeg == 1
# v.add_edges(V) == True
# [i.indeg for i in V] == [1, 1, 1]
# v.add_edges(V[1:]) == True
# [i.indeg for i in V] == [1, 2, 2]
# v.remove_edges(V)
# [i.indeg for i in V] ==> [0, 1, 1]
# v.remove_edges(V) == True
# [i.indeg for i in V] ==> [0, 0, 0]
