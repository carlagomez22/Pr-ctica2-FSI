# Search methods

import search

initials = [("A", "B"), ("O", "E"), ("G", "Z"), ("N", "D"), ("M", "F")]


for first, second in initials:
    print("--------------------------------------------")
    print(f"Problema de {first} to {second}")
    ab = search.GPSProblem(first, second
                           , search.romania)
    path, visited, generated, cost = search.breadth_first_graph_search(ab)
    print(f"ANCHURA: Camino: {path.path()}. Nodos visitados (lista cerrada): {visited}. Generados: {cost}")

    path1, visited1, generated1, cost1 = search.depth_first_graph_search(ab)
    print(f"PROFUNDIDAD: Camino: {path1.path()}. Nodos visitados (lista cerrada): {visited1}. Generados: {cost1}")
    print("--------------------------------------------")


# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
