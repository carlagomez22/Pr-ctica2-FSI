# Practica2-FSI


## Parte 1 y Parte 2:

En estas partes de la práctica se pide, a partir del código proporcionado, realizar una implementación del algoritmo de Ramificación y Acotación (Branch and Bound) y el Ramificación y Acotación con subestimación.
Siguiendo la filosofía del programa proporcionado, creamos en el archivo utils.py una estructura de datos, basándonos en las ya existentes en el archivo (Stack() y FIFOQueue()), a la que llamamos OrderedList(). Como su nombre indica, implementa una lista que se va ordenando a medida que se van añadiendo los elementos. Similarmente replicamos esta estructura pero aplicando el cálculo de la heurística para el algoritmo correspondiente a la parte 2 del trabajo. 

Se presenta a continuación el código correspondiente a las dos estructuras mencionadas.
``` 
class OrderedList():

    def __init__(self):
        self.A = []
        self.start = 0

    def append(self, node):
        self.A.append(node)
        self.A.sort(key= lambda x: x.path_cost)

    def __len__(self):
        return len(self.A) - self.start

    def extend(self, items):
        self.A.extend(items)
        self.A.sort(key=lambda x: x.path_cost)

    def pop(self):
        e = self.A[self.start]
        self.start += 1
        if self.start > 5 and self.start > len(self.A) / 2:
            self.A = self.A[self.start:]
            self.start = 0
        return e
``` 


```
class OrderedListWithH():

    def __init__(self, problem):
        self.A = []
        self.start = 0
        self.problem = problem

    def append(self, node):
        self.A.append(node)
        self.A.sort(key=lambda x: x.path_cost + self.problem.h(x))

    def __len__(self):
        return len(self.A) - self.start

    def extend(self, items):
        self.A.extend(items)
        self.A.sort(key=lambda x: x.path_cost + self.problem.h(x))

    def pop(self):
        e = self.A[self.start]
        self.start += 1
        if self.start > 5 and self.start > len(self.A) / 2:
            self.A = self.A[self.start:]
            self.start = 0
        return e
```

Para la aplicación del algoritmo, simplemente utilizamos la función ya implementada graph_search(fringe) al que llamamos desde los métodos específicos para los dos problemas que estamos tratando:
              
                          def branch_and_bround(problem):
                              return graph_search(problem, OrderedList())

                          def branch_and_bround_with_subestimnation(problem):
                              return graph_search(problem, OrderedListWithH(problem))
                    

## Parte 3

En la tercera parte del trabajo se pide alterar la función graph_search(fringe) para añadir lo siguiente:
  - Número de nodos generados
  - Número de nodos visitados
  - La ruta solución encontrada
  - Coste total de la solución encontrada.

Para la ruta solución, la clase Node ya va almacenando el camino recorrido, por lo que no almacenamos todas subrutas que se iban calculando en este método. Para los nodos visitados y los nodos generados, inicializamos contadores que se iban incrementando en las partes correspondientes del código. Por último, para devolver el costo de la ruta, nos creamos una función para tal fin. En ésta, vamos recorriendo toda la solución del problema y para cada nodo en ella, llamamos la función del problem llamada path_cost para ir acumulando el coste de la arista del nodo actual con el anterior.

También se nos pide calcular el tiempo de ejecución de la búsqueda, por lo que modificamos el run.py usando sencillamente la función de Python del módulo time llamada time(). También modificamos el run.py para que aplique, de manera automática y para cada par origen-destino propuesto, los algoritmos tratados en el trabajo. 

Así ha quedado el run.py después de las modificaciones descritas previamente:

```
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
```

Y la función modificada ha quedado de la siguiente manera:

```
def graph_search(problem, fringe):
    """Search through the successors of a problem to find a goal.
    The argument fringe should be an empty queue.
    If two paths reach a state, only use the best one. [Fig. 3.18]"""
    closed = {}
    fringe.append(Node(problem.initial))
    generated_nodes = 1
    visited_nodes = 0
    while fringe:
        node = fringe.pop()
        visited_nodes += 1
        if problem.goal_test(node.state):
            return list(reversed(node.path())), visited_nodes, generated_nodes, calculate_accumulate_path(node, problem)
        if node.state not in closed:
            closed[node.state] = True
            fringe.extend(node.expand(problem))
            generated_nodes += len(node.expand(problem))
    return None
```
      

Traza del Branch and Bound de A a B:

![AISelect_20251218_162113_Samsung Notes](https://github.com/user-attachments/assets/528675a7-0041-4b9d-bb14-4bd6153b7a2e)



