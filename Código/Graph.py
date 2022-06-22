# -*- coding: utf-8 -*-
"""
PROYECTO O4
Unidad: Diseño y Análisis de Algoritmos
Alumno: Raquel Eugenia Meléndez Zamudio
Junio 2022
CLASE GRAFO 
IMPLEMENTACIÓN DE ALGORITMOS KRUSKAL (DIRECTO E INVERSO) Y PRIM
"""

# Se importan las clases Nodo y Arista
# Se importan las librerías necesarias
from Node import node
from Edge import edge

import heapdict
import numpy as np
import copy
import random


class graph:

    # Atributos de la clase grafo
    def __init__(self, directed=False):
        self.name = 'Graph'
        self.directed = directed
        self.nodes = set(())
        self.edges = set(())
        self.distances = {}
        self.weights = {}

    # Se verifica la existencia del nodo con el parámetro nombre
    # Si existe regresa un 1
    def ExistingNode(self, name):
        for i in self.nodes:
            if i.id == name:
                return 1

    # Se verifica la existencia de la arista con el parámetro nombre
    # Si existe regresa un 1
    def ExistingEdge(self, name):
        for i in self.edges:
            if i.id == name:
                return 1

    # Aumenta el grado del nodo ingresado
    def n_degree(self, name):
        for i in self.nodes:
            n = int(i.id)
            if name == n:
                i.dg = i.dg + 1
                return 1

    # Agrega un nodo con el nombre ingresado como parámetro
    # Si el nodo existe regresa un 0 de lo contrario agrega el nodo y regresa un 1
    def AddNode(self, name):
        if self.ExistingNode(name) == 1:
            a = 0
        else:
            n_node = node(name)
            self.nodes.add(n_node)
            a = 1

        return a

    # Agrega una arista del nodo n0 al nodo n1
    # Si la arista existe regresa un 0 de lo contrario agrega la arista y regresa un 1
    # Cuando se agrega la arista aumenta el grado del nodo n0 y n1

    def AddEdge(self, n0, n1):

        if self.directed == False:
            name = str(n0) + ' -- ' + str(n1)
        else:
            name = str(n0) + ' --> ' + str(n1)

        if self.ExistingEdge(name) == 1:
            a = 0
        else:
            if self.ExistingNode(n0) == 0 or self.ExistingNode(n1) == 0:
                a = 0
            else:
                n_edge = edge(name, str(n0), str(n1))
                self.edges.add(n_edge)
                a = 1

                self.n_degree(n0)
                self.n_degree(n1)

        return a, name

    # Obtiene el nodo indicado por su nombre
    def getNode(self, name):

        for i in self.nodes:
            if i.id == name:
                return i

    # Obtiene la arista indicada por su nombre
    def getEdge(self, name):
        for i in self.edges:
            if i.id == name:
                return i
    # Obtiene la arista indicada por su nombre

    def getEdge_n(self, name):
        e = 0
        for i in self.edges:
            if e == name:
                return i
            e = e + 1

    # Se muestra el grafo generado enlistando en primera instancia los nodos
    # y posteriormente las aristas
    def showGraph(self):
        value = "Nodes: "

        for i in self.nodes:
            value = value + str(i.id) + ', '

        value = value + '\nEdges: '

        for j in self.edges:
            value = value + str(j.id) + ', '

        return print(value)

    # Se convierte el grafo al formato necesario para generar el archivo .gv
    def convertGraphViz(self):
        value = 'graph{\n'
        for i in self.edges:
            value = value + str(i.id) + ';\n'
        value = value + '}\n'

        return value

    # Se convierte el grafo al formato necesario para generar el archivo .gv (Dijkstra)
    def convertGraphViz_Dijkstra(self, d):

        edges_split = list([None]*len(self.edges))
        cont = 0

        for i in self.edges:
            edges_split[cont] = str(i).split(sep=' -- ')
            cont = cont + 1

        cont1 = 0
        for i, j in edges_split:
            edges_split[cont1][0] = int(i)
            edges_split[cont1][1] = int(j)
            cont1 += 1

        value = 'graph{\n'

        for i in edges_split:
            d1 = d[str(i[0])][0]
            d2 = d[str(i[1])][0]
            value = value + '"' + str(i[0]) + " (" + str(d1) + ")" + '"' + \
                " -- " + '"' + str(i[1]) + " (" + str(d2) + ")" + '"' + ';\n'

        value = value + '}\n'

        return value

    # Se genera el archivo .gv con el nombre ingresado y el número de nodos en el grafo
    def fileGraphViz(self, file_name):
        graph2save = self.convertGraphViz()
        f = open(file_name + str(len(self.nodes)) + '.gv', 'w+')
        f.write(graph2save)

    # Se genera el archivo .gv para el algoritmo DIjkstra con el nombre ingresado y el número de nodos en el grafo
    def fileGraphViz_Dijkstra(self, file_name, d):
        graph2save = self.convertGraphViz_Dijkstra(d)
        f = open(file_name + str(len(self.nodes)) + '.gv', 'w+')
        f.write(graph2save)

    # Se genera un árbol con el algoritmo BFS (Breadth First Search)
    # dado un nodo fuente s
    def BFS(self, s):

        # Se genera el grafo
        gph_bfs = graph()

        # Se agrega el nodo fuente al grafo
        gph_bfs.AddNode(s)

        # Se genera la primer capa que contiene al nodo fuente
        L0 = [s]

        # Se genera el conjunto donde estarán los nodos descubiertos
        discovered = set()

        # Se crea una lista vacía y se separan las aristas guardadas
        # para la obtención de los nodos source y target de cada una
        # y se guardan en la lista creada
        edges_split = list([None]*len(self.edges))
        cont = 0

        for i in self.edges:
            edges_split[cont] = str(i).split(sep=' -- ')
            cont = cont + 1

        cont1 = 0
        for i, j in edges_split:
            edges_split[cont1][0] = int(i)
            edges_split[cont1][1] = int(j)
            cont1 += 1

        while True:

            # Se crea la nueva capa
            L1 = []

            # Se guardan las aristas incidentes a los nodos en L0,
            # se guardan los, se agregan a discovered en caso no de no
            # haber sido explorados y se agregan a la capa L1.
            # La capa L1, pasa a ser la capa L0.
            # Si la capa L0 esta vacía el ciclo termina.
            for nd in L0:

                edges_a = []

                for id_Edges in edges_split:
                    if nd in id_Edges:
                        edges_a.append(id_Edges)

                for edg in edges_a:
                    if nd == edg[0]:
                        nn = edg[1]
                    else:
                        nn = edg[0]

                    if nn in discovered:
                        continue

                    gph_bfs.AddNode(nn)
                    gph_bfs.AddEdge(edg[0], edg[1])
                    discovered.add(nn)
                    L1.append(nn)

            L0 = L1

            if not L0:
                break

        return gph_bfs

    # Función recursiva para el algoritmo DFS recursivo que permite
    # agregar nodos y aristas dados un nodo, un grafo y la lista
    # de nodos explorados

    def DFS_aux(self, s, dfs_graph, discovered):

        # Se agrega al grafo y a la lista de explorados al nodo dado
        dfs_graph.AddNode(s)
        discovered.add(s)

        # Se crea una lista vacía y se separan las aristas guardadas
        # para la obtención de los nodos source y target de cada una
        # y se guardan en la lista creada
        edges_split = list([None]*len(self.edges))
        cont = 0

        for i in self.edges:
            edges_split[cont] = str(i).split(sep=' -- ')
            cont = cont + 1

        cont1 = 0
        for i, j in edges_split:
            edges_split[cont1][0] = int(i)
            edges_split[cont1][1] = int(j)
            cont1 += 1

        # Para cada arista que sale del nodo s se guarda el nodo que no
        # es el nodo s y se agrega a la lista de nodos explorados.
        # Se agregan las aristas al grafo.
        # Se realiza la recursión.
        edges_a = []
        for id_Edges in edges_split:
            if s in id_Edges:
                edges_a.append(id_Edges)

        for edg in edges_a:
            nd = edg[1]

            if not self.directed:
                if s == edg[1]:
                    nd = edg[0]
                else:
                    nd = edg[1]

            if nd in discovered:
                continue

            dfs_graph.AddEdge(edg[0], edg[1])

            self.DFS_aux(nd, dfs_graph, discovered)

    # Se genera un árbol con el algoritmo DFS (Depth First Search) recursivo
    # dado un nodo fuente s
    def recursiveDFS(self, s):

        gph_dfs = graph()

        discovered = set()

        self.DFS_aux(s, gph_dfs, discovered)

        return gph_dfs

    # Se genera un árbol con el algoritmo DFS (Depth First Search) iterativo
    # dado un nodo fuente s
    def iterativeDFS(self, s):

        # Se genera el grafo
        gph_dfs = graph()

        # Se genera la lista de nodos explorados y se agrega el nodo fuente
        discovered = set()
        discovered.add(s)

        n0 = s

        f = []

        # Se crea una lista vacía y se separan las aristas guardadas
        # para la obtención de los nodos source y target de cada una
        # y se guardan en la lista creada
        edges_split = list([None]*len(self.edges))
        cont = 0

        for i in self.edges:
            edges_split[cont] = str(i).split(sep=' -- ')
            cont = cont + 1

        cont1 = 0
        for i, j in edges_split:
            edges_split[cont1][0] = int(i)
            edges_split[cont1][1] = int(j)
            cont1 += 1

        while True:

            edges_a = []

            # Se buscan las aristas incidentes al nodo dado
            # Se guarda el nodo target en n1
            for id_Edges in edges_split:
                if n0 in id_Edges:
                    edges_a.append(id_Edges)

            for edg in edges_a:
                if n0 == edg[0]:
                    n1 = edg[1]
                else:
                    n1 = edg[0]

                if n1 not in discovered:
                    f.append((n0, n1))

            # Si la pila esta vacía, termina el ciclo
            if not f:
                break

            # Hasta que el nodo c sale de la pila se agrega a los nodos explorados.
            # Se agrega el nodo.
            # Se agrega la arista.
            p, c = f.pop()

            if c not in discovered:
                gph_dfs.AddNode(c)
                gph_dfs.AddEdge(p, c)
                discovered.add(c)

            # El nodo explorado pasa a ser el nodo source
            n0 = c

        return gph_dfs

    # Se genera el árbol de caminos más cortos con el algoritmo Dijkstra
    # dado un nodo fuente s
    def Dijkstra(self, s):

        # Se genera el grafo
        gph_djks = graph()

        # Se declaran las estructuras de datos a utilizar
        l = heapdict.heapdict()
        p = dict()
        i_t = set()

        l[s] = 0
        p[s] = None

        # Asigna distancias infinitas a los nodos y a los padres None
        for node in self.nodes:
            l[node.id] = np.inf
            p[node.id] = None

        # Asigna al nodo s la distancia 0
        l[s] = 0
        # Asigna al padre de s None
        p[s] = None

        # Se crea una lista vacía y se separan las aristas guardadas
        # para la obtención de los nodos source y target de cada una
        # y se guardan en la lista creada
        edges_split = list([None]*len(self.edges))
        cont = 0

        for i in self.edges:
            edges_split[cont] = str(i).split(sep=' -- ')
            cont = cont + 1

        cont1 = 0
        for i, j in edges_split:
            edges_split[cont1][0] = int(i)
            edges_split[cont1][1] = int(j)
            cont1 += 1

        # Ciclo while que se realiza mientras l no este vacía
        # y mientras aún existan distancias Infinitas
        while l:
            # Se saca de l el nombre del último nodo agregado y su distancia
            n0, n0_dist = l.popitem()

            if n0_dist == np.inf:
                continue

            nd = self.getNode(n0)
            nd.dis = n0_dist
            nd = int(str(nd))

            # Se guradan las distancias en el diccionario distances
            if str(nd) in self.distances.keys():
                self.distances[str(nd)] = self.distances[nd].append(n0_dist)
            else:
                self.distances[str(nd)] = [n0_dist]

            # Se agrega el nodo al grafo
            gph_djks.AddNode(nd)

            # Se agrega la arista al grafo si el padre del nodo no es None
            if p[nd] is not None:
                gph_djks.AddEdge(p[nd], nd)

            i_t.add(nd)

            # Se obtinen los nodos vecinos
            neighbor = []

            for id_Edges in edges_split:
                if nd in id_Edges:
                    if nd == id_Edges[1]:
                        n1 = id_Edges[0]
                    else:
                        n1 = id_Edges[1]
                    if n1 not in i_t:
                        neighbor.append(n1)

            # Se actualizan las distancias
            for n1 in neighbor:
                e = np.array([nd, n1])
                for i in edges_split:
                    if e[0] == i[0]:
                        if e[1] == i[1]:
                            edg = str(nd) + ' -- ' + str(n1)
                    elif e[0] == i[1]:
                        if e[1] == i[0]:
                            edg = str(n1) + ' -- ' + str(nd)

                e = self.getEdge(edg)

                if l[n1] > n0_dist + e.weight:
                    l[n1] = n0_dist + e.weight
                    p[n1] = n0

        return gph_djks, self.distances

    # Función que permite calcular el valor/costo del árbol de expansión mínimo (MST)
    def value_MST(self):
        c = 0

        for i in self.edges:
            edg = self.getEdge(str(i))
            c += edg.weight

        return c

    # Función que genera un grafo de tipo árbol utilizando el algoritmo Kruskal Directo
    # y calcula el árbol de expansión mínima (MST)
    def KruskalD(self):

        # Se genera el grafo
        gph_mst = graph()

        # Se crea una lista vacía y se separan las aristas guardadas
        # para la obtención de los nodos source y target de cada una
        # y se guardan en la lista creada
        edges_split = list([None]*len(self.edges))
        cont = 0

        for i in self.edges:
            edges_split[cont] = str(i).split(sep=' -- ')
            cont = cont + 1

        cont1 = 0
        for i, j in edges_split:
            edges_split[cont1][0] = int(i)
            edges_split[cont1][1] = int(j)
            cont1 += 1

        # Se almacenan los pesos de cada arista en un diccionario
        cont2 = 0
        for i in self.edges:
            e = self.getEdge(str(i))
            if str(edges_split[cont2]) in self.weights.keys():
                self.weights[str(edges_split[cont2])] = self.weights[str(edges_split[cont2])].append(e.weight)
            else:
                self.weights[str(edges_split[cont2])] = [e.weight]
            
            cont2 = cont2 + 1
        
        # Se ordenan las aristas conforme a su peso de forma ascendente
        edges_s = sorted(self.weights.items(), key = lambda edge: edge[1])
        
        edges_s1 = []
        cont = 0
        for i in edges_s:
            edges_s1.append(i[0])

        edges_sorted = []
        for i in edges_s1:
            edges_sorted.append(eval(i))

        connected_c = dict()

        # Componente conectado
        for node in self.nodes:
            node = int(str(node))
            connected_c[node] = node

        # Se agregan los nodos y aristas al MST iterando por peso
        for edg in edges_sorted:
            n0 = edg[0]
            n1 = edg[1]
            
            
            if connected_c[n0] != connected_c[n1]:
                gph_mst.AddNode(n0)
                gph_mst.AddNode(n1)
                gph_mst.AddEdge(n0, n1)

                name = str(n0) + ' -- ' + str(n1)
                edg_s = self.getEdge(name)
                edg_m = gph_mst.getEdge(name)
                edg_m.weight = edg_s.weight

            # Se cambia el componente conectado de n1
            # para que sea el mismo de n0
            for c in connected_c:
                if connected_c[c] == connected_c[n1]:
                    oc = connected_c[n1]
                    connected_c[c] = connected_c[n0]

                    it = (k for k in connected_c if connected_c[k] == oc)

                    for item in it:
                        connected_c[item] = connected_c[n0]
        
        # Se calcula el valor del árbol de expansión mínimo
        c = gph_mst.value_MST()
        print(f"Valor del MST con Kruskal Directo: {c}")

        return gph_mst
    
    # Función que crea una copia del grafo
    def copy_graph(self):

        o = graph()
        o.nodes = copy.deepcopy(self.nodes)
        o.edges = copy.deepcopy(self.edges)
        o.weights = copy.deepcopy(self.weights)
        o.distances = copy.deepcopy(self.distances)

        return o

    # Función que genera un grafo de tipo árbol utilizando el algoritmo Kruskal Inverso
    # y calcula el árbol de expansión mínima (MST)
    def KruskalI(self):
        
        # Se genera una copia del grafo
        gph_mst = self.copy_graph()

        # Se crea una lista vacía y se separan las aristas guardadas
        # para la obtención de los nodos source y target de cada una
        # y se guardan en la lista creada
        edges_split = list([None]*len(self.edges))
        cont = 0

        for i in self.edges:
            edges_split[cont] = str(i).split(sep=' -- ')
            cont = cont + 1

        cont1 = 0
        for i, j in edges_split:
            edges_split[cont1][0] = int(i)
            edges_split[cont1][1] = int(j)
            cont1 += 1

        # Se ordenan las aristas conforme a su peso de forma descendente
        edges_s = sorted(self.weights.items(), key = lambda edge: edge[1], reverse = True)

        edges_s1 = []
        cont = 0
        for i in edges_s:
            edges_s1.append(i[0])

        edges_sorted = []
        for i in edges_s1:
            edges_sorted.append(eval(i))

        
        for edg in edges_sorted:
            n0 = edg[0]
            n1 = edg[1]
            
            name = str(n0) + " -- " + str(n1)

            # Se van eliminando las aristas con mayor peso
            for i in gph_mst.edges:
                if name == str(i):
                    gph_mst.edges.discard(i)
                    break

            # Si el grafo no esta conectado despues de quitar la arista
            # se vuelve a agregar la arista
            if len(gph_mst.BFS(n0).nodes) != len(gph_mst.nodes):
                gph_mst.AddEdge(n0,n1)

                name = str(n0) + ' -- ' + str(n1)
                edg_s = self.getEdge(name)
                edg_m = gph_mst.getEdge(name)
                edg_m.weight = edg_s.weight

        # Se calcula el valor del árbol de expansión mínimo (MST)
        c = gph_mst.value_MST()
        print(f"Valor del MST con Kruskal Inverso: {c}")

        return gph_mst

    # Función que genera un grafo de tipo árbol utilizando el algoritmo de Prim
    # y calcula el árbol de expansión mínima (MST)
    def Prim(self):

        # Se genera el grafo
        gph_mst = graph()

        l = heapdict.heapdict()
        p = dict()
        i_t = set()

        # Se escoge un nodo inicial al azar
        s = int(str(random.choice(list(self.nodes))))

        # Se asgina al nodo s la distancia 0
        l[s] = 0
        # Se establece None como padre del nodo s
        p[s] = None

        # Asigna distancias infinitas a los nodos y a los padres None
        for node in self.nodes:
            if node.id == s:
                continue
            l[node.id] = np.inf
            p[node.id] = None

        # Se crea una lista vacía y se separan las aristas guardadas
        # para la obtención de los nodos source y target de cada una
        # y se guardan en la lista creada
        edges_split = list([None]*len(self.edges))
        cont = 0

        for i in self.edges:
            edges_split[cont] = str(i).split(sep=' -- ')
            cont = cont + 1

        cont1 = 0
        for i, j in edges_split:
            edges_split[cont1][0] = int(i)
            edges_split[cont1][1] = int(j)
            cont1 += 1

        edg_list = []
        for i in self.edges:
            edg_list.append(str(i))

        # Ciclo while que se realiza mientras l no este vacía
        # y mientras aún existan distancias Infinitas
        while l:
            # Se saca de l el nombre del último nodo agregado y su distancia
            n0, n0_dist = l.popitem()

            if n0_dist == np.inf:
                continue

            nd = self.getNode(n0)
            nd.dis = n0_dist
            nd = int(str(nd))

            # Se guradan las distancias en el diccionario distances
            if str(nd) in self.distances.keys():
                self.distances[str(nd)] = self.distances[nd].append(n0_dist)
            else:
                self.distances[str(nd)] = [n0_dist]

            # Se agrega el nodo al grafo
            gph_mst.AddNode(nd)

            # Se agrega la arista al grafo si el padre del nodo no es None
            if p[nd] is not None:
                if str(nd) + " -- " + str(p[nd]) in edg_list:
                    e = str(nd) + " -- " + str(p[nd])
                    e_g = self.getEdge(e)
                    weight = e_g.weight

                else:
                    e = str(p[nd]) + " -- " + str(nd)
                    e_g = self.getEdge(e)
                    weight = e_g.weight

                
                gph_mst.AddEdge(p[nd], nd)
                name = str(p[nd]) + ' -- ' + str(nd)

                e_h = gph_mst.getEdge(name)
                e_h.weight = weight

            i_t.add(nd)

            # Se obtinen los nodos vecinos
            neighbor = []

            for id_Edges in edges_split:
                if nd in id_Edges:
                    if nd == id_Edges[1]:
                        n1 = id_Edges[0]
                    else:
                        n1 = id_Edges[1]
                    if n1 not in i_t:
                        neighbor.append(n1)

            # Se actualizan los pesos
            for n1 in neighbor:
                e = np.array([nd, n1])
                for i in edges_split:
                    if e[0] == i[0]:
                        if e[1] == i[1]:
                            edg = str(nd) + ' -- ' + str(n1)
                    elif e[0] == i[1]:
                        if e[1] == i[0]:
                            edg = str(n1) + ' -- ' + str(nd)

                e = self.getEdge(edg)

                if l[n1] > e.weight:
                    l[n1] = e.weight
                    p[n1] = n0
        
        # Se calcula el valor del árbol de expansión mínimo MST
        c = gph_mst.value_MST()
        print(f"Valor del MST con Prim: {c}")

        return gph_mst
