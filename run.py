# Search methods

import search
from time import time

initials = [("A", "B"), ("O", "E"), ("G", "Z"), ("N", "D"), ("M", "F")]


for first, second in initials:
    print("--------------------------------------------")
    print(f"Problema de {first} to {second}")
    ab = search.GPSProblem(first, second
                           , search.romania)
    start_time = time()
    path, visited, generated, cost = search.breadth_first_graph_search(ab)
    end_time = time()
    print(f"ANCHURA: Camino: {path}. Nodos visitados (lista cerrada): {visited}. Generados: {generated}. Coste {cost}. Tiempo = {end_time-start_time}")

    start_time = time()
    path1, visited1, generated1, cost1 = search.depth_first_graph_search(ab)
    end_time = time()
    print(f"PROFUNDIDAD: Camino: {path1}. Nodos visitados (lista cerrada): {visited1}. Generados: {generated1}. Coste {cost1}. Tiempo = {end_time-start_time}")

    start_time = time()
    path2, visited2, generated2, cost2 = search.branch_and_bround(ab)
    end_time = time()
    print(f"Brand & Bound: Camino: {path2}. Nodos visitados (lista cerrada): {visited2}. Generados: {generated2}. Coste {cost2}. Tiempo = {end_time-start_time}")

    start_time = time()
    path2, visited2, generated2, cost2 = search.branch_and_bround_with_subestimnation(ab)
    end_time = time()
    print(f"Brand & Bound with H: Camino: {path2}. Nodos visitados (lista cerrada): {visited2}. Generados: {generated2}. Coste {cost2}. Tiempo = {end_time-start_time}")
    print("--------------------------------------------")


# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
