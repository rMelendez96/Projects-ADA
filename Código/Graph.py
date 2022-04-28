# -*- coding: utf-8 -*-
"""
PROYECTO O2
Unidad: Diseño y Análisis de Algoritmos
Alumno: Raquel Eugenia Meléndez Zamudio

Abril 2022

CLASE GRAFO 
IMPLEMENTACIÓN DE ALGORITMOS BFS Y DFS

"""

# Se importan las clases Nodo y Arista
from Node import node
from Edge import edge

class graph:
    
    #Atributos de la clase grafo
    def __init__(self, directed = False):
        self.name = 'Graph'
        self.directed = directed
        self.nodes = set(())
        self.edges = set(())
    
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
                
        return a
    
    # Obtiene el nodo indicado por su nombre
    def getNode(self, name):
        
        for i in self.nodes:
            if i.id == name:
                return i
    
    # Obtiene la arista indicada por su nombre
    def getEdge(self, name):
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
            value = value + str(i.id) +';\n'
        value = value + '}\n'
        
        return value
    
    # Se genera el archivo .gv con el nombre ingresado y el número de nodos en el grafo
    def fileGraphViz(self, file_name):
        graph2save = self.convertGraphViz()
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
            edges_split[cont] = str(i).split(sep = ' -- ')
            cont = cont + 1
        
        cont1 = 0
        for i,j in edges_split:
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
           edges_split[cont] = str(i).split(sep = ' -- ')
           cont = cont + 1
       
       cont1 = 0
       for i,j in edges_split:
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
            edges_split[cont] = str(i).split(sep = ' -- ')
            cont = cont + 1
        
        cont1 = 0
        for i,j in edges_split:
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
                    f.append((n0,n1))
                    
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
                
                
            
        
        
    